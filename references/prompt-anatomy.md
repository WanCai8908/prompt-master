# 提示词结构拆解（prompt-anatomy）

提示词不是散文，是按维度拼出来的说明书。这篇把图片九维、视频七维、负向词表、六个万能模板和七个新场景（文案/营销、电商、教育、代码/Agent、音频/音乐、3D/设计、日常办公）一次讲透。所有词表、模板、例子都有中英对照。

---

## 一、图片提示词：九维

九维不必全写满。没内容的维度空着，不硬凑；核心是**主体 + 风格 + 光线 + 镜头**四维不能空。

### 1. 主体（Subject）

写什么：是谁 / 什么，有几个，长什么样，穿什么，什么姿态。

- 数量写死：`one cat`、`two dancers`，不要写 `some cats`。
- 外貌写可见特征：年龄感、发型、体型、标志性物件，不要写性格标签。
- 姿态写定格瞬间：`sitting, leaning forward, holding a cup`，不要写“正在享受”。

```text
a yellow round character with big blue eyes, sitting on a pink treadmill,
drinking from a green cup with a straw
```

### 2. 风格（Style）

写什么：画面整体长什么样。只锁一种风格词，全篇不漂移。

常用风格词：

| 风格 | 英文写法 |
|---|---|
| 写实照片 | photorealistic, shot on 35mm film, natural skin texture |
| 电影感 | cinematic, film still, anamorphic, teal and orange grade |
| 3D 动画 | 3D animated film style, soft rounded shapes, Pixar-like |
| 动漫 | anime style, clean line art, cel shading |
| 扁平插画 | flat illustration, bold shapes, minimal detail |
| 水彩 | watercolor painting, soft edges, paper texture |
| 复古 | vintage photograph, faded colors, film grain |
| 赛博朋克 | cyberpunk, neon lights, rain-slick streets |

进阶风格（按组挑，每次只锁一组里的一种）：

| 组 | 风格 | 英文写法 |
|---|---|---|
| 艺术流派 | 印象派 / 浮世绘 / 装饰艺术 / 波普艺术 | impressionist painting / ukiyo-e woodblock print / art deco / pop art |
| 材质工艺 | 粘土定格 / 像素风 / 等距插画 / 双重曝光 | claymation, handmade clay texture / pixel art, 16-bit / isometric illustration / double exposure |
| 摄影 looks | 红外摄影 / 移轴摄影 / 宝丽来 | infrared photography, surreal foliage / tilt-shift photography, miniature look / Polaroid photo, instant film |
| 渲染质感 | 黏土渲染 / 体素 | clay render, soft matte material / voxel art, blocky 3D |

挑风格时先想画面长什么样，再从表里点名；一组里只锁一种，两种风格词混写一定打架。

### 3. 材质（Material）

写什么：表面的质感。材质词是“高级感”最便宜的来源。

```text
matte plastic（哑光塑料）, fluffy knitted fabric（毛绒针织面料）,
glossy ceramic（亮面陶瓷）, brushed metal（拉丝金属）,
rough concrete（粗糙水泥）, soft velvet（丝绒）, translucent glass（透明玻璃）
```

### 4. 光线（Light）

写什么：光源 + 方向 + 质感。不要只写“好看的光”。

- 光源：`warm afternoon sunlight / a streetlamp glowing orange overhead / a neon sign`
- 方向：`from the left window / from above / backlit`
- 质感：`soft shadows / hard light / golden hour glow / rim light`

```text
warm afternoon light from the left window, soft shadows,
a thin rim light on the character's outline
```

### 5. 构图（Composition）

写什么：主体在哪、留白多少、前后景关系。

```text
centered composition, generous negative space above the subject,
a blurred plant in the foreground, the treadmill fills the lower third
```

### 6. 镜头（Camera）

写什么：景别 + 焦段 + 角度。景别、焦段、角度要互相配得上：远景配广角、特写配长焦，别写出镜头装不下的画面。

- 景别：`extreme close-up / close-up / medium shot / full shot / wide shot`
- 焦段：`35mm / 50mm / 85mm / 200mm telephoto`
- 角度：`eye level / low angle / high angle / bird's-eye view / Dutch angle`

```text
medium shot, 50mm lens, eye level, shallow depth of field
```

景别从远到近排一排，画面里装的东西越来越少、细节越来越多：大远景里环境是主角、人物只是个点；远景是人物全身加大量环境；全景是人物全身、环境刚好交代清楚；中景是腰部以上；近景是胸部以上；特写是一张脸或一件东西；大特写是一只眼睛、一枚戒指。

焦段决定透视：广角（35mm 以下）把空间拉开，近处的东西显得更大，适合拍建筑、拍气势；长焦（85mm 以上）把空间压扁，前后景挤在一起，适合拍人像、拍远处的细节。人像用 85mm 左右，大场面用广角，别反过来。

### 7. 色彩（Color）

写什么：主色调和配色关系，落到具体颜色上，不要只写“色彩丰富”。

```text
pink and cream palette with a pop of green, warm tones,
high saturation, soft pastel background
```

### 8. 氛围（Mood）

写什么：情绪，但必须落到可见的东西上。只写情绪词等于没写。

- 不要写：`lonely, hopeful, epic`
- 要写：`an empty street at dusk, one figure walking away, long shadows`

```text
cozy lazy Sunday afternoon mood: warm light, a half-finished drink,
the room quiet except for the treadmill hum
```

### 9. 画质词（Quality）

适量，不要堆叠。留一两个就够，多了挤占有效长度还容易出塑料感。

```text
highly detailed, sharp focus
```

不要堆：`8k, ultra detailed, HDR, best quality, masterpiece, stunning, amazing` 全上等于什么都没说。

---

## 二、视频提示词：七维

### 1. 主体运动（Subject Motion）

写什么：谁动、怎么动。动词要具体，不要用 `do something / go there / make it happen` 这类空动词。

```text
the cat crouches low, then leaps in one smooth arc onto the desk,
lands on all fours, tail high
```

具体动词表（中英对照）：`shoves（猛推）, yanks（猛拽）, spins（旋转）, dashes（疾跑）, drags（拖）, flicks（轻弹）, pounds（猛击）, grabs（抓住）, twists（扭）, hurls（扔）, crouches（蹲下）, leaps（跃起）`。

图生视频时别复述画面：图里已有的长相、衣服、场景不用再写，写接下来发生什么。运动分三层写——前景（离镜头最近的东西）、中景（主体）、背景（远处的东西），主动作写清楚，其他两层轻一点。人脸可见时，写小的表情变化（眼神移动、眯眼、呼吸、衣角被风带起），比大动作更像真人。

### 2. 镜头运动（Camera Motion）

写什么：景别 + 运镜 + 方向 + 目标。

```text
slow push-in from a wide shot to a close-up of the paws,
camera tracks forward at eye level, staying on the same side throughout the move
```

运镜词（中英对照）：`static（固定机位） / pan（摇镜） / tilt（俯仰） / tracking（跟拍） / dolly in-out（推拉） / crane up（升降） / handheld（手持） / FPV（第一人称） / aerial（航拍） / orbit（环绕）`。

高级运镜（一个镜头里只用一种，两个叠着用会打架）：快速摇镜 whip pan——镜头猛地甩向一边，常用来转场；急速变焦 crash zoom——突然推近或拉远，制造冲击；焦点转移 rack focus——焦点从前景挪到后景、或反过来，带着视线走；动作匹配 match on action——上一个镜头的动作在下一个镜头里接着做，剪辑点藏在动作里。

### 3. 时间节奏（Pacing）

写什么：快慢、停顿、变速点。速度要写在画面上，不要写在努力词上。

- 不要写：`he runs with all his might`（模型读到的还是普通跑步）。
- 要写：`shop signs flash past, dust kicks up at his heels, the frame edge blurs with motion`。

```text
normal speed while the cat approaches; the landing plays in slow motion,
then back to normal speed
```

### 4. 转场（Transition）

写什么：镜头之间怎么接。多镜头默认写清衔接方式。

- 抽上一段尾帧做下一段首帧：`the next clip starts from the last frame of this one`。
- 匹配剪辑：`match cut on the landing`。
- 硬切：`hard cut to the close-up`。

### 5. 首尾帧（First / Last Frame）

锁定句式，一字不改：

```text
@Image 1 is the first frame.
@Image 2 is the last frame.
```

- 首帧决定输出比例，首尾帧必须同比例。
- 锁定后要另起一句描述该帧的构图（主体位置、姿态、道具、镜头方向）。
- 不要弱化成“参考开头构图”——模型不会当真。

### 6. 音频（Audio）

四种声音分开写，语法（Seedance 约定）：

| 类型 | 语法 | 例子 |
|---|---|---|
| 音乐 | `()` | `(soft piano, slow)` |
| 音效 | `<>` | `<paws thudding on wood>` |
| 对白 | `{}` | `{Wait for me.}` |
| 字幕 | `` | `` |

- 对白只能用用户原话，一个字都不能编。
- 每个说话的人给一行声音描述 + 语种：`The woman says in a soft, tired voice, {Wait for me.} Only the woman speaks.`
- 没有对白的片段不要写对白栏，空着。

### 7. 一致性（Consistency）

一句话列出全程不能变的东西：身份和服装、道具数量和归属、空间朝向、镜头所在的动作轴一侧。

```text
Keep the cat's orange tabby coat, the desk layout, the window light,
and the camera's side of the scene consistent throughout.
```

---

## 三、负向提示词词表

### 原则

优先用正面状态代替否定。真正放进负向的只剩“画面通病”。

### 通用翻车词（画面通病类，可进负向）

```text
extra fingers（多余手指）, deformed hands（变形的手）, distorted face（扭曲的脸）,
blurry（模糊）, out of focus（失焦）, overexposed（过曝）, underexposed（欠曝）,
low quality（低质量）, noisy（噪点）, watermark（水印）, text artifact（文字乱码）,
cropped（裁切不全）, cut off（切掉一半）, duplicate（重复）, disfigured（畸形）,
bad anatomy（结构错误）, extra limbs（多余肢体）
```

### 不要放进负向的东西

- 剧情否定：`no running`、`no smiling`——模型经常反向执行，改写成要他做什么。
- 具体物品否定：`no umbrella`——会把 umbrella 注入画面，改写成正面状态（双手空着，站在屋檐下）。
- 风格否定：`no cartoon style`——不如直接写死要的风格。

### 分模型写法

- Midjourney：用 `--no` 参数，例如 `--no text, watermark, blurry`。
- 多数视频模型：没有独立负向栏，否定写成正面状态或删句。
- 有负向栏的模型：只放画面通病类词，不要放剧情类否定。

---

## 四、万能模板（模板 1–3）

### 模板 1：电影感短片（视频）

```text
目标：<一句话：类型 + 主体 + 主事件>

参考图分工：
@Image 1 负责 <角色 1 的外貌、服装>，不用图里的背景。
@Image 2 负责 <环境的墙面、地面、光线>，只是风格参考，不是固定机位，模型可以自己扩展世界。

人物与站位：
<主体绑定参考图 + 固定属性；拿不动的东西当参照，定内外、前后、朝向、距离>

事件分段：
第一段：开头画面是 <...>。<一件主要的事>。结束时 <能看见的状态>。
第二段：接着上一段。<...>。结束时 <...>。
第三段：<...>。结束时 <静止状态，让剪辑有落点>。

镜头与光线：
<运镜 + 光线 + 色彩，落到具体的东西上；最关键的一刻，挑一种具体的拍法来撑场面：长镜头跟拍、变焦突进、无人机俯冲、第一人称、慢动作定格、肩扛跟拍>

声音：
<音乐 () / 音效 <> / 对白 {} / 字幕 【】，只写实际能听到的>

收尾与一致性：
<身份、服装、道具、空间朝向、镜头一侧>全程不变。
```

### 模板 2：产品图（图片）

```text
<主体：产品名 + 材质 + 颜色 + 关键特征>, <姿态 / 摆放>,
<风格：studio product photography / minimal>,
<光线：soft studio light from the left, gentle shadows>,
<构图：centered, generous negative space, <品牌色> background>,
<镜头：medium shot, 85mm, eye level>,
<色彩：<品牌主色> palette, clean and premium>,
<画质词：highly detailed, sharp focus>
--no text, watermark, blurry, extra objects
```

要点：产品图留白是给文案留的，构图里写清留白位置；品牌色写死色值或颜色名；背景越干净越好。

### 模板 3：角色一致性（图片 + 视频通用）

```text
角色锚点（写一次，全片复用，一字不改）：
<名字>：<年龄感>，<脸型 / 五官>，<发型 / 发色>，<体型>，
<标志性服装>，<标志性道具>。注册为 @<名字>。

每段提示词里只写三样，不再重复描述外貌：
1. 动作：<具体动词 + 身体部位>
2. 服装状态：<穿着 / 拿着 / 脱下>
3. 光线：<光源 + 方向>

示例：
@阿远，穿着一件洗旧的蓝色工装，单手把木门推开一条缝，
门外的冷光斜切进来，照亮他半张脸。
```

要点：角色锚点一经注册就只用 tag，不再重复外貌；多角色同框时用发型、服装、剪影区分开；环境参考只定风格，不定机位。

进阶：表情表 + 种子固定。

- **表情表**：同一个角色、同一套衣服、同一张脸，先做一张九宫格出来：笑、皱眉、回头、挥手、坐下、跑起来……以后每张图直接说“用表情表里第几个表情”，长相不用每次重写。表情表本身也是一张图，生成时写清楚“同一角色，九种表情，九宫格排列，表情之间不串味”。比如黄色圆润角色那张图，先做一张它在粉色跑步机上的九种表情表，后面每张图直接指表情编号。
- **种子固定**：出到一张满意的图，把它的种子值记下来（Midjourney 用 `--seed`）。下次微调提示词时种子别动，只改一处，改动才可控；种子一换，整张图都会变。

---

## 五、新场景结构小节

图片、视频之外的场景，结构换一换，铁律不变（不改意图、不编事实、不编参数、画面文字单语言、中英同步）。

### 1. 文案 / 营销（Copy & Marketing）

结构：受众 → 痛点 → 卖点 → 社会证明 → 行动号召。

- 受众：写给谁，一句话定死（年龄、身份、场景），不要写“所有人”。
- 痛点：用户现在难受在哪，写一个具体场景，不要写“你有烦恼吗”。
- 卖点：只写三个以内，每个卖点配一个可验证的事实或数字。
- 社会证明：用户数、评分、真实评价，三选一，要有出处。
- 行动号召：只给一个动作（点链接 / 留言 / 下单），不要三个一起上。
- 语言：中文受众出中文，英文受众出英文；口号不直译，两个版本各写各的。

简短例子（中文版）：

```text
给每天通勤两小时的上班族：早上起不来、晚上到家只想躺平？
这款 300ml 随行杯保温 8 小时，单手开盖，地铁上也能喝。
已卖出 20 万只，好评率 98%。今天下单，明天到手。
```

英文版：

```text
For commuters with a two-hour daily ride: too tired to make coffee in the morning?
This 300ml travel mug keeps drinks hot for 8 hours and opens with one hand, even on the subway.
200,000 sold, 98% positive reviews. Order today, get it tomorrow.
```

### 2. 电商（E-commerce）

图片结构：主体九维 + 卖点视觉化 + 留白给文案 + 品牌色锁定。

- 卖点视觉化：每个卖点对应一个可见的东西（防水 → 水珠挂在表面；轻 → 单手拎起）。
- 留白：主图上方或一侧留白，写清留白位置（以后放标题和价格）。
- 背景：越干净越好，品牌色做底色，不要抢产品风头。

文案结构：产品名 → 三个卖点 → 规格 → 售后 → 行动号召。

简短例子（主图提示词，中英对照）：

```text
英文：a white ceramic travel mug, 300ml, matte finish, water droplets on the surface,
standing on a light wooden table, minimal studio product photography,
soft light from the left, centered, generous negative space above,
cream background, highly detailed, sharp focus
中文：白色陶瓷随行杯，300ml，哑光表面挂着水珠，放在浅色木桌上，
极简影棚产品摄影，左侧柔光，居中构图，上方大面积留白，
米白背景，细节清晰，焦点锐利
```

### 3. 教育（Education）

结构：学习目标 → 讲解步骤 → 例子 → 自测题 → 总结。

- 学习目标：一句话，学完能做什么（能算出 / 能讲清 / 能写出）。
- 讲解步骤：每步只讲一个概念，配一个生活里的例子。
- 自测题：2–3 道，答案单独给，不要混在题目里。
- 语言：给中国学生出中文，给海外学生出英文；术语第一次出现时给中英对照。

简短例子（中文版）：

```text
目标：学完能用一句话讲清什么是“光圈”。
步骤：1. 光圈是镜头里的可变小孔；2. 数字越小孔越大、进光越多、背景越虚；
3. 生活例子：猫的瞳孔白天缩成线、晚上张得圆圆的。
自测：光圈 f/1.8 和 f/8，哪个背景更虚？答案：f/1.8。
```

### 4. 代码 / Agent 提示词（Code & Agent）

结构：角色 → 目标 → 输入 → 约束 → 成功标准 → 边界情况 → 出错处理。

- 角色：一句话定身份（“你是一个资深 Python 工程师”），不要写成长篇人设。
- 目标：只写一个目标，动词开头（“写一个函数……”“修掉这个 bug……”）。
- 输入：给全上下文（文件路径、相关代码、报错原文），不要让模型猜。
- 约束：列出不能做的事（不要改无关文件、不要升级依赖、不要改接口）。
- 成功标准：怎么写才算完成（测试通过、输出格式、性能要求）。
- 边界情况：空输入、超大输入、网络失败，各写一句怎么处理。
- 语言：代码任务用英文写指令通常更稳（标识符、注释习惯英文），但需求本身是中文就用中文写需求、英文写约束，两部分分开。

简短例子（中文版）：

```text
角色：资深 Python 工程师。
目标：给 check_prompt.py 加一个语言混用检测函数。
输入：文件在 scripts/check_prompt.py，现有检查项见文件头注释。
约束：只读不写，不改现有函数签名，不引入新依赖。
成功标准：中英混杂的提示词报出问题，纯中文或纯英文的通过；附一次实测。
边界情况：空文件、只有符号的输入不报错。
出错处理：读文件失败时返回退出码 2 并打印原因。
```

### 文本提示词通用技法（写给 LLM 的提示词都适用）

图像提示词靠维度堆，文本提示词靠结构清。下面四条放在哪个文字场景都适用：

- **围栏分隔**：指令和输入要分开写，别揉在一起。输入用 ``` 或 `<input>` 标签包起来，例子用 `<example>` 标签包起来，这样模型才不会把用户贴进来的文字当成指令。
- **少样本**：给 2–5 个例子，例子要贴近真实任务，再带一两个边界情况。例子比规则管用：想让输出格式固定，举一个格式正确的例子，比写三行格式要求更稳。例子里的事实必须是用户确认过的，不要编。
- **平实语气**：“必须、绝不、CRITICAL”这类重话别用。新模型对重话反应过度——本来只想收紧一处，结果处处都收紧了。平常说法就够了。
- **先想后答**：要推理的任务（判断、计算、多步分析），让模型先一步一步想清楚再给答案。简单任务不用这套，硬加反而啰嗦。

### 5. 音频 / 音乐（Audio & Music）

结构：情绪 → 配器 / 音色 → 节奏 → 长度 → 参考。

- 情绪：先定情绪，再定配器（悲伤不一定用钢琴，写具体乐器）。
- 音色：写乐器 + 演奏方式（指弹吉他、闷音贝斯、呼吸感人声）。
- 节奏：BPM 或快慢描述 + 有没有变速点。
- 长度：写清秒数或小节数。
- 音效：每个音效落到具体声音上（雨声打在铁皮上、木门吱呀一声）。

简短例子（中英对照）：

```text
英文：(soft piano, slow, 60 BPM, 30 seconds) <rain on a tin roof,
a wooden door creaking open> calm, warm, late-night mood
中文：轻柔钢琴，慢速，60 BPM，30 秒；音效是雨打铁皮屋顶、木门吱呀一声；
情绪是深夜的安静和暖意
```

### 6. 3D / 设计（3D & Design）

结构：图片九维 + 版式 → 字阶 → 配色规范 → 输出要求。

- 版式：写清网格、留白、对齐（居中 / 左对齐 / 黄金比例）。
- 字阶：标题、正文、注释的字号关系（标题是正文的 2 倍之类），不要只写“大标题”。
- 配色规范：主色、辅色、点缀色写死色值或颜色名。
- LOGO / 海报：画面内文字必须单语言，文字内容用户给什么写什么，一个字不改。
- 3D 建模：写清视角（等距 / 透视）、渲染风格（粘土 / 写实 / 卡通）、材质。

简短例子（LOGO 提示词，中英对照）：

```text
英文：minimal logo for a coffee brand, a simple line-art coffee cup
with steam forming a small heart, warm brown and cream palette,
flat vector style, generous negative space, no text
中文：咖啡品牌极简 LOGO，线条风咖啡杯，蒸汽弯成一颗小爱心，
暖棕 + 米白配色，扁平矢量风，大量留白，不要文字
```

### 7. 日常办公（Office）

结构：目的 → 受众 → 要点 → 格式 → 篇幅。

- 目的：这份东西用来干什么（汇报 / 请批 / 同步信息），一句话。
- 受众：给谁看（老板 / 客户 / 全组），语气跟着受众走。
- 要点：最多 5 条，按重要性排序。
- 格式：邮件 / 总结 / PPT 大纲，写清结构（总分总 / 时间顺序 / 问题-方案）。
- 篇幅：写清字数或页数上限，不要写“越短越好”。

简短例子（邮件提示词，中文版）：

```text
目的：向客户同步项目延期一周的原因和新的交付时间。
受众：客户项目经理，语气正式、直接，不找借口。
要点：1. 延期原因：第三方接口晚了三天；2. 新交付日：下周五；
3. 补救：已加人手，本周五先交付核心功能。
格式：邮件，三段：说明、原因、新的时间表。300 字以内。
```

---

## 六、新增模板（模板 4–6，中英对照）

### 模板 4：营销文案（文字）

```text
中文版：
受众：<一句话：年龄、身份、场景>
痛点：<一个具体场景，不要写“你有烦恼吗”>
卖点（最多三个）：
1. <卖点 + 可验证的事实或数字>
2. <卖点 + 可验证的事实或数字>
3. <卖点 + 可验证的事实或数字>
社会证明：<用户数 / 评分 / 真实评价，三选一，要有出处>
行动号召：<只给一个动作>

英文版（不直译中文口号，各写各的）：
Audience: <one line: age, identity, situation>
Pain point: <one concrete scene>
Selling points (max three):
1. <benefit + verifiable fact or number>
2. <benefit + verifiable fact or number>
3. <benefit + verifiable fact or number>
Social proof: <user count / rating / real review, one only, with source>
Call to action: <one action only>
```

要点：卖点没有事实支撑就是空话；社会证明没有出处就是编造；行动号召只能有一个。

### 模板 5：Agent 任务指令（文字）

```text
中文版：
角色：<一句话身份，如“资深 Python 工程师”>
目标：<只写一个目标，动词开头>
输入：<文件路径、相关代码、报错原文，给全上下文>
约束：
- <不能做的事 1>
- <不能做的事 2>
成功标准：<怎么写才算完成：测试通过 / 输出格式 / 性能要求>
边界情况：<空输入 / 超大输入 / 网络失败，各一句>
出错处理：<失败时怎么办>

英文版：
Role: <one-line identity, e.g. "senior Python engineer">
Objective: <one goal only, starting with a verb>
Input: <file paths, relevant code, error messages, full context>
Constraints:
- <do-not-do 1>
- <do-not-do 2>
Success criteria: <what counts as done: tests pass / output format / performance>
Edge cases: <empty input / huge input / network failure, one line each>
Error handling: <what to do on failure>
```

要点：目标只能有一个；约束里写“不要改无关文件”比写一堆“要改什么”更重要；成功标准要能验证（测试通过、输出长什么样），不要写“做得好一点”。

### 模板 6：电商商品主图（图片）

```text
英文版：
<product name>, <material>, <color>, <key feature>,
<pose / placement>, <selling point made visible>,
<studio product photography / minimal>, <light: source + direction>,
<composition: centered, negative space for copy>,
<background: brand color>, <lens: 85mm, eye level>,
<color palette: brand colors>, highly detailed, sharp focus
--no text, watermark, blurry, extra objects

中文版：
<产品名>，<材质>，<颜色>，<关键特征>，
<摆放姿态>，<卖点视觉化：防水 → 水珠挂在表面>，
<影棚产品摄影 / 极简>，<光线：光源 + 方向>，
<构图：居中，留白给文案>，
<背景：品牌色>，<镜头：85mm，平视>，
<色彩：品牌配色>，细节清晰，焦点锐利
负向：不要文字、水印、模糊、多余物品
```

要点：每个卖点都要在画面里找得到对应的东西；留白位置写死（上方 / 左侧）；品牌色写死色值或颜色名。
