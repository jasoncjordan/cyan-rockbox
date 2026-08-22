# Milestone 6 — Remote

Implementation snapshot: 2026-08-20. Cyan// now treats the H1x0 remote as a
native 128×64×1 interface rather than a scaled version of the main LCD.

## Remote WPS

`Cyan.rwps` uses the configured `10-ProFont.fnt`, two pixels larger than the
initial remote prototype. Its hierarchy is intentionally short:

- top-aligned title beside a fixed 14×7 discrete battery
- independently scrolling title and artist rows with filename/unknown fallback
- five-pixel native progress rail plus elapsed and remaining time
- centered 9×9 stop/play/pause/seek state, textual state, and numeric volume
- a compact `CYAN//` status line with `READY`, `M.HOLD`, or `R.HOLD`

Remote Hold (`%mr`) takes display priority over main-unit Hold (`%mh`) when
both are active, making the two physical locks unambiguous.

## Remote lists

`Cyan.rsbs` removes the earlier footer and reserves a 54-pixel native UI
viewport: five complete rows at ten pixels each. The header preserves
Rockbox's native `%Lt` context within a battery-safe scrolling region and shows
a compact `M.H` or `R.H` lock state when active. The selected row uses the same
full-width inverse bar and `>` prompt as Cyan's main browser. Rockbox still
owns list contents, actions, navigation, and screen-specific metadata.

All four development profiles set the current official config keys `remote
font`, `rwps`, `rsbs`, and `remote statusbar`. The clean release package ships
only `Cyan.cfg`, both remote skins, and the two separately generated one-bit
remote asset strips.

## Validation boundary

The generated asset checker validates all ten one-bit assets, and the package
build includes both remote skins. Browser proxies cover playing, paused, main
Hold, remote Hold, long metadata, and remote menu composition at the native
128×64 aspect ratio.

No compatible remote is recorded in `HARDWARE.md`. LCD packing, remote button
behavior, scroll timing, and Hold reporting therefore remain pending the
physical gate in [`testing.md`](testing.md).

Sources: [current Rockbox settings definitions](https://github.com/Rockbox/rockbox/blob/master/apps/settings_list.c),
[current theme tags](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex),
and [current H120 target configuration](https://github.com/Rockbox/rockbox/blob/master/firmware/export/config/iriverh120.h).
