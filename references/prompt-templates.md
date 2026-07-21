# 2+2Video prompt templates

Replace bracketed fields and remove unused lines. Keep the final video prompt direct and production-oriented.

## GPT Image 2 master character bible

Use the complete low-freedom template in [master-character-board.md](master-character-board.md). Fill every identity and style field, preserve its exact panel counts, and remove only sections explicitly marked optional.

## GPT Image 2 key-object asset prompt

```text
Create a professional object identity sheet for [OBJECT/PRODUCT] in [VISUAL STYLE]. Lock its [SHAPE, SCALE, MATERIAL, COLOR, MARKINGS, FASTENERS, INTERIOR]. Show front, side, back, top, three-quarter, open, closed, and detail views; include a neutral hand or scale marker only if necessary. Keep construction and proportions identical in every view. Neutral studio background, even light, no scene, no extra objects, no watermark.
```

## Seedance 2 ref2v — 15-second segment

```text
SUBJECTS
[Character A] @Image1 ([clarifier]): [appearance]; [movement quality]; [action specialty]; [role in this segment]
[Character B] @Image2 ([clarifier]): [appearance]; [movement quality]; [action specialty]; [role in this segment]
[Supporting character]: [silhouette, wardrobe, behavior, purpose]
[Key object] @Image3 ([clarifier, if referenced]): [locked construction and placement]

ENVIRONMENT
[Architecture, period, fixed furniture, paths, foreground/background, spatial restrictions]

STYLE
[Medium/rendering style]; [lighting]; [depth of field]; [texture]; real physical contact; stable spatial continuity; clear action feedback

CONTINUITY
Keep @Image1, @Image2, and @Image3 designs exact. Preserve wardrobe, faces, proportions, object construction, screen direction, spatial axis, lighting logic, and current damage state. [Cross-segment continuity handle if this is not the first segment.]

AUDIO RULE
No BGM, no music, no score, no melody, no song, no choir, no musical percussion. Generate only diegetic ambience and synchronized physical sound effects. No dialogue or narration unless explicitly requested.

TIMELINE
0:00-[T1]
[Shot size, lens feel, camera move]. [Exact action, reaction, geography, object position.]
SFX: [physical ambience and synchronized event]

[T1]-[T2]
[Shot size, lens feel, camera move]. [Next causal beat.]
SFX: [physical events only]

[Continue with contiguous beats.]

[END START]-0:15 — HARD-CUT END FRAME
[Exact shot size, lens feel, angle]. Camera locked. [Exact pose, gaze, expression, object position/orientation, foreground/background geometry, light state.] Resolve all motion and hold this exact readable composition for [0.3-0.7] seconds. End precisely on this frame. No fade, dissolve, morph, or camera drift.
SFX: [final physical sound] resolves into [diegetic room tone]

NEXT SEGMENT CUT HANDLE
HARD CUT IN to [different shot size/angle], preserving [subject / gaze / motion direction / object position / color / screen axis].
```

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
      "video_prompt": "SUBJECTS ... ENVIRONMENT ... STYLE ... CONTINUITY ... AUDIO RULE: NO BGM, SFX ONLY ... TIMELINE ... HARD-CUT END FRAME ..."
    }
  ]
}
```
