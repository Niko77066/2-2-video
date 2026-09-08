# 2+2Video prompt templates

Replace bracketed fields and remove unused lines. Keep the final prompts direct and production-oriented. The hard-cut boundary rules in this file override any softer ending, transition, or "smooth flow" language imported from other templates.

## Character design sheet — fill before any prompt

```text
Character [A] — [NAME]
- Species / form: [description]
- Age: [N]
- Appearance: [fur or hair color, build, silhouette, signature feature]
- Signature prop: [prop]
- Personality: [keywords, must contain a contrast]
- Action specialty: [what this character can physically do in an action beat]
- Micro-emotion: [fake calm / secretly scared / smug / guilty / stubborn]
- EN prompt keywords: [fixed English phrases reused in every image and video prompt]
```

Reuse `EN prompt keywords` verbatim in the character board and in every video prompt. Do not swap in synonyms between segments.

## GPT Image 2 cinematic character introduction board — default

Use for one or two recurring leads when the board doubles as a Seedance reference.

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

## GPT Image 2 master character bible — maximum consistency

Use the complete low-freedom template in [master-character-board.md](master-character-board.md) when a single character needs maximum lock-in, or when the shared board makes faces, hands, text, or materials too small. Fill every identity and style field, preserve its exact panel counts, and remove only sections explicitly marked optional.

## GPT Image 2 key-object asset prompt

```text
Create a professional object identity sheet for [OBJECT/PRODUCT] in [VISUAL STYLE]. Lock its [SHAPE, SCALE, MATERIAL, COLOR, MARKINGS, FASTENERS, INTERIOR]. Show front, side, back, top, three-quarter, open, closed, and detail views; include a neutral hand or scale marker only if necessary. Keep construction and proportions identical in every view. Neutral studio background, even light, no scene, no extra objects, no watermark.
```

## Seedance 2 ref2v — 15-second segment

```text
A 15-second [STYLE] animated short film. [ASPECT_RATIO]. [Color palette].

SUBJECTS
[Character A] @Image1 ([clarifier]): [appearance]; [movement quality]; [action specialty]; [role in this segment]
[Character B] @Image2 ([clarifier]): [appearance]; [movement quality]; [action specialty]; [role in this segment]
[Supporting character]: [silhouette, wardrobe, behavior, purpose]
[Key object] @Image3 ([clarifier, if referenced]): [locked construction and placement]

ENVIRONMENT
[Architecture, period, fixed furniture, paths, foreground/background, spatial restrictions]

STYLE
[Medium/rendering style]; [lighting]; [depth of field]; [texture]; soft volumetric lighting; cinematic camera work; expressive character animation; real physical contact; stable spatial continuity; temporal consistency; clear action feedback; no flickering; no identity drift; no wardrobe change; no prop redesign

CONTINUITY
Keep @Image1, @Image2, and @Image3 designs exact. Preserve wardrobe, faces, proportions, object construction, screen direction, spatial axis, lighting logic, and current damage state. [Cross-segment continuity handle if this is not the first segment.]

AUDIO RULE
No BGM, no music, no score, no melody, no song, no choir, no musical percussion: music is added in post, not generated here. Generate continuous diegetic ambience, synchronized visible-source SFX, and only the exact specified dialogue. @Audio1 = [exact current-segment dialogue slice, if present]. The matching character speaks the complete line from its @Audio reference exactly once with natural lip sync; preserve speaker identity, vocal age, accent, timbre, pitch, pace, articulation, emotion, microphone distance and room character. No paraphrase, repetition, truncation, extra dialogue, narration, lyrics, crowd words, extra speakers, or clipping. Leave headroom for the post-production music bed.
Music is never generated here: the BGM is added as a separate track after the hard-cut assembly.

TIMELINE
0:00-[T1]
[Shot size, lens feel]. [Exact action, reaction, geography, object position.]
Camera: [one movement]. Light: [light state or change].
Dialogue: [speaker + @AudioN + emotion] or none
Ambience: [space] | SFX: [visible-source event] | Mix: dialogue forward, headroom for post music

[T1]-[T2]
[Shot size, lens feel]. [Next causal beat.]
Camera: [one movement]. Light: [light state or change].
Dialogue: [line or none]
Ambience: [continuous] | SFX: [visible-source event] | Mix: no clipping

[Continue with contiguous beats; five beats total for a 15-second segment.]

[END START]-0:15 — HARD-CUT END FRAME
[Exact shot size, lens feel, angle]. Camera locked. [Exact pose, gaze, expression, object position/orientation, foreground/background geometry, light state.] Resolve all motion and hold this exact readable composition for [0.3-0.7] seconds. End precisely on this frame. No fade, dissolve, morph, whip transition, generated transition, or camera drift.
SFX: [final physical sound] resolves into [diegetic room tone]

NEXT SEGMENT CUT HANDLE
HARD CUT IN to [different shot size/angle], preserving only [subject / gaze / motion direction / object position / color / screen axis].
```

## Seedance 2.5 — native 30-second ten-shot clip

Do not stretch the 15-second five-beat template. A native 30-second clip has exactly ten shots, normally one new shot every 2.5-3.5 seconds. Every shot after SHOT 01 begins with an explicit hard cut to a different shot size or angle. Each shot contains one primary visible action and one direct visible consequence; split multi-step choreography across shots. The block names match the 15-second template so the same checklist and validator apply.

```text
A native 30-second [STYLE] animated short film generated with Seedance 2.5. [ASPECT_RATIO]. [Color palette].

SUBJECTS
[Character A] @Image1 ([clarifier]): [appearance]; [movement quality]; [action specialty]; [role in this clip]
[Character B] @Image2 ([clarifier]): [appearance]; [movement quality]; [action specialty]; [role in this clip]
[Key object] @Image3 ([clarifier, if referenced]): [locked construction and placement]

ENVIRONMENT
[Architecture, period, fixed furniture, paths, foreground/background, spatial restrictions]

STYLE
[Medium/rendering style]; [lighting]; [depth of field]; [texture]; cinematic lighting; brisk readable action; real physical contact; stable spatial continuity; temporal consistency; no flicker; no identity drift; no wardrobe change; no prop redesign

CONTINUITY
Keep @Image1, @Image2, and @Image3 designs exact. Preserve wardrobe, faces, proportions, object construction, screen direction, spatial axis, lighting logic, and current damage state. [Cross-clip continuity handle if another clip precedes this one.]

AUDIO RULE
No BGM, no music, no score, no melody, no song, no choir, no musical percussion: music is added in post, not generated here. Generate continuous diegetic ambience, synchronized visible-source SFX, and only the exact specified dialogue. @Audio1 = [exact current-segment dialogue slice, if present]. The matching character speaks the complete line from its @Audio reference exactly once with natural lip sync; preserve speaker identity, vocal age, accent, timbre, pitch, pace, articulation, emotion, microphone distance and room character. No paraphrase, repetition, truncation, extra dialogue, narration, lyrics, crowd words, extra speakers, or clipping. Leave headroom for the post-production music bed.
Music is never generated here: the BGM is added as a separate track after the hard-cut assembly.

SHOT-DENSITY LOCK
Exactly ten shots. Do not merge adjacent shots. SHOT 02-10 each begin with a visible HARD CUT IN
to a different shot size or camera angle. No continuous tracking shot may cover more than one shot block.
Each shot has one primary action and one immediate visible result across all of its prose, not only the
labeled Action line. Do not hide extra sequential actions in the scene description. Keep action brisk and
decisive at natural speed. Do not use slow motion. Do not use slow push-ins, gentle arcs, controlled orbits,
or smooth tracking in two adjacent action shots. No fade, dissolve, morph, whip transition, or generated transition.

TIMELINE
[0s-3s] SHOT 01 — HOOK
[Shot size]. [Immediate anomaly, danger, strong action, scale contrast, or absurd visual].
Camera: [one brisk movement]. Light: [light state].
Action: [one primary action] → Result: [one visible state change].
SFX: [visible-source sound].

[3s-6s] SHOT 02 — HARD CUT IN — GOAL / PURSUIT
[Different shot size or angle]. [Subject commits to the goal].
Camera: [one movement]. Light: [light state].
Action: [one action] → Result: [one visible consequence].
SFX: [visible-source sound].

[6s-9s] SHOT 03 — HARD CUT IN — OBSTACLE
[Different shot size or angle]. [One new obstacle appears before the reaction].
Camera: [one movement]. Action: [obstacle action] → Result: [clear threat state].
SFX: [visible-source sound].

[9s-12s] SHOT 04 — HARD CUT IN — IMMEDIATE RESPONSE
[Different shot size or angle]. [One decisive response].
Camera: [one movement]. Action: [response] → Result: [obstacle avoided, redirected, or worsened].
SFX: [impact, material, distance].

[12s-15s] SHOT 05 — HARD CUT IN — ESCALATION
[Different shot size or angle]. [One escalation that changes space, speed, ownership, or danger].
Camera: [one movement]. Action: [one action] → Result: [new state readable at 15s].
SFX: [visible-source sound].

[15s-18s] SHOT 06 — HARD CUT IN — MIDPOINT REVERSAL
[Different shot size or angle]. [A reveal or reversal contradicts the apparent goal].
Camera: [one movement]. Action: [one reveal action] → Result: [new objective or danger].
SFX: [visible-source sound].

[18s-21s] SHOT 07 — HARD CUT IN — NEW DANGER
[Different shot size or angle]. [The reversal produces one immediate danger].
Camera: [one movement]. Action: [one danger action] → Result: [specific spatial consequence].
SFX: [one precise sound chain].

[21s-24s] SHOT 08 — HARD CUT IN — CLIMAX ACTION
[Different shot size or angle]. [One decisive climax action].
Camera: [one energetic movement]. Action: [one action] → Result: [conflict physically resolves or tips].
SFX: [synchronized climax sound].

[24s-28s] SHOT 09 — HARD CUT IN — PAYOFF
[Different shot size or angle]. [One emotional or visual payoff; do not begin the final hold yet].
Camera: [one short settling movement that stops completely by 28s].
Action: [one payoff action] → Result: [exact final pose and prop state].
SFX: [final action sound completes before 28s].

[28s-30s] SHOT 10 — HARD CUT IN — HARD-CUT END FRAME
[Exact shot size, lens feel, angle, pose, gaze, expression, object position/orientation,
foreground/background geometry, and light state]. Camera locked. Resolve all motion.
Hold this exact readable composition for 0.3-0.7 seconds. End precisely on this frame.
No fade, dissolve, morph, whip transition, generated transition, or camera drift.
SFX: [final physical sound] resolves into [diegetic room tone].

FINAL ENDING
This is the final clip: end on SHOT 10. If another generated clip follows, replace this paragraph with
NEXT SEGMENT CUT HANDLE: HARD CUT IN to [different shot size or angle], preserving only [one visual handle].
```

Native-30s pacing invariants:

- Exactly 10 shots, not 5-7 long beats.
- New shot, new information, new danger, new joke, new visual change, or reversal at least every 3 seconds.
- SHOT 02-10 explicitly say `HARD CUT IN`; timestamps alone do not guarantee a cut.
- One primary action plus one direct visible consequence per shot.
- Count the whole shot description: a sequence such as jump → cross → land, or climb out → shake off → settle, must be split across shots even if the `Action:` line names only one step.
- No two adjacent action shots use slow, smooth, gentle, or controlled camera language.
- SHOT 09 resolves the action by 28s; SHOT 10 is a stable end frame, not a new action beat.

## Camera vocabulary

Use one concrete verb per beat:

`cinematic push in` / `whip pan` / `crash zoom` / `dramatic reveal` / `over-the-shoulder` /
`tracking shot` / `fast dolly` / `slow dolly out` / `scale contrast` / `extreme close-up` /
`wide cinematic shot` / `low-angle hero shot` / `overhead top-down` / `handheld follow` / `locked-off`

Rules:

- One primary camera move per beat; never chain two moves in one line.
- These describe motion inside a clip only. `match cut` and any other edit-level device belong in the hard-cut continuity table, not in a single prompt.
- The end-frame beat is always `locked-off`.
- Do not use `slow`, `smooth`, `gentle`, or `controlled` moves in two consecutive action beats.

## Banned prompt language

| Do not write | Why | Use instead |
|---|---|---|
| smooth transition / seamless transition to the next scene | the model invents a generated transition that cannot be cut | `HARD-CUT END FRAME` plus `NEXT SEGMENT CUT HANDLE` |
| fade out / dissolve / morph / whip transition | destroys the cut point and the reusable end composition | camera locked, motion resolved, 0.3-0.7s hold |
| slow build, calm establishing pan as the opening | wastes the first second | danger, anomaly, strong action, scale contrast, or absurd visual in the first second |
| epic music swells, rhythmic score | 音乐不由模型生成，写了只会让它自己垫一段每片不同的曲子 | 可见来源的物理声；BGM 在合成阶段作为单独音轨加入 |
| the character feels nervous | the model cannot render stated emotion | a visible micro-behaviour: fake calm, hidden tremor, stiff smile |

## Hard-cut continuity table

```markdown
| Cut | Outgoing 15s end frame | Incoming shot | Shot change | Preserved visual handle | SFX out / in |
|---|---|---|---|---|---|
| S01 → S02 | [locked close-up of case latch] | [high wide of train aisle] | ECU → high wide | [same latch position and brass highlight] | [latch click → rail clatter] |
```

## SFX translation guide

音效层永远只写可见来源，无论是否有 BGM。把抽象的音乐化节奏提示换成物理事件：

| Remove | Use instead |
|---|---|
| low-frequency plucked strings | low train rumble, carriage resonance, restrained breathing |
| music begins accelerating | faster footsteps, cloth snaps, seat scrape, impact cadence |
| rapid jazz drums | rail-joint clatter, repeated wood impacts, shoe hits, breath |
| music suddenly cuts back | action sounds stop abruptly; train ambience remains |
| exaggerated choir burst | case latch, lid hinge, tiny object movement, short human reaction breath |

Do not merely rename music as `rhythmic ambience`. Keep every sound tied to a visible physical source.

## Audio prompt guide

模型出对白 + 环境音 + 同步音效，**不出音乐**；BGM 在硬切合成后作为单独音轨加入。完整流程见 [audio-production.md](audio-production.md)。

| Avoid | Use instead |
|---|---|
| exciting music | fixed 86 BPM marimba motif, rising two-note phrase, low under dialogue |
| same voice as before | exact current-segment @AudioN slice from the character's single project master |
| dramatic sound effects | named visible-source impacts with material, distance and timing |
| music suddenly changes | same motif with thinner/thicker orchestration and an explicit energy change |
| dialogue over loud score | dialogue forward; BGM ducked at least 8-12 dB during speech |

BGM 身份跨片不变。每个音效都要有可见或空间上说得通的来源。没有对白的 beat 写 `Dialogue: none`。

## Minimal JSON plan

`scripts/validate_plan.py` checks this shape: one shot per `ceil(duration / 3)` (5 for 15s, 10 for 30s), contiguous beats, a locked end anchor in the final 3 seconds, a hard-cut handle between segments, the six prompt sections, and the audio rules: no model-generated music, dialogue lines pointing at their own slices.

```json
{
  "project": {"title": "Example", "total_duration_seconds": 15, "ratio": "16:9", "music": {"identity": "86 BPM marimba motif, rising two-note phrase", "added_in": "assembly"}},
  "assets": {"characters": [{"id": "char-a", "name": "A", "image_prompt": "..."}]},
  "segments": [
    {
      "id": "S01",
      "duration_seconds": 15,
      "references": {"ref_images": ["char-a"]},
      "beats": [
        {"start": 0, "end": 3, "shot_size": "wide", "camera": "crash zoom", "action": "..."},
        {"start": 3, "end": 6, "shot_size": "medium", "camera": "whip pan", "action": "..."},
        {"start": 6, "end": 10, "shot_size": "close-up", "camera": "scale contrast", "action": "..."},
        {"start": 10, "end": 12.5, "shot_size": "medium wide", "camera": "fast dolly", "action": "..."},
        {"start": 12.5, "end": 15, "shot_size": "extreme close-up", "camera": "locked", "action": "..."}
      ],
      "end_anchor": {"start": 12.5, "end": 15, "shot_size": "extreme close-up", "camera": "locked", "composition": "...", "subject_state": "...", "hold_seconds": 0.5},
      "next_opening": {"cut": "hard", "shot_size": "high wide", "visual_link": "same object position"},
      "audio": {"bgm": false, "dialogue": [{"character": "char-a", "audio_ref": "audio/S01_char-a.wav", "time": 6.0}], "events": [{"time": 4.2, "sound": "case latch"}]},
      "video_prompt": "A 15-second ... film ... SUBJECTS ... ENVIRONMENT ... STYLE ... CONTINUITY ... AUDIO RULE: NO BGM, no music, music added in post; Dialogue: char-a @Audio1 ... TIMELINE ... HARD-CUT END FRAME ..."
    }
  ]
}
```

每个片段的 `audio.bgm` 必须是 `false`，`video_prompt` 必须显式禁止音乐；BGM 身份写在 `project.music` 里，在合成阶段作为单独音轨加入。

A 30-second Seedance 2.5 clip uses `"duration_seconds": 30`, ten beats, an end anchor at `28 → 30`, and a prompt whose SHOT 02-10 each say `HARD CUT IN`.
