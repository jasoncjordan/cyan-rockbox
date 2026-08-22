# Milestone 8 — Full `%cs` coverage audit

Audit snapshot: 2026-08-20. The current Rockbox theme-tag appendix defines 20
current-screen categories. Cyan// now has an explicit treatment or documented
boundary for every one.

## Result

| Classification | `%cs` values | Count |
|---|---|---:|
| Themed or conditionally integrated | 1–10 except 11; 12, 13, 15, 16, 18, 19, 20 | 17 |
| Plugin-owned rendering | 11, 14 | 2 |
| Unavailable on H120 | 17 | 1 |

The complete per-screen evidence is maintained in
[`screen-matrix.md`](screen-matrix.md). `tools/check-screen-coverage.py`
enforces the 1–20 set, checks every conditional SBS route, verifies the WPS/FMS
sources, and requires the Pitch, Plugin, and no-RTC boundaries to remain
documented.

## Route summary

- `%cs=2` uses the dedicated `Cyan.wps`.
- `%cs=4` uses the dedicated `Cyan.fms`.
- `%cs=1`, 3, 5–10, 12, 13, 15, 16, and 18–20 use generic or conditional
  `Cyan.sbs` geometry, headers, rows, and native bodies.
- `%cs=11` retains conditional compatibility chrome, but current Rockbox loads
  the self-drawing `pitch_screen.rock`; it is classified plugin-owned.
- `%cs=14` is arbitrary plugin runtime and is classified plugin-owned.
- `%cs=17` retains conditional compatibility chrome but is unreachable on the
  H120 because the target has no RTC.

## Browser evidence

The Milestone 8 browser view presents three dense coverage pages for categories
1–7, 8–14, and 15–20. Each row identifies its dedicated-skin, SBS/native,
external, or target-unavailable route. These pages are an audit visualization,
not additional Rockbox screens.

## Exit gate

The source/documentation coverage gate passes. Parser/simulator and physical
device tests remain separate requirements described in [`testing.md`](testing.md).

Sources: [current `%cs` table](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex),
[current skinnable-screen enum](https://github.com/Rockbox/rockbox/blob/master/apps/gui/skin_engine/skin_engine.h),
and [current H120 target configuration](https://github.com/Rockbox/rockbox/blob/master/firmware/export/config/iriverh120.h).
