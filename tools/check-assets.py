#!/usr/bin/env python3
"""Validate Cyan// H1x0 bitmap dimensions and strip frame counts."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
ASSETS = ROOT / "src/h1x0/.rockbox/wps/Cyan"
ICONS = ROOT / "src/h1x0/.rockbox/icons"
EXPECTED = {
    "playback.bmp": (11, 55),       # five 11x11 frames
    "battery.bmp": (18, 42),        # six 18x7 frames
    "charging.bmp": (18, 7),
    "powered.bmp": (18, 7),
    "disk.bmp": (5, 5),
    "repeat.bmp": (13, 27),         # all, one, and A-B 13x9 frames
    "hold.bmp": (9, 9),
    "sleep.bmp": (13, 9),
    "shuffle.bmp": (13, 9),
    "seek.bmp": (9, 9),            # bordered diamond plus rail continuations
    "remote-playback.bmp": (9, 45), # five 9x9 remote frames
    "remote-battery.bmp": (14, 42), # six 14x7 remote frames
    "remote-charging.bmp": (14, 7),
    "remote-powered.bmp": (14, 7),
    "fm-state.bmp": (13, 52),       # lock, search, stereo, mono
    "record-state.bmp": (13, 26),   # active and paused
    "remote-hold.bmp": (9, 18),     # main and remote locks
    "remote-fm-state.bmp": (9, 36), # lock, search, stereo, mono
}


def main():
    failures = []
    for name, expected_size in EXPECTED.items():
        path = ASSETS / name
        if not path.exists():
            failures.append(f"missing: {path}")
            continue
        with Image.open(path) as image:
            if image.size != expected_size:
                failures.append(
                    f"{name}: expected {expected_size}, found {image.size}"
                )
            if image.mode != "1":
                failures.append(f"{name}: expected one-bit mode, found {image.mode}")
    icon_path = ICONS / "Cyan-13.bmp"
    if not icon_path.exists():
        failures.append(f"missing: {icon_path}")
    else:
        with Image.open(icon_path) as image:
            if image.size != (13, 416) or image.mode != "1":
                failures.append(
                    f"Cyan-13.bmp: expected one-bit 13x416, "
                    f"found {image.mode} {image.size}"
                )
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Validated {len(EXPECTED) + 1} one-bit Cyan// assets.")


if __name__ == "__main__":
    main()
