# 2+2Video

`2-2-video` is a Codex skill for turning a story or product idea into a production-ready AI video packet. It creates reusable GPT Image 2 character bibles, stable Seedance 2 reference maps, linked 15-second ref2v prompts, hard-cut continuity plans, and SFX-only sound direction.

## What it provides

- Master character and key-object production boards
- Fixed reference numbering across every video segment
- Self-contained 15-second Seedance 2 prompts
- Explicit hard-cut end frames and continuity handles
- Diegetic ambience and synchronized SFX without BGM
- Correct Seedance 2 API payload guidance
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

The validator checks 15-second segment timing, reference anchors, end-frame requirements, hard-cut continuity, required prompt sections, and SFX-only audio rules.

## Repository layout

```text
2-2-video/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── references/
│   ├── agent-escort-example.md
│   ├── master-character-board.md
│   └── prompt-templates.md
└── scripts/
    └── validate_plan.py
```

## License

No license has been granted yet. The repository is public for viewing and use subject to applicable copyright law; add an explicit open-source license if you want to permit redistribution and modification under defined terms.
