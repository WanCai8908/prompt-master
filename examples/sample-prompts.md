# 提示词示例（sample-prompts）

六个完整例子，都能直接拿去用。每个例子都有英文版和中文版，意思一致，措辞按各自语言的习惯写，不逐句对译。中文说明只写给人看，不放进提示词正文。

---

## 例 1：图片生成——黄色圆润角色坐在粉色跑步机上

**用户原话**：“想要一张图，一个黄色的、圆滚滚的小怪物，坐在粉色跑步机上喝饮料，房间背景，3D 动画的感觉。”

**思路**：主体、风格、材质、光线、构图、镜头、色彩、氛围九维补齐；留白写清楚（上方留白给标题用）；画质词只留两个。

**给模型用的提示词**（英文版，可直接粘贴）：

```text
a yellow round chubby character with big blue eyes and tiny orange feet,
sitting on a pink treadmill, drinking from a green cup with a straw,
relaxed pose, one hand holding the cup, 3D animated film style,
soft rounded shapes, matte plastic texture, warm afternoon light
from the left window, soft shadows, cozy bedroom background with
a plant and a poster on the wall, centered composition,
generous negative space above the character, medium shot,
50mm lens, eye level, pink and cream palette with a pop of green,
warm tones, lazy Sunday afternoon mood, highly detailed, sharp focus
```

**给模型用的提示词**（中文版，可直接粘贴，中文友好的模型直接用）：

```text
一个黄色圆滚滚的角色，大大的蓝眼睛，小小的橘色脚丫，
坐在粉色跑步机上，用吸管喝着绿色杯子里的饮料，
姿势放松，一只手拿着杯子，3D 动画电影风格，
圆润柔和的造型，哑光塑料质感，午后暖光从左侧窗户照进来，
柔和的阴影，温馨的卧室背景，墙上有植物和一张海报，
居中构图，角色上方大面积留白，中景，50mm 镜头，平视，
粉白配色加一抹绿色，暖色调，慵懒的周日午后氛围，细节清晰，焦点锐利
```

**说明**：

- 主体写死了颜色、眼睛、脚、姿势和手里的杯子，模型没得猜。
- 风格锁了 3D 动画一种，没加其他风格词。
- 构图写了“上方留白”，以后加标题不用裁图。
- 背景只给了植物和海报两个元素，没塞太多东西。
- 负向提示词（Midjourney 用 `--no`，其他模型放负向栏）：`--no text, watermark, blurry, extra limbs, deformed hands`

---

## 例 2：图片优化前后对比——花园里的女孩

**用户贴来的原提示词**：

```text
a beautiful girl in a garden, high quality, 8k, no people in background,
amazing, stunning, masterpiece, ultra detailed, HDR
```

**诊断**：

- 问题 1（模糊词）：“beautiful”“amazing”“stunning”“masterpiece”全是空词，模型无法执行。
- 问题 2（否定词）：“no people in background”会把 people 塞进画面，背景反而容易出现人。
- 问题 3（画质词堆叠）：“high quality, 8k, ultra detailed, HDR”堆了四个，挤占有效长度。
- 问题 4（缺失维度）：没写女孩长什么样、穿什么、什么姿势；没写光线、镜头、色彩、季节。
- 问题 5（矛盾）：主角是女孩，背景又“不要人”，意图其实是“背景干净”，写错了地方。

**优化后的提示词**（英文版，可直接粘贴）：

```text
a young woman in her early twenties, long black hair, white cotton dress,
standing by a wooden window, looking back over her shoulder,
quiet garden behind her, empty stone path, no other figures in sight,
soft morning light, gentle haze, 35mm lens, eye level, medium shot,
green and cream palette, calm and still mood, highly detailed, sharp focus
```

**优化后的提示词**（中文版，可直接粘贴）：

```text
一位二十岁出头的年轻女子，黑色长发，白色棉布连衣裙，
站在木窗边，回头看向身后，
身后是安静的花园，空无一人的石子小路，
清晨柔和的光线，淡淡薄雾，35mm 镜头，平视，中景，
绿色与米白配色，平静安宁的氛围，细节清晰，焦点锐利
```

**改了什么**：

- “beautiful”换成具体长相：二十岁出头、黑色长发、白色棉布裙、站在木窗边回头。
- “no people in background”改成正面状态：`empty stone path, no other figures in sight`——背景干净的意思写清楚了，不用否定词。
- 画质词从四个砍到两个：`highly detailed, sharp focus`。
- 补了光线（清晨柔光 + 薄雾）、镜头（35mm、平视、中景）、色彩（绿 + 米白）、氛围（安静）。
- “amazing / stunning / masterpiece”全部删掉，没留一个空词。

---

## 例 3：视频生成（含首尾帧锁定）——橘猫偷小鱼

**用户原话**：“做一段视频，清晨厨房，一只橘猫从窗台跳上餐桌，偷走一条小鱼。开头是猫蹲在窗台，结尾是猫叼着鱼跳下桌子。”

**思路**：Seedance 七段结构；首帧锁猫蹲窗台，尾帧锁猫叼鱼下桌；事件分三段，每段只讲一件主要的事；声音只写实际能听到的（没对白就不写对白栏）。

**给模型用的提示词**（英文版，可直接粘贴）：

```text
目标：Generate a short cinematic video: in a quiet kitchen at dawn,
an orange tabby cat leaps from the windowsill onto the dining table
and steals a small fish, then jumps down with it.

参考图分工：
@Image 1 is the first frame. The cat crouches on the windowsill,
tail low, eyes fixed on the table.
@Image 2 is the last frame. The cat lands on the kitchen floor
with the fish in its mouth, looking toward the door.

人物与站位：
The cat is an orange tabby with a white chest, corresponding to @Image 1.
The dining table stands in the middle of the kitchen, the windowsill
on the left wall above the sink. A plate with a small fish sits
at the far edge of the table, near the window side.

事件分段：
第一段：开头画面是猫蹲在窗台上，尾巴低垂，盯着桌上的盘子。
猫后腿一蹬，划出一道弧线落在桌边。结束时猫四脚站在桌上，尾巴竖起。
第二段：接着上一段。猫压低身子，慢慢靠近盘子，叼起小鱼。
结束时鱼在猫嘴里，猫的耳朵向后贴。
第三段：猫叼着鱼从桌沿跳下，落地时前爪先着地，头也不回地朝门口跑去。
结束时猫站在门口回头看了一眼，画面静止。

镜头与光线：
Slow push-in from a wide shot of the kitchen to a close-up of the paws
as the cat lands. Cold dawn light comes through the window from the left,
a thin warm lamp glow from the hallway behind. Normal speed through
the approach; time slows for a beat as the cat snatches the fish,
then returns to normal speed.

声音：
(soft piano, slow) <paws thudding on wood, a plate sliding, the cat's
quiet breathing>

收尾与一致性：
Keep the cat's orange tabby coat with white chest, the table layout,
the plate position, the window light, and the camera's side of the
scene consistent throughout.
```

**给模型用的提示词**（中文版，可直接粘贴，中文模型直接用；锁定句式和音频标记保持英文原句）：

```text
目标：生成一段电影感短视频：清晨安静的厨房里，一只橘猫从窗台跳上餐桌，
偷走一条小鱼，然后叼着鱼跳下桌子。

参考图分工：
@Image 1 is the first frame. 猫蹲在窗台上，尾巴低垂，眼睛盯着桌子。
@Image 2 is the last frame. 猫叼着鱼落在厨房地板上，看向门口。

人物与站位：
猫是橘色虎斑、白胸脯，对应 @Image 1。
餐桌在厨房中间，窗台在左侧墙上、水槽上方。
一只装着小鱼的盘子放在桌子远端、靠窗那一侧。

事件分段：
第一段：开头画面是猫蹲在窗台上，尾巴低垂，盯着桌上的盘子。
猫后腿一蹬，划出一道弧线落在桌边。结束时猫四脚站在桌上，尾巴竖起。
第二段：接着上一段。猫压低身子，慢慢靠近盘子，叼起小鱼。
结束时鱼在猫嘴里，猫的耳朵向后贴。
第三段：猫叼着鱼从桌沿跳下，落地时前爪先着地，头也不回地朝门口跑去。
结束时猫站在门口回头看了一眼，画面静止。

镜头与光线：
从厨房全景慢慢推近到猫爪特写。清晨冷光从左侧窗户进来，
身后走廊透出一线暖色灯光。靠近时常速；叼鱼的一瞬放慢，
随后恢复常速。

声音：
(soft piano, slow) <paws thudding on wood, a plate sliding, the cat's
quiet breathing>

收尾与一致性：
全程保持不变：猫的橘色虎斑配白胸脯、桌子布局、盘子位置、
窗光、镜头所在的动作轴一侧。
```

**说明**：

- 首帧和尾帧各用一句锁定句式写死，再各补一句构图描述；两帧比例一致，提交时用同一比例。
- 事件分三段：跳上桌、叼鱼、跳下桌，每段一件主要的事，段尾都落到能看见的状态。
- 没对白就不写对白栏，只写音乐和音效；音效都和画面动作对得上。
- “冷光从左窗进来 + 走廊暖光在后”是光线的主次关系，不是两个打架的光源。
- 一致性里写了猫的花色、桌子布局、盘子位置、窗光、镜头一侧，五样全程不能变。

---

## 例 4：营销文案——随行杯社媒帖子

**用户原话**：“帮我写个文案，卖一款 300ml 的随行保温杯，保温 8 小时，单手开盖，卖 20 万只了，好评率 98%，发小红书和朋友圈。”

**思路**：营销文案模板（受众 → 痛点 → 卖点 → 社会证明 → 行动号召）；卖点只留三个，每个都配事实或数字；行动号召只给一个；中英文各写各的，不直译口号。

**中文版**（可直接发布）：

```text
每天通勤两小时的上班族，早上起不来、晚上到家只想躺平？
这款 300ml 随行杯保温 8 小时，单手开盖，地铁上也能喝。
已卖出 20 万只，好评率 98%。今天下单，明天到手。
```

**英文版**（可直接发布）：

```text
Two-hour commute, too tired to make coffee in the morning?
This 300ml travel mug keeps drinks hot for 8 hours and opens with one hand, even on the subway.
200,000 sold, 98% positive reviews. Order today, get it tomorrow.
```

**说明**：

- 受众一句话定死：通勤两小时的上班族，不是“所有人”。
- 痛点写了一个具体场景（早上起不来），没写“你有烦恼吗”这种空话。
- 卖点三个，每个都有数字：8 小时、单手开盖、20 万只 / 98%。
- 英文版没直译中文口号，按英文社媒的习惯重写了一遍，意思一致。

---

## 例 5：电商商品主图——白色陶瓷随行杯

**用户原话**：“给我一张商品主图，白色陶瓷随行杯，300ml，哑光的，要显得防水，背景干净，上方留白放标题。”

**思路**：电商主图模板；卖点视觉化（防水 → 水珠挂在表面）；留白位置写死在上方；品牌色锁定；中英各一份。

**给模型用的提示词**（英文版，可直接粘贴）：

```text
a white ceramic travel mug, 300ml, matte finish, fine water droplets
clinging to the surface, standing on a light wooden table,
minimal studio product photography, soft light from the left,
gentle shadows, centered composition, generous negative space above
for headline text, cream background, 85mm lens, eye level,
clean and premium, highly detailed, sharp focus
--no text, watermark, blurry, extra objects
```

**给模型用的提示词**（中文版，可直接粘贴）：

```text
白色陶瓷随行杯，300ml，哑光表面，细密水珠挂在杯身上，
放在浅色木桌上，极简影棚产品摄影，左侧柔光，阴影轻柔，
居中构图，上方大面积留白放标题，米白背景，85mm 镜头，平视，
干净高级，细节清晰，焦点锐利
负向：不要文字、水印、模糊、多余物品
```

**说明**：

- “防水”没写成 `waterproof` 一个词，而是写成可见的水珠挂在表面，模型才能画出来。
- 留白写死了位置（上方）和用途（放标题），以后加字不用裁图。
- 背景只给了米白一个颜色，没抢产品风头。
- 负向词只放画面通病，没放剧情否定。

---

## 例 6：Agent 任务指令——给 check_prompt.py 加语言混用检测

**用户原话**：“让编程助手给 check_prompt.py 加一个功能：检测提示词正文里中英混杂的情况。只读不写，别改现有函数。”

**思路**：Agent 任务指令模板（角色 → 目标 → 输入 → 约束 → 成功标准 → 边界情况 → 出错处理）；目标只写一个；约束里写清“不要改什么”；成功标准要能验证。

**中文版**（可直接发给编程助手）：

```text
角色：资深 Python 工程师。
目标：给 check_prompt.py 加一个语言混用检测函数。
输入：文件在 scripts/check_prompt.py，现有检查项见文件头注释；
检测对象是提示词正文，先去掉引号、【】里的画面内文字再判断。
约束：
- 只读不写，不改现有函数签名，不引入新依赖。
- 提示词正文里同时出现 5 个以上中文字和 5 个以上英文词，才报中英混杂。
- 模型参数（--ar、--no）和锁定句式（@Image N is the first frame.）不算混杂。
成功标准：中英混杂的提示词报出问题，纯中文或纯英文的通过；
附一次实测（混杂的和干净的各测一个）。
边界情况：空文件、只有符号的输入不报错。
出错处理：读文件失败时返回退出码 2 并打印原因。
```

**英文版**（可直接发给编程助手）：

```text
Role: senior Python engineer.
Objective: add a language-mixing detection function to check_prompt.py.
Input: the file is at scripts/check_prompt.py; existing checks are listed
in the header comment. Check the prompt body only: strip quoted text
and 【】 on-screen text before judging.
Constraints:
- Read-only; do not change existing function signatures; no new dependencies.
- Report mixing only when the body contains 5+ Chinese characters AND 5+ English words.
- Model parameters (--ar, --no) and lock sentences (@Image N is the first frame.) do not count as mixing.
Success criteria: a mixed-language prompt is flagged; a pure Chinese or pure English prompt passes;
include one test run (one mixed, one clean).
Edge cases: empty files and symbol-only input must not crash.
Error handling: return exit code 2 with a printed reason when the file cannot be read.
```

**说明**：

- 目标只有一个：加一个检测函数，没顺带让它“顺便优化一下别的”。
- 约束里“不要改现有函数签名”比“要改什么”更重要，先写清楚。
- 成功标准能量化：混杂的报出来、干净的通过、附实测。
- 边界情况和出错处理各写了一句，没留给模型自己猜。
