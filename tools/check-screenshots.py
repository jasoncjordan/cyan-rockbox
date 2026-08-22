#!/usr/bin/env python3
"""Validate the dimensions and labels of Cyan// distribution previews."""

from pathlib import Path

from PIL import Image


ROOT = Path(__file__).resolve().parents[1]
SCREENSHOTS = ROOT / "docs/screenshots"
EXPECTED = {
    "Cyan-wps-browser-proxy.png": (160, 128),
    "Cyan-menu-browser-proxy.png": (160, 128),
    "Cyan-fm-browser-proxy.png": (160, 128),
    "Cyan-recording-browser-proxy.png": (160, 128),
    "Cyan-remote-wps-browser-proxy.png": (128, 64),
}


def main():
    failures = []
    for name, expected_size in EXPECTED.items():
        path = SCREENSHOTS / name
        if not path.exists():
            failures.append(f"missing: {path}")
            continue
        with Image.open(path) as image:
            if image.format != "PNG":
                failures.append(f"{name}: expected PNG, found {image.format}")
            if image.size != expected_size:
                failures.append(
                    f"{name}: expected {expected_size}, found {image.size}"
                )
    if failures:
        raise SystemExit("\n".join(failures))
    print(f"Validated {len(EXPECTED)} labeled browser-proxy screenshots.")


if __name__ == "__main__":
    main()
