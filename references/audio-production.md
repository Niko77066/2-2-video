# 原生 BGM、对白与跨片音色一致性

本 skill 的默认声音策略是：无 BGM、无对白，只有可见来源的环境声和同步音效——片段当作可剪辑素材交付，配乐留给后期。

只有当用户要求原生 BGM、出镜对白或旁白时才启用本份流程。启用后，视频 Prompt 的 `AUDIO RULE` 块换成下面的 `AUDIO LOCK` 版本，`metadata.generate_audio` 改为 `true`。

## 1. 先锁定声音圣经

生成视频前冻结：

- BGM：曲风、速度、调性气质、主奏乐器、核心动机、情绪弧线和片尾处理。
- 环境：场所底噪、天气、远近层次、混响和跨切点连续底声。
- 每个角色：固定 ID、性别表达、年龄段、口音、音色、音高、语速、咬字、气息、情绪基线、拾音距离和空间感。
- 混音：对白优先；对白时 BGM 避让；关键音效清楚但不遮蔽台词；禁止削波。

每条 Prompt 原样复用声音圣经里的关键字段，不对音色和 BGM 身份做同义改写——这与角色的 `Prompt 关键词(EN)` 是同一种锁。

## 2. 音色一致性：一次母带，逐段切片

不要让 TTS 按同一段文字描述逐句独立生成。实测中，相同角色描述的独立调用存在明显声纹漂移。

对每个重复角色执行：

1. 用 SeedAudio 1.0 **一次生成该角色在整个项目中的全部干声台词**，句间留明确静音。
2. 母带只出现该角色，不混 BGM、环境音、音效或其他说话人；输出 48kHz WAV/MP3。
3. 用静音检测或强制对齐，切成每个视频片段实际需要的精确台词文件。
4. 每个切片跑 ASR；台词不完整、顺序错误或多出内容时先修音频，不进入付费视频生成。
5. 固定命名：`audio/voice_<character_id>_master.*` 与 `audio/<segment>_<character_id>.*`。

关键区别：`reference_audio` 不只是抽象音色，它同时携带**要说的内容**。后续片段不能反复传第一段台词当“音色样本”再要求模型说另一句；每段必须传当前段要说的精确切片。

实测依据（2026-08-05，同一项目内的相对比较）：相同音色描述分别调用 SeedAudio，同角色声纹均值约 `0.489`；一次生成完整角色母带再切片后，同角色片段均值约 `0.697`；一条 Seedance2 `reference_audio` 成片与其输入台词切片相似度约 `0.814`，ASR 逐字正确。同批四次并发探索里只有一条在等待窗口内完成，因此还没有拿到同角色两条成片的直接跨片对照。该结果支持“母带一次生成 → 精确切片 → 每段作为 reference_audio”的保守流程，但不构成对未来任务的保证，仍要逐片验收。

## 3. 声音路由

### 出镜角色对白

- `metadata.generate_audio = true`，`content` 里加当前片段的精确台词切片，`role: reference_audio`。
- Prompt 写 `the character from @Image1 speaks the complete line from @Audio1 exactly once`，并要求保留声纹、口音、音高、语速、情绪和拾音距离，做自然口型同步。
- 不在 Prompt 里另写一套可能冲突的替代台词；中文文本只用于核对，`@AudioN` 是唯一声音真值。

### 画外音或旁白

人物不该对口型时，不要把旁白作为 `reference_audio` 传进去，否则模型可能让画面里的人开口。让模型只生成 BGM、环境音和音效，旁白用同一条完整 TTS 母带在合成阶段混入。

### 无对白片段

`content` 不带音频，`generate_audio = true`，明确要求 BGM、环境音和同步音效，并写 `Dialogue: none; no speech, narration, lyrics or crowd words`。

### 一致性回退

原生出镜对白连续漂移时：

1. 保留失败片段和任务 ID，不静默重提。
2. 改为只生成 BGM、环境音和音效，强制画面人物无声。
3. 把已验收的母带切片在后期混入；需要口型时重做该镜头或改成画外音构图。

## 4. AUDIO LOCK 块

原生声音项目里，用它替换视频 Prompt 的 `AUDIO RULE` 块：

```text
AUDIO RULE / AUDIO LOCK
Generate the complete native soundtrack: [immutable BGM identity, BPM, motif, instrumentation],
[continuous diegetic ambience], [synchronized visible-source SFX], and only the exact specified dialogue.
@Audio1 = [exact current-segment dialogue slice for Character A, if present]
@Audio2 = [exact current-segment dialogue slice for Character B, if present]
The matching character speaks the complete line from its @Audio reference exactly once with natural lip sync.
Preserve the reference speaker identity, vocal age, accent, timbre, pitch, pace, articulation,
emotion, microphone distance and room character. Duck BGM under speech.
No paraphrase, repetition, truncation, extra dialogue, narration, lyrics, crowd words,
extra speakers, or clipping.
```

块名保留 `AUDIO RULE`，让 `scripts/validate_plan.py` 的小节检查继续通过。

每个时间块分别写：

```text
BGM: [固定动机/乐器/能量/与上一段的承接]
Dialogue: [角色 + @AudioN + 情绪 + 时间窗]，或 none
Ambience: [场所底声、天气、空间和连续性]
SFX: [可见来源、同步点、远近和材质]
Mix: dialogue forward; duck BGM under speech; no clipping
```

## 5. BGM 与切点

所有片段复用一份不可变的音乐身份：同一 BPM 区间、主奏乐器、核心动机、调性气质和动态范围。每段只改变能量与编配，不重新定义曲风。

画面继续硬切，不生成视觉转场。声音接点优先保留同一 BGM 动机或环境底噪，让短促物理音效在切点前完成；只允许为消除爆音做极短技术性交叉，不做创意淡入淡出。

## 6. 验收

不要把 API 成功当作声音成功。逐段检查：

- ASR：台词逐字完整，角色、顺序和时间窗正确，无额外人声。
- 声纹：比较输入切片与输出对白窗口，并比较同角色跨片结果；数值只作相对证据，人工试听是最终门。
- 口型：开口与参考台词同步，没有无声口型或旁白被错绑到角色。
- 音乐：BGM 身份、速度气质和乐器编制连续，没有无因换曲。
- 音效：可见动作有同步音效，环境底声符合空间，没有无来源巨响。
- 混音：对白清晰，BGM 已避让，峰值不削波；切点没有爆音或突兀静音。
