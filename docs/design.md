# Cyan// current H1x0 design baseline

This document records the implemented design decisions for the H1x0 edition.
The revised maximalist `PRD.md` remains authoritative if this summary conflicts
with it; completed browser/WPS work is a baseline, not the end of scope.

## Product character

Cyan// is a small technical instrument: terse, calm, high-contrast, and
terminal-adjacent without fake shell decoration. Apple Music influences the
information hierarchy only. The theme must not resemble an original iPod.

## Priority order

1. Browse, search, and selection
2. Now Playing
3. Rockbox menus and settings

Readability beats density. Remove low-value information before reducing primary
type sizes. Optimize for quick glances at roughly 18–30 inches, including with
the H120's blue backlight off.

## Typography

| Role | Frozen starting font |
|---|---|
| Browser and menu rows | 14-Terminus |
| Browser context header | 14-Terminus-Bold |
| Compact status | 12-Terminus |
| Native Track Info | 12-Terminus |
| WPS title | 18-Terminus-Bold |
| WPS artist | 16-Terminus |
| WPS album | 12-Terminus |

Do not choose a smaller browser font merely to fit more rows. Long strings may
scroll or truncate; both behaviors require physical testing.

## Browser language

- One clear context title at the top. Database, File, and Settings screens
  combine `MUSIC /`, `FILES /`, or `CONFIG /` with Rockbox's actual list title.
- Six 16-pixel list slots in the Milestone 1 geometry.
- Full-width inverse selected row.
- Large `>>` at the left of the selected row; dense technical rows retain `::`.
- A generated 13-pixel icon column appears only where Rockbox supplies a
  reliable semantic list callback.
- No persistent scrollbar in Milestone 1.
- Segmented one-pixel separators above functional footers.
- Compact graphical battery occupies the upper-right header on every screen.
- Footers report real action or state such as `SELECT:OPEN`, `LEFT:BACK`,
  `NOW//CURRENT`, `DATA//LIVE`, or live recording format.

The prompt marker and inverse bar are functional state, not decoration.

Long combined headers scroll inside the dedicated 136-pixel title viewport;
the fixed battery remains outside that viewport and cannot be overwritten.

## Geometry for 160×128 grayscale

| Region | Coordinates | Purpose |
|---|---:|---|
| Header | `x=0, y=0, w=160, h=16` | context + upper-right battery |
| List UI viewport | `x=0, y=16, w=160, h=96` | six 16-pixel rows |
| Footer rule | `y=112, h=1` | segmented region separation |
| Footer | `x=0, y=114, w=160, h=14` | operational state/actions |

The coordinates are target-specific. Design rules, target geometry, and future
assets remain separate so later ports can be deliberately laid out rather than
automatically scaled.

## Now Playing language

The WPS uses a fixed information hierarchy: title, artist, album, progress,
elapsed/remaining time, then status. Track title is 18-Terminus-Bold;
technical codec and bitrate fields are intentionally absent.

| Region | Coordinates | Purpose |
|---|---:|---|
| WPS header | `x=0, y=0, w=160, h=16` | normal-case context + battery |
| Track title | `x=2, y=20, w=156, h=22` | primary metadata |
| Artist | `x=2, y=45, w=156, h=18` | secondary metadata |
| Album | `x=2, y=66, w=156, h=14` | tertiary metadata |
| Progress | `x=2, y=84, w=156, h=5` | odd-height playback rail |
| Time | `y=94, h=12` | elapsed + remaining |
| Status rail | `y=108–127` | transient volume, sleep time, centered playback, optional modes |

Graphics must answer: what is happening, how much, where am I, or what is
selected? Generated one-bit assets show stop, play, pause, fast-forward,
rewind, seek position, discrete battery level, charging, repeat, repeat-one,
and shuffle. The seven-pixel seek diamond remains centered over the five-pixel
progress rail. Short upper/lower border continuations enter its bitmap field
from both sides, seating the marker in the bar without thickening the rail. Playback state uses an
11×11 icon centered in the bottom rail; repeat and shuffle use 13×9 icons and
appear only when active. During volume adjustment, a wide level meter
temporarily takes over the complete bottom rail and hides its normal indicators.
Native Rockbox drawing supplies progress and volume fills; generated assets
provide recognizable state silhouettes. The seek asset is a 9×9 bitmap with a
seven-pixel black diamond and a one-pixel white separation field. On the rail's
two border rows, two black pixels enter from each side and stop before the
white edge around the diamond. The
sleep indicator spells `Zzz` in a dedicated 13×9 bitmap.

Main Hold and an active sleep timer use compact nine-pixel bitmap marks in the
normal rail and consume no space when inactive. Repeat A-B has a dedicated
third repeat frame. Fast-forward and rewind temporarily replace the header with
`SEEK//FORWARD` or `SEEK//REWIND`. During the final seven seconds, `UP NEXT//`
plus the next title and artist replaces only the album line; the current title
and artist remain stable.

## Native Track Info language

Cyan// uses Rockbox's native Track Info screen as its optional technical
playback view. It is opened from Now Playing with `ON + MODE`; playback
continues, and `LEFT` or `OFF` returns. Cyan// does not duplicate track metadata
inside the WPS and does not assign the user's optional WPS hotkey.

When Rockbox reports current-screen value 20, the SBS switches to:

- a literal `[ TRACK//INFO ]` header
- 12-Terminus list text and eight 12-pixel rows
- `>>` selected and `::` unselected TUI prompts
- a `META//NATIVE` / `LEFT:BACK` footer

The underlying list, field ordering, missing-value handling, scrolling, and
track-change refresh remain firmware-owned. Consequently codec, bitrate,
sample rate, ReplayGain, file size, path, and every other field supported by
the installed Rockbox build remain available without copied theme logic.

## Native playback-support lists

Revised Milestone 4 remains native-list-first:

- Current Playlist uses `QUEUE//` and `%LN` line numbers.
- Playlist Catalogue uses `PLAYLISTS//` and the normal readable list rows.
- Context Menu uses `ACTION//` with `>>`/`::` command-palette prompts.
- Shortcuts uses `SHORTCUTS//` with the same command-palette prompts.

Cyan changes only SBS chrome and row rendering. Playlist state, action names,
shortcut assignments, selection behavior, and execution remain Rockbox-owned.

## Milestone 5 polish decisions

- Browser headers scroll within the 136-pixel title viewport rather than
  colliding with the fixed upper-right battery.
- Track, artist, and album remain independently clipped and scrolled by their
  Rockbox viewports; metadata never enters the time/progress region.
- The five-pixel progress rail and seven-pixel seek diamond retain a shared
  center row. Border continuations within the seek asset seat the marker more
  congruently without changing the rail height.
- Bottom icons share a visual center near `y=118`: playback is 11×11 and the
  optional repeat/shuffle marks are 13×9.
- The one-pixel header/footer rules and pure one-bit assets remain unchanged for
  maximum backlight-off contrast. No decorative grayscale was introduced.
- Asset dimensions are executable invariants in `tools/check-assets.py`.

## Pre-final terminal/instrument decisions

- Human content uses `DOMAIN / Context`; action surfaces use `ACTION//`-style
  identities; technical instruments use bracketed headers such as
  `[ RADIO//RX ]`, `[ RECORD//LINE ]`, and `[ SYSTEM//INFO ]`.
- Main FM uses a left-aligned `FREQ//` datum, labeled native RSSI rail,
  receiver-state cells, and generated lock/search and stereo/mono icons.
- Recording retains the native body while its chrome maps the real source to
  terse uppercase labels and shows generated active/pause state.
- QuickScreen retains native controls inside four short crosshair datum rails.
- Pure one-bit rendering remains deliberate; grayscale experimentation is
  deferred to a later major version.

## Milestone 9 regression decisions

- All 111 numeric main/remote viewport declarations remain inside their target
  LCD bounds; `tools/check-layout.py` makes this an executable invariant.
- The bordered seek marker remains centered on the five-pixel rail and is
  reviewed at exactly 0%, 50%, and 100%, including the rail endpoints.
- The fixed 20-pixel battery reservation continues to protect every main and
  remote header from long scrolling titles.
- Pure one-bit foreground/background rendering remains the contrast baseline;
  no decorative grayscale is introduced during polish.
- Browser inversion is a composition proxy only. Backlight and real LCD
  inversion judgments are reserved for the physical H120/H140 gate.
