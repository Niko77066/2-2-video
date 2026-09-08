---
name: 2-2-video
description: Use when turning a story, product idea, or character concept into GPT Image 2 reference assets and multiple Seedance 2 video clips assembled with deliberate hard cuts. Covers character design, cinematic character/key-object boards, 15-second clip prompts, timestamped action, cross-clip continuity, local hard-cut assembly, and correct Seedance 2 API payloads with metadata.duration.
---

# 2+2Video

把一个故事拆成可控的视觉资产和多个 15 秒视频片段：先用 Image2 / GPT Image 2 固定角色与关键道具，再用 Seedance2 为每个片段生成独立 prompt，最后通过“锁定结束帧 → 下一段改变景别/角度 → 保留视觉接点”的方式硬切成片。

本 skill 负责视觉资产、Prompt、片段规划、Seedance2 调用和硬切合成。默认可以用本地文件，也可以按任务需要使用 CDN 或外部资产；不要把某一种资产存储方式硬编码成必选步骤。

Prompt 写法采用电影级写法：角色板按 AAA / Netflix 设计板标准写，视频 Prompt 以“片头声明 + 锁定块 + 逐时间码分镜”组织。片段边界仍然由本 skill 的硬切规则决定，任何外部模板里的柔性结尾、生成式转场或“平滑过渡”写法都被下文的硬切规则覆盖。

读取规则：

- 创建或修改角色资产时，读取 [references/master-character-board.md](references/master-character-board.md)。
- 需要完整 Prompt 模板时，读取 [references/prompt-templates.md](references/prompt-templates.md)。

## 输出生产包

按以下顺序输出：

1. 简短假设：总时长、比例、风格、对白规则、结尾。
2. 故事和片段拆分：每段 15 秒，说明段落功能与硬切点。
3. 角色、关键道具和场景资产计划。
4. 每个资产一条可直接用于 Image2 的 Prompt。
5. 固定的 Seedance2 参考图映射，例如 `@Image1 = 主角 A`。
6. 每个 15 秒片段一条可直接用于 Seedance2 的视频 Prompt。
7. 片段之间的硬切连续性表。
8. 本地片段文件命名和硬切合成方式。
9. 用户要求执行 Seedance2 或生成 API payload 时，附上完整请求体和关键校验。
10. 检查结果。

用户只要 Prompt 时，不执行生图或生视频；用户要求实际生成时，使用 Codex 内置 `image_gen` 生成 Image2 资产，并按当前可用的 Seedance2 生成方式处理本地片段。

## 1. 锁定故事简报

提取并锁定：总时长、画幅、视觉风格、重复出现的角色、关键道具、环境、对白规则、声音规则、结尾动作。

- 默认总时长是 15 秒的整数倍，每段完整 15 秒。
- 不是 15 秒整数倍时，优先询问是否调整总时长；不要悄悄生成一个过短的末段。
- 15 秒内使用 5 个递进镜头：建立/钩子 → 冲突 → 升级 → 爆发 → 结尾定格。
- 第 1 秒必须有危险、异常、强动作、巨大尺度反差或荒谬视觉钩子。
- 每 3 秒至少出现一次新信息、新危险、新笑点、新视觉变化或反转。
- 节奏是：发现 → 升级 → 更离谱 → 爆发 → 安静余韵。故事必须越来越失控，不能一个镜头讲完。
- 视觉动作优先于解释性对白；让动作、表情、空间、光影和声音承担叙事。
- 角色要有强轮廓、性格反差、微情绪和明确的行动特长。

### 角色设计

角色是后面所有 Prompt 的地基，先设计角色再写画面。

**强视觉轮廓（一眼认出）**：必须有标志性外形，发挥想象，例如但不限于巨大眼镜、超长围巾、圆滚滚身体、发光背包、不对称造型、巨大工具、奇怪比例。禁止普通人、无特征角色。

**性格反差**：胆小却爱装勇敢 / 暴躁但爱哭 / 冷静却总倒霉 / 超乐观但总闯祸。禁止“普通善良角色”。

**角色关系火花（多角色时）**：性格必须冲突，自然产生喜剧或张力，例如一个冲动一个冷静、一个相信奇迹一个极度现实。

**微情绪**：角色要有细微真实反应，假装冷静、偷偷害怕、小得意、心虚、嘴硬；用画面表现，不要直接说出情绪。

角色设计输出格式：

```text
Character A — [名字]
- 物种/形象: [描述]
- 年龄: [N 岁]
- 外貌: [毛色/发色/体型/标志性特征]
- 标志性道具: [道具]
- 性格: [关键词，含反差]
- 行动特长: [在动作段里能做什么]
- Prompt 关键词(EN): [用于 Image2 与 Seedance2 的固定英文短语]
```

同一角色的 `Prompt 关键词(EN)` 一旦确定，必须原样复用到角色板 Prompt 和每一条视频 Prompt，不要换同义词。

### 世界观与视觉记忆点

- 一个简单但迷人的设定，只露冰山一角，不做解释：云朵会吃人 / 重力每天变化 / 电梯通往不同宇宙 / 每个人的情绪会变成天气。
- 至少一个视觉记忆点：星空裂开、海浪倒流、巨型月亮压下来、房间无限折叠、小角色面对巨大机械、城市漂浮起来。视觉记忆点要落在具体某个时间块里，并写进对应片段的 Prompt。

### 镜头语言库

写 `Camera:` 字段时优先使用具体动词：

`cinematic push in` / `whip pan` / `crash zoom` / `dramatic reveal` / `over-the-shoulder` /
`tracking shot` / `fast dolly` / `slow dolly out` / `scale contrast` / `extreme close-up` /
`wide cinematic shot` / `low-angle hero shot` / `overhead top-down` / `handheld follow` / `locked-off`

约束：

- 每个 beat 最多一个主要运镜，不要在一行里连写两个运镜。
- 这些词只描述片段内部的镜头运动；`match cut` 这类剪辑手法只能在硬切连续性表里规划，不写进单条 Prompt。
- 结束帧所在时间块只能是 `locked-off`。

### 严格禁止

- 平淡剧情、无冲突、低幼搞笑、“两个角色站着聊天”。
- 空洞对白、世界观解释过多。
- 镜头不变化、无情绪变化、无视觉高潮。
- 流水线短视频感、AI 感随机拼接。
- 在 Prompt 里要求 fade、dissolve、morph 或任何生成式转场；片段之间只由剪辑硬切。

故事草案使用：

```text
Title: [片名]
Core Idea: [一句话]
World Setting: [一到两句]
Emotional Hook: [情绪钩子]
Visual Hook: [视觉记忆点]

[0s-3s] Scene / Action / Camera / Sound
[3s-6s] Scene / Action / Camera / Sound
[6s-10s] Scene / Action / Camera / Sound
[10s-13s] Scene / Action / Camera / Sound
[13s-15s] Scene / Action / Camera / Sound / Ending Payoff
```

## 2. 用 Image2 固定视觉资产

### 角色资产原则

每个重复出现的主角单独占一个固定参考位。角色板必须锁定：年龄和体型、脸部几何、发型轮廓、服装层次、材质、配色、配饰、动作气质、行动特长和明确的排除项。

默认使用下面的 16:9 电影项目角色介绍板；双主角可以同板。用作视频参考时，脸、全身轮廓和服装层次必须足够大。如果需要最大化单角色一致性，或同板导致脸、手、文字、材质过小，切换成 [references/master-character-board.md](references/master-character-board.md) 的 4:3 单角色技术板，必要时拆成两张同风格板，不要反复重抽一张过载的板。

### 角色介绍板 Prompt

当需要一张双角色介绍板或电影项目角色板时，使用以下模板；将方括号内容替换为具体信息：

```text
[LEFT SIDE] Character A — [NAME]
[Full appearance], [costume], [dynamic pose], [animation style],
cinematic soft studio lighting, rim light, rich material detail.

[RIGHT SIDE] Character B — [NAME]
[Full appearance], [costume], [dynamic pose], [same animation style],
matching lighting and material quality.

LAYOUT
- 16:9 horizontal composition.
- Left half: Character A name label, role, and key traits including Age / Height / Personality.
- Right half: Character B name label, role, and key traits including Age / Height / Personality.
- Center: subtle divider with project title "[TITLE]".
- Each side may vary slightly but must stay symmetrical in weight: one large full-body hero
  illustration, one small front/side/back turnaround in a bottom corner, and 3-5 detail crop
  panels for head, accessory, footwear, clothing construction, hands, or signature materials.
- All text in English with editorial typography, clean visual hierarchy, and large readable labels.
- Keep faces, hands, clothing layers, accessories, and materials large enough to inspect.

VISUAL STYLE
- AAA game character sheet / Netflix animation design board quality.
- Masterpiece, ultra detailed, ArtStation-featured concept-art finish.
- Editorial typography, clean visual hierarchy, premium presentation.
- Cinematic editorial color system: soft layered gradients, elegant low-saturation tones,
  subtle premium accent colors, and a harmonious palette derived from character personality
  and world setting.
- Background: soft warm ivory / mist gray / pale beige / fog blue / muted cream /
  atmospheric gradient / cinematic neutral tones; automatically choose the best fit.
- Accent colors derive from character costume, personality, and emotional tone.
- Overall feel: cinematic, cohesive, breathable, elegant, modern, soft premium contrast.
- Both characters use the same rendering style, lighting direction, palette logic,
  and material quality.
- AVOID: oversaturated colors, neon cyberpunk palette, harsh contrast, cheap infographic
  colors, noisy rainbow palettes, cluttered layout, tiny unreadable text, logos, watermarks.
```

直接调用 Codex 的 `image_gen` 生成；不要用 PIL、Canvas 或 HTML 伪造生图。保存到本地任务目录并保留原始生成图，例如：

```text
<task>/assets/character_a_master.png
<task>/assets/character_b_master.png
<task>/assets/key_object.png
```

### 关键道具 Prompt

需要跨镜头保持形状、材质或标记一致的物体，单独生成资产：

```text
Create a professional object identity sheet for [OBJECT] in [VISUAL STYLE].
Lock its shape, scale, material, color, markings, fasteners, interior, and damage state.
Show front, side, back, top, three-quarter, open, closed, and detail views.
Keep construction and proportions identical in every view.
Neutral studio background, even light, no scene, no extra objects, no watermark.
```

### 参考图映射

一旦分配就不要跨片段重排：

```text
@Image1 = [主角 A 的 master board]
@Image2 = [主角 B 的 master board]
@Image3 = [关键道具板，可选]
@Image4 = [环境板，可选]
```

在视频 Prompt 中总是写成 `@Image1 (主角 A)`，不要写“上面的参考图”这类模糊指代。

## 3. 为每个片段写 Seedance2 Prompt

每段必须是自洽的 15 秒视频 Prompt。不要把一条 45 秒故事塞进一条 Prompt；拆成 `S01`、`S02`、`S03`……，每段都重新声明片头、主体和连续性。

视频 Prompt 固定使用以下结构：

```text
A 15-second [STYLE] animated short film. [ASPECT_RATIO]. [Color palette].

SUBJECTS
[Character A] @Image1 ([clarifier]): [appearance], [movement quality], [action specialty], [role]
[Character B] @Image2 ([clarifier]): [appearance], [movement quality], [action specialty], [role]
[Key object] @Image3 ([clarifier]): [locked construction and current placement]
[Supporting character]: [silhouette, wardrobe, behavior, purpose]

ENVIRONMENT
[Architecture, fixed furniture, entrances, paths, foreground/background layers, spatial restrictions]

STYLE
[Rendering style]. [Lighting]. [Depth of field]. [Texture]. Soft volumetric lighting,
cinematic camera work, expressive character animation, real physical contact,
stable spatial continuity, temporal consistency, smooth motion, clear action feedback,
no flickering, no identity drift, no wardrobe change, no prop redesign.

CONTINUITY
Keep all referenced designs exact. Preserve faces, hair, wardrobe layers, proportions,
object construction, screen direction, spatial axis, lighting logic, and current damage state.
[Cross-segment visual handle].

AUDIO RULE
No BGM, no music, no score, no melody, no song, no choir, no musical percussion.
Generate only diegetic ambience and synchronized physical sound effects.
No dialogue or narration unless explicitly requested.

TIMELINE
0:00-0:03 [Shot size]. [Scene]. [Character] [exact visible action].
  Camera: [one movement]. Light: [light state or change]. SFX: [physical sound].
0:03-0:06 [Shot size]. [Causal escalation and reaction].
  Camera: [one movement]. Light: [light state or change]. SFX: [physical sound].
0:06-0:10 [Shot size]. [Reversal or visual escalation, including the visual hook if it lands here].
  Camera: [one movement]. Light: [light state or change]. SFX: [physical sound].
0:10-0:12.5 [Shot size]. [Climax action; the action fully resolves before the end-frame hold].
  Camera: [one movement that settles completely by 0:12.5]. SFX: [physical sound].
0:12.5-0:15 HARD-CUT END FRAME
[exact shot size, lens feel, angle, pose, gaze, expression, object position,
foreground/background geometry, and light state]. Camera locked. Resolve all motion.
Hold the exact readable composition for 0.3-0.7 seconds. End precisely on this frame.
No fade, dissolve, morph, whip transition, generated transition, or camera drift.
SFX: [final physical sound] resolves into room tone.

NEXT SEGMENT CUT HANDLE
HARD CUT IN to [different shot size or angle], preserving only [one visual handle:
same subject / gaze / motion direction / object position / color highlight / screen axis].
```

Prompt 要求：

- 片头一行先声明时长、风格和画幅，让模型在第一句就锁定成片形态。
- 每个时间轴覆盖精确的 `0:00` 到 `0:15`，无空档、无重叠。
- 每个 beat 只有一个主景别、最多一个主要运镜、一个主动作和一个直接结果；出现“起跳 → 越过缺口 → 落地”这类连续三步时，拆成两个景别。
- `Camera:` 使用镜头语言库里的具体动词；连续两个 beat 不要都写 `slow`、`smooth`、`gentle`、`controlled` 这类舒缓运镜，动作段尤其不行。
- 每个 beat 写清光线状态，让光影参与叙事，而不是只描述动作。
- 把“节奏”翻译成可见动作和物理声音，不写音乐代用品。
- 默认无 BGM、无配乐；如用户明确要对白，只在对应时间点写对白及其反应。
- 不写“生成平滑转场”；片段之间必须由剪辑硬切。
- `0:12.5-0:15` 不是新的动作段，而是高潮动作解决后的稳定出点。
- 除最后一段外，每条 Prompt 都要写出 `NEXT SEGMENT CUT HANDLE`；最后一段改写成明确的最终结束构图。

## 4. 片段边界：硬切而不是生成转场

每段最后 1.5-3 秒预留为 `HARD-CUT END FRAME`：

- 镜头完全锁定，或在结束前完全稳定。
- 明确景别、角度、镜头感、角色姿态、视线、表情、道具位置和光线。
- 所有动作在最后一帧前解决；最后 0.3-0.7 秒保持可读构图。
- 禁止 fade、dissolve、morph、whip-transition 或生成式转场。

下一段必须以 `HARD CUT IN` 开始，并立即改变景别或角度，同时保留一个视觉接点：同一主体、视线、运动方向、道具位置、色彩高光或屏幕轴线。

示例：

```text
S01 ends: locked extreme close-up of the brass latch centered in frame,
the hand exits, the latch clicks, 0.5s hold.
S02 begins: HARD CUT IN to a high wide shot of the aisle;
the same brass latch remains on the same screen axis as the case enters frame.
```

连续性表：

| Cut | 片段结束帧 | 下一段开场 | 景别变化 | 保留接点 | 声音衔接 |
|---|---|---|---|---|---|
| S01 → S02 | 锁定道具特写 | 高位远景硬切 | ECU → Wide | 同一道具位置/高光 | 咔嗒声 → 环境声 |

## 5. 本地片段合成

片段生成后只保留本地文件。建议命名：

```text
<task>/clips/S01.mp4
<task>/clips/S02.mp4
<task>/clips/S03.mp4
<task>/hard-cut-list.txt
<task>/final_hard_cut.mp4
```

`hard-cut-list.txt`：

```text
file 'clips/S01.mp4'
file 'clips/S02.mp4'
file 'clips/S03.mp4'
```

当所有片段编码参数一致时，直接拼接，不添加转场：

```bash
ffmpeg -y -f concat -safe 0 -i hard-cut-list.txt -c copy final_hard_cut.mp4
```

如果编码参数不一致，使用统一参数重新编码后拼接；仍然不加入过渡：

```bash
ffmpeg -y -f concat -safe 0 -i hard-cut-list.txt \
  -c:v libx264 -crf 18 -pix_fmt yuv420p -c:a aac final_hard_cut.mp4
```

合成后用 `ffprobe` 检查总时长、分辨率、音轨和片段边界；不要把“生成模型返回成功”当作剪辑完成。

## 6. 调用 Seedance2 API

仅当用户要求实际调用 Seedance2、生成 API payload 或排查任务时使用本节。只要输出 Prompt，不要额外加入 API 请求体。

对于 `POST /v1/videos`，使用模型 `doubao-seedance-2-0-260128`，并把 `duration` 放在 `metadata` 内。禁止把 `duration` 放在请求根级别：网关可能忽略根级别的值并生成默认时长的片段，同时仍返回成功。

完整请求体：

```json
{
  "model": "doubao-seedance-2-0-260128",
  "prompt": "<完整的 Seedance2 15 秒片段 Prompt>",
  "metadata": {
    "content": [],
    "resolution": "1080p",
    "ratio": "16:9",
    "generate_audio": false,
    "duration": 15
  }
}
```

参数规则：

- `metadata.duration` 必须是整数，范围为 `4` 到 `15`；对于本 skill 的标准片段，使用 `15`。
- `metadata.ratio` 使用 `16:9`、`9:16` 或用户指定的支持比例。
- `metadata.resolution` 使用 `480p`、`720p` 或 `1080p`，按任务要求选择。
- `metadata.generate_audio` 默认 `false`，因为 Prompt 默认要求无 BGM、只保留物理环境声和 SFX；用户需要生成音频时才改为 `true`。
- 参考图编号仍然写入视频 Prompt 的 `@Image1`、`@Image2` 等映射；不要在不同片段间重排。

提交示例：

```python
import requests

payload = {
    "model": "doubao-seedance-2-0-260128",
    "prompt": video_prompt,
    "metadata": {
        "content": [],
        "resolution": "1080p",
        "ratio": "16:9",
        "generate_audio": False,
        "duration": 15,
    },
}

resp = requests.post(
    f"{base_url}/v1/videos",
    headers={
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json",
    },
    json=payload,
    timeout=60,
)
resp.raise_for_status()
task_id = resp.json().get("id") or resp.json().get("task_id")
```

任务完成后立即下载返回的 `metadata.url` 或供应商等价视频 URL，并用 `ffprobe` 测量实际时长；不要相信任务响应中的预计时长字段，也不要因为接口返回成功就跳过片段边界检查。

如果用户要求使用 CDN 或外部参考资产，先确保 URL 对 Seedance2 可访问，再把它作为任务需要的参考资产使用；CDN 不是本 skill 的固定前置步骤。

## 7. 交付前检查

- [ ] 角色有强视觉轮廓、性格反差和行动特长，`Prompt 关键词(EN)` 在所有资产和片段里一致。
- [ ] 角色、道具和环境资产已经用 Image2 固定，参考编号在所有片段中不变。
- [ ] 角色板脸、手、服装层次和文字足够大可读；否则已改用单角色技术板。
- [ ] 每个视频片段是完整 15 秒，Prompt 含片头声明和 `SUBJECTS`、`ENVIRONMENT`、`STYLE`、`CONTINUITY`、`AUDIO RULE`、`TIMELINE`。
- [ ] 每段时间轴精确覆盖 15 秒，且最后 1.5-3 秒是锁定的硬切结束帧。
- [ ] 每个 beat 只有一个主景别、一个主要运镜和一个主动作，`Camera:` 用的是具体镜头动词。
- [ ] 视觉记忆点落在具体时间块里，并写进了对应片段的 Prompt。
- [ ] 下一段以不同景别或角度硬切进入，并明确保留一个视觉接点。
- [ ] 没有 fade、dissolve、morph 或生成式转场要求。
- [ ] 默认无 BGM；每个时间块都有可见来源对应的环境声或 SFX。
- [ ] 脸、发型、服装层次、比例、道具结构、光线、屏幕方向和动作因果保持连续。
- [ ] 本地片段已按顺序合成，输出文件可用 `ffprobe` 读取。
- [ ] 如果生成 API payload，`duration` 位于 `metadata.duration`，不在请求根级别。
