#!/usr/bin/env python3
"""check_prompt.py -- 提示词自查小工具（启发式检查，只读不写）。

用法：
    python3 check_prompt.py <prompt-file> [--kind image|video]

检查项：
    1. 长度（词数）：图片建议 <= 150 词，视频单 clip 建议 <= 200 词。
    2. 维度覆盖：图片九维 / 视频七维各写了几维（关键词启发式，仅供参考）。
    3. 模糊词：beautiful / amazing / stunning / 高质量 等空词。
    4. 否定词：no / without / don't / never（会把不想要的东西注入画面）。
    5. 画面内文字语言：引号、“”、''、【】里的文字是否中英混用。
    6. 首尾帧锁定（视频）：是否用了 @Image N is the first/last frame 句式。
    7. 语言混用与翻译腔：提示词正文（去掉画面内文字后）是否中英混杂；
       是否有直译翻车的词（atmosphere feeling / high-level feeling 等）。

退出码：0 = 通过；1 = 发现问题。
只读文件，不写任何东西，不联网。
"""

import re
import sys

VAGUE_WORDS = [
    "beautiful", "amazing", "stunning", "gorgeous", "masterpiece",
    "high quality", "best quality", "incredible", "breathtaking",
    "美丽", "好看", "高质量", "精美", "震撼", "绝美",
]
NEGATION_WORDS = [" no ", " without ", " don't ", " never ", " not "]

# 维度关键词（启发式：出现即算覆盖，仅供参考）
IMAGE_DIMENSIONS = {
    "主体": ["cat", "dog", "man", "woman", "girl", "boy", "character",
             "猫", "狗", "男人", "女人", "女孩", "角色", "小怪物"],
    "风格": ["photorealistic", "cinematic", "anime", "3d animated",
             "flat illustration", "watercolor", "vintage", "cyberpunk",
             "写实", "电影感", "动漫", "动画", "插画", "水彩", "复古"],
    "材质": ["matte", "glossy", "metal", "fabric", "plastic", "ceramic",
             "wooden", "velvet", "glass", "材质", "金属", "木质", "塑料"],
    "光线": ["light", "sunlight", "lamp", "shadow", "glow", "backlit",
             "光", "阳光", "灯", "影", "逆光", "暖光"],
    "构图": ["centered", "composition", "negative space", "foreground",
             "background", "构图", "居中", "留白", "前景", "背景"],
    "镜头": ["shot", "lens", "mm", "angle", "eye level", "close-up",
             "wide shot", "景别", "镜头", "焦段", "平视", "特写", "广角"],
    "色彩": ["palette", "color", "colour", "tone", "saturation",
             "色彩", "色调", "配色", "粉色", "暖色"],
    "氛围": ["mood", "atmosphere", "cozy", "quiet", "peaceful",
             "氛围", "情绪", "安静", "温馨"],
    "画质词": ["detailed", "sharp focus", "highly detailed", "细节", "清晰"],
}

VIDEO_DIMENSIONS = {
    "主体运动": ["walks", "runs", "leaps", "jumps", "crouches", "pushes",
                 "opens", "falls", "rises", "走", "跑", "跳", "蹲", "推", "开"],
    "镜头运动": ["tracking", "push-in", "push in", "pan", "tilt", "dolly",
                 "crane", "handheld", "aerial", "跟拍", "推近", "摇镜", "航拍"],
    "时间节奏": ["slow motion", "normal speed", "slow down", "speed up",
                 "慢动作", "常速", "变速", "停顿"],
    "转场": ["match cut", "hard cut", "cut to", "transition",
             "转场", "硬切", "匹配剪辑"],
    "首尾帧": ["first frame", "last frame", "首帧", "尾帧"],
    "音频": ["(", "<", "{", "music", "sound", "dialogue",
             "音乐", "音效", "对白", "字幕"],
    "一致性": ["consistent", "keep the", "throughout",
               "一致", "全程不变", "保持"],
}


def word_count(text):
    return len(text.split())


def check_dimensions(text, kind):
    dims = IMAGE_DIMENSIONS if kind == "image" else VIDEO_DIMENSIONS
    low = text.lower()
    covered, missing = [], []
    for name, keywords in dims.items():
        if any(k.lower() in low for k in keywords):
            covered.append(name)
        else:
            missing.append(name)
    return covered, missing


def find_vague(text):
    low = text.lower()
    return sorted({w for w in VAGUE_WORDS if w.lower() in low})


def find_negations(text):
    low = " " + text.lower().replace("\n", " ") + " "
    found = []
    for w in NEGATION_WORDS:
        if w in low:
            found.append(w.strip())
    return sorted(set(found))


def check_on_screen_text_language(text):
    """检查引号、【】里的画面内文字是否中英混用。"""
    spans = []
    spans += re.findall(r'"([^"]*)"', text)
    spans += re.findall(r'“([^”]*)”', text)
    spans += re.findall(r"'([^']*)'", text)
    spans += re.findall(r'【([^】]*)】', text)
    issues = []
    for s in spans:
        has_cjk = bool(re.search(r'[\u4e00-\u9fff]', s))
        has_latin = bool(re.search(r'[A-Za-z]{2,}', s))
        if has_cjk and has_latin:
            issues.append(s)
    return issues


def check_first_last_frame(text):
    has_first = bool(re.search(r'is the first frame', text, re.I))
    has_last = bool(re.search(r'is the last frame', text, re.I))
    return has_first, has_last


# 直译翻车的词（启发式，见到就提醒换成画面描述）
TRANSLATIONESE = [
    "atmosphere feeling",
    "high-level feeling",
    "rice white",
    "plant grass",
    "explosive product",
    "very beautiful",
    "very very",
]

# 不算混杂的东西：模型参数、锁定句式（平台语法，本来就是英文）
NOT_MIXING = [
    r'--ar\b', r'--no\b', r'--chaos\b', r'--stylize\b', r'--style\b',
    r'@image \d+ is the (first|last) frame\.?',
]


def strip_on_screen_text(text):
    """去掉引号、【】里的画面内文字，剩下的才是提示词正文。"""
    out = re.sub(r'"[^"]*"', ' ', text)
    out = re.sub(r'“[^”]*”', ' ', out)
    out = re.sub(r"'[^']*'", ' ', out)
    out = re.sub(r'【[^】]*】', ' ', out)
    return out


def check_language_mix(text):
    """检查提示词正文是否中英混杂、是否有翻译腔。

    返回 (mixed, translationese)：mixed 为 True 表示正文同时含
    5 个以上中文字和 5 个以上英文词；translationese 列出命中的直译词。
    """
    body = strip_on_screen_text(text)
    for pat in NOT_MIXING:
        body = re.sub(pat, ' ', body, flags=re.I)
    cjk_count = len(re.findall(r'[\u4e00-\u9fff]', body))
    latin_words = re.findall(r'[A-Za-z]{2,}', body)
    mixed = cjk_count >= 5 and len(latin_words) >= 5
    low = text.lower()
    found = sorted({w for w in TRANSLATIONESE if w in low})
    return mixed, found


def main():
    if len(sys.argv) < 2:
        print("用法：python3 check_prompt.py <prompt-file> [--kind image|video]")
        return 2
    path = sys.argv[1]
    kind = "image"
    if "--kind" in sys.argv:
        i = sys.argv.index("--kind")
        if i + 1 < len(sys.argv) and sys.argv[i + 1] in ("image", "video"):
            kind = sys.argv[i + 1]
    try:
        text = open(path, encoding="utf-8").read()
    except OSError as e:
        print(f"读文件失败：{e}")
        return 2

    problems = 0
    print(f"检查：{path}（{kind}）")
    wc = word_count(text)
    limit = 150 if kind == "image" else 200
    print(f"词数：{wc}", end=" ")
    if wc > limit:
        print(f"-- 超过建议长度 {limit} 词，考虑删减")
        problems += 1
    else:
        print("-- 长度合适")

    covered, missing = check_dimensions(text, kind)
    total = len(covered) + len(missing)
    print(f"维度覆盖：{len(covered)}/{total}（{', '.join(covered) or '无'}）")
    if missing:
        print(f"  缺失维度（供参考）：{', '.join(missing)}")
        problems += 1

    vague = find_vague(text)
    if vague:
        print(f"模糊词：{', '.join(vague)} -- 换成可见的具体描述")
        problems += 1
    else:
        print("模糊词：无")

    negations = find_negations(text)
    if negations:
        print(f"否定词：{', '.join(negations)} -- 改写成正面状态或删句")
        problems += 1
    else:
        print("否定词：无")

    mixed = check_on_screen_text_language(text)
    if mixed:
        print(f"画面内文字中英混用：{mixed} -- 只用一种语言")
        problems += 1
    else:
        print("画面内文字语言：无混用")

    if kind == "video":
        has_first, has_last = check_first_last_frame(text)
        print(f"首帧锁定：{'有' if has_first else '无'}；"
              f"尾帧锁定：{'有' if has_last else '无'}")

    mixed, translationese = check_language_mix(text)
    if mixed:
        print("语言混用：提示词正文里中英混杂 -- 按目标语言统一，"
              "模型参数和锁定句式除外")
        problems += 1
    else:
        print("语言混用：无")
    if translationese:
        print(f"翻译腔：{', '.join(translationese)} -- 换成可见的画面描述，"
              "不要直译抽象词")
        problems += 1
    else:
        print("翻译腔：无")

    print("结果：通过" if problems == 0 else f"结果：发现 {problems} 类问题")
    return 0 if problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
