# Milestone 7 — Utility surfaces

Implementation snapshot: 2026-08-20. This milestone integrates every reachable
H120 utility surface named by the PRD and records the two current native
boundaries that cannot honestly be themed.

## Integrated surfaces

- **QuickScreen (`%cs=10`)** — `QUICK//` header, shared battery, dense
  12-Terminus UI viewport, and a compact native-control footer. Rockbox still
  draws the assigned setting names, current values, directional arrows, and
  handles all four actions. Cyan does not force the user's QuickScreen slots.
- **Setting Chooser (`%cs=12`)** — retains the native setting title as
  `CONFIG / …`, with a full-width inverse selection and `>>`/`::` modal prompts.
- **System Info (`%cs=16`)** — `SYSTEM//INFO`, dense 12-Terminus rows, and
  `NATIVE//DATA` chrome around the firmware's simple list. Current native data
  includes battery/time, audio buffer size, recording/root paths, version, and
  internal-volume free/total space; Cyan adds no fields.
- **Bookmark Browser (`%cs=18`)** — `BOOKMARKS//` plus normal Cyan list
  selection while preserving Rockbox's bookmark text, position, and resume
  actions.
- **Plugin Browser (`%cs=9`)** — `TOOLS//` command-launcher treatment using
  native plugin categories, names, navigation, and launch actions.

## Native and unavailable boundaries

Current Rockbox's core Pitch entry loads `/.rockbox/rocks/viewers/pitch_screen.rock`.
That plugin calls `viewport_set_defaults`, draws its own three-row instrument,
and has its activity push/pop calls commented out. It does not enable the SBS,
so Cyan cannot reliably add `PITCH//` chrome without modifying firmware or the
plugin. The SBS retains a conditional compatibility header for builds that do
expose `%cs=11`, but current-master Pitch remains theme-external.

The current H120 target does not define `CONFIG_RTC`. `%cs=17` and conditional
`CLOCK//` chrome remain documented for compatibility, but the Time/Date screen
is not reachable and Cyan does not fabricate time or date values.

Arbitrary plugin runtimes likewise own their pixels. Cyan styles the native
Plugin Browser and the UI shown after a plugin returns; it does not attempt to
redesign games, viewers, or applications internally.

## Validation boundary

The browser review includes QuickScreen, Setting Chooser, System Info,
Bookmarks, Plugin Browser, native Pitch, the no-RTC boundary, and plugin-runtime
ownership. Representative browser values illustrate geometry only; the
installable SBS always uses Rockbox's live native strings and callbacks.

Physical H120 validation remains required using [`testing.md`](testing.md).

Sources: [current QuickScreen implementation](https://github.com/Rockbox/rockbox/blob/master/apps/gui/quickscreen.c),
[current Pitch loader](https://github.com/Rockbox/rockbox/blob/master/apps/gui/pitchscreen.c),
[current Pitch plugin](https://github.com/Rockbox/rockbox/blob/master/apps/plugins/pitch_screen.c),
[current System Info implementation](https://github.com/Rockbox/rockbox/blob/master/apps/menus/main_menu.c),
and [current theme tags](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex).
