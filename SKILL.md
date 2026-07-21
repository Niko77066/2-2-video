---
name: 2-2-video
description: Turn a story or product idea into production-grade GPT Image 2 master character bibles and Seedance 2 reference-to-video prompts. Use for official-style character sheets, identity turnarounds, expression and detail boards, character-consistent AI shorts, product-placement stories, multi-part videos built from 15-second clips, timestamped action choreography, explicit hard-cut end frames, and SFX-only sound design with no BGM.
---

# 2+2Video

Build video prompts in two stages: generate and approve reusable character assets with GPT Image 2, then use those assets as numbered references in Seedance 2 ref2v prompts. Write every video segment as a self-contained 15-second block that ends on a precise still-readable frame and hard-cuts into a new shot size in the next block.

Read [references/prompt-templates.md](references/prompt-templates.md) before drafting prompts. Read [references/master-character-board.md](references/master-character-board.md) whenever creating or revising a character asset. Read [references/agent-escort-example.md](references/agent-escort-example.md) only when a worked action example is useful. Run `scripts/validate_plan.py` when a JSON production plan is requested.

## Output the production packet

Return these sections in order:

1. concise assumptions;
2. character and key-object asset plan;
3. one paste-ready GPT Image 2 prompt per asset;
4. the fixed Seedance reference map, such as `@Image1 = male agent`;
5. one paste-ready Seedance 2 prompt per 15-second segment;
6. a hard-cut continuity table between segments;
7. an SFX-only cue list.

Do not mention a video editor, API, product UI, or platform-specific tool unless the user asks for one. Do not generate paid assets when the user asks only for prompts.

## Lock the brief

Extract the total duration, aspect ratio, visual style, recurring characters, key object or product, environment, dialogue policy, and ending. Make low-risk assumptions explicit. Ask only when a missing choice would materially change the characters, ratio, or story.

Use full 15-second segments. If the requested duration is not a multiple of 15, ask whether to change the runtime or allow a shorter last segment.

## Create the GPT Image 2 master character bibles

Write one master character bible prompt per recurring main character. Keep characters separate so each receives a stable reference slot. Use a 4:3 horizontal production board with a clean white or off-white technical layout; apply the requested art style to the character renders, not to the board UI. Add a key-object sheet when the object must stay exact across shots. Supporting characters may remain text-defined unless they recur or must be visually identical.

Define each main character with immutable traits:

- age range, build, proportions, face, skin tone, hair silhouette;
- exact outfit construction, materials, palette, footwear, accessories;
- movement temperament and action specialty;
- explicit exclusions that prevent drift.

Make `MAIN IDENTITY + SCALE` the largest section. Demand front, three-quarter, side, and back full-body views; scale guides and silhouette thumbnails; an eight-expression progression; five micro-expressions; five head angles; a neutral baseline; posture variants; one cinematic close-up; four wardrobe/accessory callouts; five hand gestures; six to eight color swatches; and one isolated key prop only when relevant. Keep labels short and readable. See the master-board reference for exact counts and layout.

Keep the neutral turnaround free of handheld props and action poses. Use an optional hero illustration only as a small secondary art-direction insert; never let it displace the identity, face, hand, or material references needed by Seedance.

If one unified board makes faces, hands, labels, or details too small, split it after the first failed attempt into two matching 4:3 boards: `A — Identity / Scale / Palette` and `B — Performance / Details / Prop`. Preserve the exact same identity and style in both. Do not repeatedly reroll an overloaded single board.

Approve the assets before writing final video prompts when generation is part of the task. If an identity sheet drifts, repair the asset instead of bloating the video prompt.

## Fix the reference map

Assign reference numbers once and never reorder them across segments:

```text
@Image1 = [main character A asset]
@Image2 = [main character B asset]
@Image3 = [key object asset, if used]
```

Refer to each numbered image with a noun or clarification: `@Image1 (male agent)`, not a vague phrase such as `the reference above`.

## Write each Seedance 2 prompt

Use the author's compact production structure exactly:

```text
SUBJECTS
...

ENVIRONMENT
...

STYLE
...

CONTINUITY
...

AUDIO RULE
...

TIMELINE
0:00-...
...
```

### SUBJECTS

Describe every active character and key object. For referenced subjects, include the fixed reference number, appearance, movement quality, dramatic role, and action specialty. Distinguish supporting characters through silhouette, wardrobe, behavior, and purpose.

### ENVIRONMENT

Define architecture, entrances, fixed furniture, paths of movement, foreground/background layers, and spatial restrictions. State details that make action geography legible, such as one central aisle or one table between two benches.

### STYLE

State the rendering medium, lighting, depth of field, texture, physical-contact quality, spatial continuity, and action feedback. Keep it short enough that the timeline remains dominant.

### CONTINUITY

Lock wardrobe, faces, object design, screen direction, spatial axis, prop location, lighting logic, and damage state. Preserve these within and across segments.

### AUDIO RULE

Write this rule in every 15-second prompt:

```text
No BGM, no music, no score, no melody, no song, no choir, no musical percussion. Generate only diegetic ambience and synchronized physical sound effects. No dialogue or narration unless explicitly requested.
```

Do not use musical substitutes such as plucked strings, jazz drums, choir, rhythmic bed, tonal riser, or trailer hit. Translate pacing into physical sound: rail clatter, breath, cloth, footsteps, wood impact, metal latch, glass, wind, or room tone.

### TIMELINE

Write contiguous timestamps from `0:00` to `0:15`. Use 5-8 beats. Give each beat:

- one dominant framing;
- at most one camera move;
- precise subject action and reaction;
- spatial relation to the key object;
- a concrete `SFX:` line.

Use cuts inside the segment when the action needs a new view. Never stack contradictory camera movements in one beat.

## Control every 15-second boundary

Reserve the last 1.5-3 seconds for a `HARD-CUT END FRAME` beat. Specify:

- exact shot size, lens feel, and angle;
- camera locked or fully settled;
- character pose, gaze, and expression;
- key-object position and orientation;
- foreground/background geometry and light state;
- all motion resolved;
- final 0.3-0.7 seconds held on the exact composition;
- no fade, dissolve, morph, or camera drift.

The hard cut occurs between clips. Start the next segment with `HARD CUT IN` and immediately change shot size or angle while preserving one visual handle: the same subject, gaze line, direction of motion, object position, color accent, or screen axis.

Example boundary:

```text
S01 ends: locked extreme close-up of the brass latch centered in frame, hand exits, 0.5s hold.
S02 begins: HARD CUT IN to a high wide shot; the same latch remains on the same screen axis as the case is carried into the aisle.
```

Do not request a generative transition between segments. A stable outgoing frame plus a deliberate incoming composition creates the rhythm.

## Check before delivery

Verify that:

- the reference order never changes;
- each prompt contains `SUBJECTS`, `ENVIRONMENT`, `STYLE`, `CONTINUITY`, `AUDIO RULE`, and `TIMELINE`;
- every timeline covers exactly 15 seconds with no gaps or overlaps;
- every segment ends on a fully specified hard-cut frame at 15.0 seconds;
- every next segment opens at a different shot size or angle and preserves a named visual handle;
- every time block has concrete ambience or SFX;
- no prompt requests BGM, instruments, choir, melody, rhythmic score, or musical percussion;
- faces, wardrobe, bodies, props, lighting, spatial axis, and action causality remain stable.
