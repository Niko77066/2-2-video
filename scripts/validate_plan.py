#!/usr/bin/env python3
"""Validate a 2+2Video machine-readable production plan."""

from __future__ import annotations

import json
import math
import sys
from pathlib import Path


EPSILON = 1e-6
LOCKED_CAMERA_WORDS = {"locked", "fixed", "static", "锁定", "固定", "静止"}
# duration -> required shot count, from the ceil(duration / 3) density rule
SHOT_COUNTS = {15: 5, 30: 10}


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

    durations = [s.get("duration_seconds") for s in segments if isinstance(s, dict)]
    expected_total = sum(d for d in durations if number(d))
    total = project.get("total_duration_seconds")
    if not number(total):
        fail(errors, "project.total_duration_seconds", "expected a number")
    elif not math.isclose(total, expected_total, abs_tol=EPSILON):
        fail(errors, "project.total_duration_seconds", f"expected {expected_total:g}, the sum of the segment durations")

    previous_anchor_size: str | None = None
    for index, segment in enumerate(segments):
        base = f"segments[{index}]"
        duration = segment.get("duration_seconds")
        if not number(duration) or int(duration) not in SHOT_COUNTS:
            fail(errors, f"{base}.duration_seconds", f"must be one of {sorted(SHOT_COUNTS)}")
            continue
        duration = int(duration)
        required_shots = SHOT_COUNTS[duration]

        references = segment.get("references", {})
        ref_images = references.get("ref_images")
        if not isinstance(ref_images, list) or not ref_images:
            fail(errors, f"{base}.references.ref_images", "must include at least one approved visual anchor")
        beats = segment.get("beats")
        if not isinstance(beats, list) or not beats:
            fail(errors, f"{base}.beats", "expected a non-empty array")
        else:
            if len(beats) != required_shots:
                fail(errors, f"{base}.beats", f"a {duration}s segment needs exactly {required_shots} shots, got {len(beats)}")
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
            if not math.isclose(cursor, duration, abs_tol=EPSILON):
                fail(errors, f"{base}.beats", f"must end at {duration}.0, got {cursor:g}")

        anchor = segment.get("end_anchor", {})
        if not isinstance(anchor, dict):
            fail(errors, f"{base}.end_anchor", "expected an object")
            anchor = {}
        start, end = anchor.get("start"), anchor.get("end")
        if not number(start) or not duration - 3 <= start < duration:
            fail(errors, f"{base}.end_anchor.start", "must begin in the final 3 seconds")
        if not number(end) or not math.isclose(end, duration, abs_tol=EPSILON):
            fail(errors, f"{base}.end_anchor.end", f"must equal {duration}")
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
        if not isinstance(audio.get("events"), list) or not audio.get("events"):
            fail(errors, f"{base}.audio.events", "must list at least one ambience or SFX event")
        if audio.get("bgm") is not False:
            fail(errors, f"{base}.audio.bgm", "must be false; the BGM is added as a separate track after assembly")
        for line_index, line in enumerate(audio.get("dialogue", []) or []):
            line_path = f"{base}.audio.dialogue[{line_index}]"
            if not isinstance(line, dict):
                fail(errors, line_path, "expected an object")
                continue
            if not str(line.get("character", "")).strip():
                fail(errors, f"{line_path}.character", "must name the speaker")
            if not str(line.get("audio_ref", "")).strip():
                fail(errors, f"{line_path}.audio_ref", "must point at this segment's exact dialogue slice")

        prompt = str(segment.get("video_prompt", "")).lower()
        required_sections = ("subjects", "environment", "style", "continuity", "audio rule", "timeline")
        for section in required_sections:
            if section not in prompt:
                fail(errors, f"{base}.video_prompt", f"missing required section: {section.upper()}")
        if "hard-cut end frame" not in prompt and "hard cut end frame" not in prompt and "硬切结束画面" not in prompt:
            fail(errors, f"{base}.video_prompt", "must name the HARD-CUT END FRAME")
        if required_shots > 5:
            hard_cuts = prompt.count("hard cut in")
            if hard_cuts < required_shots - 1:
                fail(errors, f"{base}.video_prompt", f"shots 02-{required_shots:02d} must each say HARD CUT IN ({required_shots - 1} expected, found {hard_cuts})")
        no_music = any(token in prompt for token in ("no bgm", "无bgm", "不要bgm", "no music", "无音乐"))
        if not no_music:
            fail(errors, f"{base}.video_prompt", "must explicitly prohibit model-generated BGM/music")
        if "dialogue" not in prompt:
            fail(errors, f"{base}.video_prompt", "must state dialogue lines or 'Dialogue: none'")

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
