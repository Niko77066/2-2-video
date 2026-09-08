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
No BGM, no music, no score, no melody, no song, no choir, no musical percussion. Generate only diegetic ambience and synchronized physical sound effects. No dialogue or narration unless explicitly requested.

TIMELINE
0:00-[T1]
[Shot size, lens feel]. [Exact action, reaction, geography, object position.]
Camera: [one movement]. Light: [light state or change].
SFX: [physical ambience and synchronized event]

[T1]-[T2]
[Shot size, lens feel]. [Next causal beat.]
Camera: [one movement]. Light: [light state or change].
SFX: [physical events only]

[Continue with contiguous beats; five beats total for a 15-second segment.]

[END START]-0:15 — HARD-CUT END FRAME
[Exact shot size, lens feel, angle]. Camera locked. [Exact pose, gaze, expression, object position/orientation, foreground/background geometry, light state.] Resolve all motion and hold this exact readable composition for [0.3-0.7] seconds. End precisely on this frame. No fade, dissolve, morph, whip transition, generated transition, or camera drift.
SFX: [final physical sound] resolves into [diegetic room tone]

NEXT SEGMENT CUT HANDLE
HARD CUT IN to [different shot size/angle], preserving only [subject / gaze / motion direction / object position / color / screen axis].
```

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
| epic music swells, rhythmic score | there is no BGM by default | physical sounds from visible sources |
| the character feels nervous | the model cannot render stated emotion | a visible micro-behaviour: fake calm, hidden tremor, stiff smile |

## Hard-cut continuity table

```markdown
| Cut | Outgoing 15s end frame | Incoming shot | Shot change | Preserved visual handle | SFX out / in |
|---|---|---|---|---|---|
| S01 → S02 | [locked close-up of case latch] | [high wide of train aisle] | ECU → high wide | [same latch position and brass highlight] | [latch click → rail clatter] |
```

## SFX translation guide

Replace musical timing cues with physical ones:

| Remove | Use instead |
|---|---|
| low-frequency plucked strings | low train rumble, carriage resonance, restrained breathing |
| music begins accelerating | faster footsteps, cloth snaps, seat scrape, impact cadence |
| rapid jazz drums | rail-joint clatter, repeated wood impacts, shoe hits, breath |
| music suddenly cuts back | action sounds stop abruptly; train ambience remains |
| exaggerated choir burst | case latch, lid hinge, tiny object movement, short human reaction breath |

Do not merely rename music as `rhythmic ambience`. Keep every sound tied to a visible physical source.

## Minimal JSON plan

```json
{
  "project": {"title": "Example", "total_duration_seconds": 30, "ratio": "16:9"},
  "assets": {"characters": [{"id": "char-a", "name": "A", "image_prompt": "..."}]},
  "segments": [
    {
      "id": "S01",
      "duration_seconds": 15,
      "references": {"ref_images": ["char-a"]},
      "beats": [
        {"start": 0, "end": 12.5, "shot_size": "medium", "camera": "push-in", "action": "..."},
        {"start": 12.5, "end": 15, "shot_size": "close-up", "camera": "locked", "action": "..."}
      ],
      "end_anchor": {"start": 12.5, "end": 15, "shot_size": "close-up", "camera": "locked", "composition": "...", "subject_state": "...", "hold_seconds": 0.5},
      "next_opening": {"cut": "hard", "shot_size": "wide", "visual_link": "same object position"},
      "audio": {"bgm": false, "sfx_only": true, "events": [{"time": 4.2, "sound": "case latch"}]},
      "video_prompt": "A 15-second ... film ... SUBJECTS ... ENVIRONMENT ... STYLE ... CONTINUITY ... AUDIO RULE: NO BGM, SFX ONLY ... TIMELINE ... HARD-CUT END FRAME ..."
    }
  ]
}
```
