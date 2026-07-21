#!/usr/bin/env python3
"""Validate a 2+2Video machine-readable production plan."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


EPSILON = 1e-6
LOCKED_CAMERA_WORDS = {"locked", "fixed", "static", "锁定", "固定", "静止"}


def fail(errors: list[str], path: str, message: str) -> None:
    errors.append(f"{path}: {message}")


def number(value: object) -> bool:
    return isinstance(value, (int, float)) and not isinstance(value, bool)


def validate(path: Path) -> tuple[list[str], list[str]]:
    data = json.loads(path.read_text(encoding="utf-8"))
    errors: list[str] = []
    warnings: list[str] = []
    project = data.get("project", {})
    segments = data.get("segments")

    if not isinstance(segments, list) or not segments:
        return ["segments: expected a non-empty array"], warnings

    total = project.get("total_duration_seconds")
    if not number(total):
        fail(errors, "project.total_duration_seconds", "expected a number")
    elif not math.isclose(total, 15 * len(segments), abs_tol=EPSILON):
        fail(errors, "project.total_duration_seconds", f"expected {15 * len(segments)} for {len(segments)} full blocks")

    previous_anchor_size: str | None = None
    for index, segment in enumerate(segments):
        base = f"segments[{index}]"
        duration = segment.get("duration_seconds")
        if not number(duration) or not math.isclose(duration, 15, abs_tol=EPSILON):
            fail(errors, f"{base}.duration_seconds", "must equal 15")

        references = segment.get("references", {})
        ref_images = references.get("ref_images")
        if not isinstance(ref_images, list) or not ref_images:
            fail(errors, f"{base}.references.ref_images", "must include at least one approved visual anchor")
        beats = segment.get("beats")
        if not isinstance(beats, list) or not beats:
            fail(errors, f"{base}.beats", "expected a non-empty array")
        else:
            cursor = 0.0
            for beat_index, beat in enumerate(beats):
                beat_path = f"{base}.beats[{beat_index}]"
                if not isinstance(beat, dict):
                    fail(errors, beat_path, "expected an object")
                    continue
                start, end = beat.get("start"), beat.get("end")
                if not number(start) or not number(end):
                    fail(errors, beat_path, "start and end must be numbers")
                    continue
                if not math.isclose(start, cursor, abs_tol=EPSILON):
                    fail(errors, f"{beat_path}.start", f"expected {cursor:g}; timestamps must be contiguous")
                if end <= start:
                    fail(errors, f"{beat_path}.end", "must be greater than start")
                cursor = float(end)
            if not math.isclose(cursor, 15, abs_tol=EPSILON):
                fail(errors, f"{base}.beats", f"must end at 15.0, got {cursor:g}")

        anchor = segment.get("end_anchor", {})
        if not isinstance(anchor, dict):
            fail(errors, f"{base}.end_anchor", "expected an object")
            anchor = {}
        start, end = anchor.get("start"), anchor.get("end")
        if not number(start) or not 12 <= start < 15:
            fail(errors, f"{base}.end_anchor.start", "must begin in the final 3 seconds")
        if not number(end) or not math.isclose(end, 15, abs_tol=EPSILON):
            fail(errors, f"{base}.end_anchor.end", "must equal 15")
        camera = str(anchor.get("camera", "")).lower()
        if not any(word in camera for word in LOCKED_CAMERA_WORDS):
            fail(errors, f"{base}.end_anchor.camera", "must be locked/fixed/static")
        for field in ("composition", "subject_state", "shot_size"):
            if not str(anchor.get(field, "")).strip():
                fail(errors, f"{base}.end_anchor.{field}", "must be explicit")
        hold = anchor.get("hold_seconds")
        if not number(hold) or not 0.3 <= hold <= 0.7:
            fail(errors, f"{base}.end_anchor.hold_seconds", "must be between 0.3 and 0.7")

        current_size = str(anchor.get("shot_size", "")).strip().lower()
        if previous_anchor_size:
            first_beat = beats[0] if isinstance(beats, list) and beats and isinstance(beats[0], dict) else {}
            first_size = str(first_beat.get("shot_size", "")).strip().lower()
            if not first_size:
                fail(errors, f"{base}.beats[0].shot_size", "must be explicit at a segment boundary")
            elif first_size == previous_anchor_size:
                fail(errors, f"{base}.beats[0].shot_size", "must differ from the previous end anchor")
        previous_anchor_size = current_size or None

        if index < len(segments) - 1:
            opening = segment.get("next_opening", {})
            if str(opening.get("cut", "")).lower() not in {"hard", "hard cut", "硬切"}:
                fail(errors, f"{base}.next_opening.cut", "must be hard")
            if not str(opening.get("visual_link", "")).strip():
                fail(errors, f"{base}.next_opening.visual_link", "must name the continuity handle")
            if str(opening.get("shot_size", "")).strip().lower() == current_size:
                fail(errors, f"{base}.next_opening.shot_size", "must differ from the outgoing end anchor")

        audio = segment.get("audio", {})
        if audio.get("bgm") is not False:
            fail(errors, f"{base}.audio.bgm", "must be false")
        if audio.get("sfx_only") is not True:
            fail(errors, f"{base}.audio.sfx_only", "must be true")
        if not isinstance(audio.get("events"), list) or not audio.get("events"):
            fail(errors, f"{base}.audio.events", "must list at least one ambience or SFX event")

        prompt = str(segment.get("video_prompt", "")).lower()
        no_music = any(token in prompt for token in ("no bgm", "无bgm", "不要bgm", "no music", "无音乐"))
        sfx_only = any(token in prompt for token in ("sfx only", "sound effects only", "仅音效", "只有音效"))
        required_sections = ("subjects", "environment", "style", "continuity", "audio rule", "timeline")
        for section in required_sections:
            if section not in prompt:
                fail(errors, f"{base}.video_prompt", f"missing required section: {section.upper()}")
        if "hard-cut end frame" not in prompt and "hard cut end frame" not in prompt and "硬切结束画面" not in prompt:
            fail(errors, f"{base}.video_prompt", "must name the HARD-CUT END FRAME")
        if not no_music:
            fail(errors, f"{base}.video_prompt", "must explicitly prohibit BGM/music")
        if not sfx_only:
            fail(errors, f"{base}.video_prompt", "must explicitly request SFX only")

    return errors, warnings


def main() -> int:
    if len(sys.argv) != 2:
        print("usage: validate_plan.py PLAN.json", file=sys.stderr)
        return 2
    try:
        errors, warnings = validate(Path(sys.argv[1]))
    except (OSError, json.JSONDecodeError) as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2
    for warning in warnings:
        print(f"WARNING: {warning}")
    if errors:
        for error in errors:
            print(f"ERROR: {error}")
        print(f"FAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    print(f"OK: plan satisfies the 2+2Video contract ({len(warnings)} warning(s))")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
