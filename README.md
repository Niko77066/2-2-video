# 2+2Video

`2-2-video` is a Codex skill for turning a story or product idea into a production-ready AI video packet. It designs the characters first, then creates reusable GPT Image 2 character boards, stable Seedance 2 reference maps, linked 15-second ref2v prompts, hard-cut continuity plans, and SFX-only sound direction.

## What it provides

- Character design sheets with strong silhouettes, contrast personalities, and fixed English prompt keywords
- Cinematic 16:9 character introduction boards, plus a low-freedom master board for maximum single-character consistency
- Key-object production boards
- Fixed reference numbering across every video segment
- Self-contained Seedance 2 prompts with a film header, locked reference block, and per-beat camera and light direction — five shots for a 15-second clip, ten for a native 30-second Seedance 2.5 clip
- Explicit hard-cut end frames and continuity handles
- Diegetic ambience and synchronized SFX without BGM by default, plus an opt-in native BGM/dialogue pipeline with single-master voice slicing
- Correct Seedance 2 / 2.5 API payloads, reference-media wiring, and paid-task discipline
- A Python validator for machine-readable production plans

## Install

Copy this repository into your Codex skills directory:

```bash
git clone https://github.com/Niko77066/2-2-video.git ~/.codex/skills/2-2-video
```

Restart Codex after installation so the skill is discovered.

## Use

Invoke the skill by name and provide a story or product brief:

```text
Use $2-2-video to turn this idea into a 60-second, 16:9 cinematic short with no dialogue and no BGM: ...
```

The skill returns assumptions, an asset plan, GPT Image 2 prompts, a fixed Seedance reference map, one prompt per 15-second segment, a hard-cut continuity table, and an SFX cue list.

## Validate a production plan

When working with a JSON production plan, run:

```bash
python3 scripts/validate_plan.py path/to/plan.json
```

The validator checks segment timing (15s or native 30s), the `ceil(duration / 3)` shot count, reference anchors, end-frame requirements, hard-cut continuity, required prompt sections, and the audio rules for the declared `audio_mode` (`sfx_only` by default, `native` for BGM and on-camera dialogue).

## Repository layout

```text
2-2-video/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── agent-escort-example.md
│   ├── audio-production.md
│   ├── master-character-board.md
│   ├── prompt-templates.md
│   └── seedance-api.md
└── scripts/
    └── validate_plan.py
```

## License

No license has been granted yet. The repository is public for viewing and use subject to applicable copyright law; add an explicit open-source license if you want to permit redistribution and modification under defined terms.
