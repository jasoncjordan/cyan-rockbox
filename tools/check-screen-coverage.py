#!/usr/bin/env python3
"""Verify that Cyan// documents every current Rockbox %cs category."""

import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
MATRIX = ROOT / "docs/screen-matrix.md"
SBS = ROOT / "src/h1x0/.rockbox/wps/Cyan.sbs"
WPS = ROOT / "src/h1x0/.rockbox/wps/Cyan.wps"
FMS = ROOT / "src/h1x0/.rockbox/wps/Cyan.fms"
RFMS = ROOT / "src/h1x0/.rockbox/wps/Cyan.rfms"
CFG = ROOT / "src/h1x0/.rockbox/themes/Cyan.cfg"

THEMED = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 12, 13, 15, 16, 18, 19, 20}
EXTERNAL = {11, 14}
UNAVAILABLE = {17}
CONDITIONAL_SBS = {3, 5, 6, 7, 8, 9, 10, 11, 12, 13, 15, 16, 17, 18, 19, 20}


def main():
    matrix = MATRIX.read_text(encoding="utf-8")
    sbs = SBS.read_text(encoding="utf-8")
    wps = WPS.read_text(encoding="utf-8")
    fms = FMS.read_text(encoding="utf-8")
    rfms = RFMS.read_text(encoding="utf-8")
    cfg = CFG.read_text(encoding="utf-8")
    documented = {
        int(number)
        for number in re.findall(r"^\|\s*(\d+)\s*\|", matrix, re.MULTILINE)
    }
    expected = set(range(1, 21))
    failures = []

    if documented != expected:
        failures.append(
            f"screen matrix mismatch: missing={sorted(expected - documented)}, "
            f"extra={sorted(documented - expected)}"
        )

    classified = THEMED | EXTERNAL | UNAVAILABLE
    if classified != expected:
        failures.append("coverage classification does not contain exactly 1–20")
    if (THEMED & EXTERNAL) or (THEMED & UNAVAILABLE) or (EXTERNAL & UNAVAILABLE):
        failures.append("coverage classifications overlap")

    for category in sorted(CONDITIONAL_SBS):
        if not re.search(rf"%cs,\s*=,\s*{category}\)", sbs):
            failures.append(f"Cyan.sbs has no conditional route for %cs={category}")

    if "External on current master" not in matrix:
        failures.append("Pitch external-rendering boundary is undocumented")
    if "Unavailable and documented" not in matrix:
        failures.append("Time/Date target-unavailable boundary is undocumented")
    if "| 14 | Plugin |" not in matrix or "| External |" not in matrix:
        failures.append("plugin-runtime ownership is undocumented")

    for path in (
        ROOT / "src/h1x0/.rockbox/wps/Cyan.wps",
        ROOT / "src/h1x0/.rockbox/wps/Cyan.fms",
        ROOT / "src/h1x0/.rockbox/wps/Cyan.rfms",
        SBS,
    ):
        if not path.is_file():
            failures.append(f"missing themed screen source: {path}")

    if "%tr(" not in fms or "%pb(" in fms:
        failures.append("Cyan.fms must use real %tr RSSI and no playback %pb rail")
    if "%tr(" not in rfms or "rfms: /.rockbox/wps/Cyan.rfms" not in cfg:
        failures.append("remote FM skin is missing or not configured")
    for tag in ("Rr", "Rh", "Rn", "Rs", "Rf", "Re", "Rm"):
        if not re.search(rf"%\??{tag}", sbs):
            failures.append(f"recording technical chrome is missing %{tag}")
    for tag in ("bp", "bc", "lh"):
        if not re.search(rf"%\??{tag}", sbs):
            failures.append(f"SBS system-state chrome is missing %{tag}")
    if "%?bs<%alSLEEP// %bs|>" not in wps:
        failures.append("WPS sleep countdown is missing from the normal rail")
    if "%?mv(2)<|%alVOL" in wps:
        failures.append("WPS still exposes persistent volume outside takeover")
    if "playlist viewer icons: on" not in cfg:
        failures.append("Queue A requires the native playlist icon callback")
    if "%?if(%LI, =, 0)<NOW%>" not in sbs:
        failures.append("Queue A NOW> current-track marker is missing")
    for fragment in (
        "[ RECORD//", "[ SYSTEM//INFO ]", "SELECT:OPEN",
        "LEFT:BACK", "%xl(I,__list_icons__", "%Vl(qn,",
    ):
        if fragment not in sbs:
            failures.append(f"terminal/instrument SBS treatment is missing {fragment}")
    for fragment in (
        "[ RADIO//RX ]", "FREQ//", "RSSI//", "MODE:",
        "fm-state.bmp",
    ):
        if fragment not in fms:
            failures.append(f"receiver-style FM treatment is missing {fragment}")
    if "show icons: on" not in cfg or "Cyan-13.bmp" not in cfg:
        failures.append("generated semantic icon set is not active")

    if failures:
        raise SystemExit("\n".join(failures))

    print(
        "Validated all 20 current %cs categories: "
        f"{len(THEMED)} themed, {len(EXTERNAL)} external, "
        f"{len(UNAVAILABLE)} unavailable on H120."
    )


if __name__ == "__main__":
    main()
