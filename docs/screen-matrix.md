# Cyan// H1x0 screen matrix

Research snapshot: 2026-08-20, revised PRD roadmap. The upstream `%cs` list
currently contains 20 screen categories. “SBS/list” means Cyan can style shared
chrome and, when the firmware uses `gui_synclist`, its rows. Only the custom
status bar, WPS, and FM screen are independent skinnable-screen types in the
current engine; other native screens are not separate skin files.

Status meanings:

- **Complete** — intentional Cyan treatment exists in source and browser proxy.
- **Partial** — shared Cyan styling applies, but the revised PRD calls for a
  more specific treatment or firmware owns part of the body.
- **Pending** — supported route identified; implementation not started.
- **External** — the plugin/application owns rendering beyond Cyan's skin.

## Milestone 8 audit result

**PASS — all 20 current `%cs` values are explicitly classified.** No category
remains partially planned or undocumented:

- **17 themed/conditional:** 1–10 except 11, plus 12, 13, 15, 16, and 18–20
- **2 plugin-owned:** 11 Pitch on current master and 14 Plugin runtime
- **1 unavailable on H120:** 17 Time and Date because the target has no RTC

“External” and “Unavailable” are completed scope decisions, not incomplete
implementations. Physical testing remains pending independently of this source
coverage audit. Run `tools/check-screen-coverage.py` to verify that the matrix,
source routes, and boundary classifications remain complete.

| `%cs` | Upstream screen | H120 | Theme surface / useful tags | Cyan target | Font | Status | Screenshot | Physical test |
|---:|---|---|---|---|---|---|---|---|
| 1 | Menus | Yes | SBS/list: `%Lt`, `%LT`, `%Lc`, `%Lb` | Native contextual title; `SYSTEM//` only when no useful title exists | 14 Terminus | Complete, generic | Browser proxy | Pending |
| 2 | WPS | Yes | `Cyan.wps`; playback, metadata, bar and state tags | Disciplined `Now Playing` hierarchy and conditional state rail | Mixed 18/16/12 | Complete through revised Milestone 3 | Core metadata plus ten playback-state browser proxies | Pending |
| 3 | Recording screen | Yes | SBS `%cs`; native recorder owns meters/body; recording tags supply technical chrome | `[ RECORD//SOURCE ]`, generated state icon, native meters, real state/time/rate/encoder/channel footer | 12 Terminus body, 14 Bold chrome | Complete to native boundary; terminal/instrument pass | Four browser proxies | Pending |
| 4 | FM Radio screen | Yes | Dedicated `.fms`; `%tf`, `%tt`, `%tm`, `%ts`, `%tr`, preset/RDS and playback tags | `[ RADIO//RX ]`, left datum, labeled RSSI, receiver cells, tactical icons | 12/14/18 Terminus | Complete; receiver-style terminal/instrument pass | Three browser proxies | Pending |
| 5 | Current Playlist | Yes | SBS/list; `%LN`, `%LT`, `%Lc`, `%LI`; Icon_Audio callback identifies the playing entry | `QUEUE//`, numbered rows, explicit `NOW>` playing marker independent of inverse selection | 14 Terminus | Complete; Queue A selected in pre-final review | Browser proxy | Pending |
| 6 | Settings menus | Yes | SBS/list | `CONFIG /` plus native setting title; readable values | 14 Terminus | Complete | Browser proxy | Pending |
| 7 | File browser | Yes | SBS/list | `FILES /` plus native context; strongest list treatment | 14 Terminus | Complete | Browser proxy | Pending |
| 8 | Database browser | Yes | SBS/list | `MUSIC /` plus native context; strongest list treatment | 14 Terminus | Complete | Browser proxy | Pending |
| 9 | Plugin browser | Yes | SBS/list | `TOOLS//` command-launcher treatment | 14 Terminus | Complete through Milestone 7 | Browser proxy | Pending |
| 10 | QuickScreen | Yes | Core screen uses themed UI viewport; `%QT/%Qt`, `%QR/%Qr`, `%QB/%Qb`, `%QL/%Ql` also expose assigned names/values | `QUICK//`, four datum rails, operational directional footer | 14 Terminus | Complete; terminal/control-matrix pass | Browser proxy | Pending |
| 11 | Pitchscreen | Yes | Current core loader launches self-drawing `pitch_screen.rock`; activity/theme calls are absent/commented in the plugin | Preserve native calibration instrument; document external ownership | Plugin-owned | External on current master; conditional legacy header retained | Native-boundary proxy | Per plugin/build |
| 12 | Setting chooser | Yes | SBS/list | Native setting title with focused `>>`/`::` selection | 14 Terminus | Complete through Milestone 7 | Browser proxy | Pending |
| 13 | Playlist Catalogue Viewer | Yes | SBS/list | `PLAYLISTS//` with normal strong selection | 14 Terminus | Complete through revised Milestone 4 | Browser proxy | Pending |
| 14 | Plugin | Yes | Usually plugin-owned; SBS only when plugin returns to a native surface | Document external rendering; `PLUGIN//` only where genuinely available | Plugin-owned | External | N/A per plugin | Per plugin |
| 15 | Context menu | Yes | SBS/list | `ACTION//` action-palette chrome; retain native action names | 14 Terminus | Complete through revised Milestone 4 | Browser proxy | Pending |
| 16 | System Info screen | Yes | Native simple-list with battery, buffer, paths, version and volume data | `SYSTEM//INFO`, dense workstation rows | 12 Terminus | Complete through Milestone 7 | Browser proxy | Pending |
| 17 | Time and Date screen | No RTC in current H120 target config | SBS `%cs` only if reachable on another build/target | `CLOCK//` conditional retained; no H120 body invented | 12 Terminus | Unavailable and documented through Milestone 7 | Boundary proxy | N/A |
| 18 | Bookmark browser | Yes | SBS/list | `BOOKMARKS//`, preserve native bookmark text and resume actions | 14 Terminus | Complete through Milestone 7 | Browser proxy | Pending |
| 19 | Shortcuts menu | Yes | SBS/list | `SHORTCUTS//` command-palette treatment | 14 Terminus | Complete through revised Milestone 4 | Browser proxy | Pending |
| 20 | Track Info screen | Yes | SBS/list, `%cs`; firmware-owned paired metadata list | `[ TRACK//INFO ]`, dense native technical list | 12 Terminus | Complete through revised Milestone 4 | Browser proxy, four scroll positions | Pending |

## Architectural constraints

### Remote matrix

| Remote surface | Native route | Cyan treatment | Status | Physical test |
|---|---|---|---|---|
| While Playing | `rwps` at 128×64×1 | Two metadata rows, progress/time, transient volume, centered playback state, sleep countdown, distinct power, `M.HOLD`/`R.HOLD` | Complete in source and browser proxy | Pending compatible remote |
| Lists/menus | `rsbs` plus native list callbacks | Five 10-pixel 10-ProFont rows, contextual header with compact Hold state, full inverse selected row, `>>` prompt; no footer | Complete where Rockbox applies RSBS | Pending compatible remote |
| Remote FM | `rfms` at 128×64×1 | Frequency, preset, real RSSI rail, tuning/stereo state, audio live/muted, distinct power | Complete in source and browser proxy | Pending compatible remote |

- Current Rockbox defines only `CUSTOM_STATUSBAR`, `WPS`, and `FM_SCREEN` as
  independent skinnable screens. There is no dedicated recording, QuickScreen,
  pitch, or system-info skin file in that enum. Cyan must use SBS detection and
  preserve native rendering for those bodies.
- `%cs` is a detection mechanism, not proof that the entire screen can be
  redrawn by a theme.
- List categories can share Cyan's existing row renderer. Screen-specific
  identity should not discard a meaningful native `%Lt` title.
- Plugin runtime screens remain plugin-owned unless the plugin deliberately
  uses normal Rockbox UI services.

## Sources

- [Current theme-tag appendix](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex)
- [Current skinnable-screen enum](https://github.com/Rockbox/rockbox/blob/master/apps/gui/skin_engine/skin_engine.h)
- [H120/H140 target configuration](https://github.com/Rockbox/rockbox/blob/master/firmware/export/config/iriverh120.h)
