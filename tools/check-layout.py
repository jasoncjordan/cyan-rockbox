#!/usr/bin/env python3
"""Validate Cyan// viewport bounds and frozen high-risk geometry."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKIN_ROOT = ROOT / "src/h1x0/.rockbox/wps"
TARGETS = {
    "Cyan.sbs": (160, 128),
    "Cyan.wps": (160, 128),
    "Cyan.fms": (160, 128),
    "Cyan.rfms": (128, 64),
    "Cyan.rwps": (128, 64),
    "Cyan.rsbs": (128, 64),
}
VIEWPORT = re.compile(r"%(V|Vl|Vi)\(([^)\n]+)\)")


def dimensions(kind, raw):
    args = [value.strip() for value in raw.split(",")]
    offset = 1 if kind in {"Vl", "Vi"} else 0
    if len(args) < offset + 4:
        return None
    values = args[offset:offset + 4]
    if not all(value == "-" or value.isdigit() for value in values):
        return None
    return values


def resolved(value, origin, extent):
    return extent - origin if value == "-" else int(value)


def main():
    failures = []
    checked = 0
    sources = {}

    for filename, (width, height) in TARGETS.items():
        path = SKIN_ROOT / filename
        source = path.read_text(encoding="utf-8")
        sources[filename] = source
        for line_number, line in enumerate(source.splitlines(), 1):
            if line.lstrip().startswith("#"):
                continue
            for match in VIEWPORT.finditer(line):
                values = dimensions(match.group(1), match.group(2))
                if values is None:
                    failures.append(
                        f"{filename}:{line_number}: unreadable viewport {match.group(0)}"
                    )
                    continue
                x, y = int(values[0]), int(values[1])
                w = resolved(values[2], x, width)
                h = resolved(values[3], y, height)
                checked += 1
                if x < 0 or y < 0 or w <= 0 or h <= 0:
                    failures.append(
                        f"{filename}:{line_number}: non-positive viewport {x},{y},{w},{h}"
                    )
                if x + w > width or y + h > height:
                    failures.append(
                        f"{filename}:{line_number}: viewport exceeds {width}x{height}: "
                        f"{x},{y},{w},{h}"
                    )

    invariants = {
        "Cyan.sbs": (
            "%Vl(h,0,0,136,15,2)",
            "%V(140,4,18,7,-)",
            "%Vi(main,0,16,160,96,1)",
            "%V(0,112,78,1,-)",
            "%V(82,112,78,1,-)",
        ),
        "Cyan.wps": (
            "%Vl(n,2,84,156,5,-)",
            "%Vl(s,2,82,156,9,-)",
            "%pb(0,2,156,5)",
            "%pb(0,0,156,9,nobar,slider,S)",
            "%V(0,108,160,1,-)",
        ),
        "Cyan.rwps": (
            "%V(1,0,110,10,1)",
            "%V(113,1,14,7,-)",
            "%V(1,23,126,5,-)",
            "%V(1,54,58,10,1)",
        ),
        "Cyan.rsbs": (
            "%Vi(remote,0,10,128,54,1)",
            "%Vl(i,0,0,128,10,1)",
            "%V(113,1,14,7,-)",
        ),
        "Cyan.rfms": (
            "%V(1,11,126,10,1)",
            "%V(1,34,126,5,-)",
            "%tr(0,0,126,5)",
            "%V(113,1,14,7,-)",
        ),
    }
    for filename, required in invariants.items():
        for fragment in required:
            if fragment not in sources[filename]:
                failures.append(f"{filename}: missing frozen geometry: {fragment}")

    if failures:
        raise SystemExit("\n".join(failures))

    print(
        f"Validated {checked} viewport declarations across {len(TARGETS)} "
        "skins; frozen header, battery, progress, seek, footer, and remote "
        "geometry is intact."
    )


if __name__ == "__main__":
    main()
