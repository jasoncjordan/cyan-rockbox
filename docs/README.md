# Cyan//

Cyan// is a large-type, TUI-inspired Rockbox theme for the iRiver H120/H140
family. Version 0.1.0 is the current H1x0 release candidate with readable
14-Terminus lists, a clear context header, full-width inverse selection,
prompt-style `>>` marker, and a large-type Now Playing screen for the physical
160×128 grayscale display.

## Current H1x0 release candidate

The revised `PRD.md` defines a ten-milestone maximalist H-series roadmap. The
current implementation preserves the completed browser, WPS, playback-state,
and native Track Info work while development continues across the remaining
Rockbox surfaces. It includes:

- the frozen design rules in [`docs/design.md`](docs/design.md)
- the revised Milestone 0 completion report in
  [`docs/milestone-0.md`](docs/milestone-0.md)
- the revised Milestone 2 implementation report in
  [`docs/milestone-2.md`](docs/milestone-2.md)
- the revised Milestone 3 implementation report in
  [`docs/milestone-3.md`](docs/milestone-3.md)
- the revised Milestone 4 implementation report in
  [`docs/milestone-4.md`](docs/milestone-4.md)
- the revised Milestone 5 implementation report in
  [`docs/milestone-5.md`](docs/milestone-5.md)
- the Milestone 6 remote implementation report in
  [`docs/milestone-6.md`](docs/milestone-6.md)
- the Milestone 7 utility-surface implementation report in
  [`docs/milestone-7.md`](docs/milestone-7.md)
- the Milestone 8 full-screen coverage audit in
  [`docs/milestone-8.md`](docs/milestone-8.md)
- the Milestone 9 polish and stress-test report in
  [`docs/milestone-9.md`](docs/milestone-9.md)
- the Milestone 10 distribution report in
  [`docs/milestone-10.md`](docs/milestone-10.md)
- current Rockbox implementation notes in
  [`docs/rockbox-notes.md`](docs/rockbox-notes.md)
- the required 20-screen audit in
  [`docs/screen-matrix.md`](docs/screen-matrix.md)
- the H120/H140 hardware/skin exposure audit in
  [`docs/h1x0-capabilities.md`](docs/h1x0-capabilities.md)
- reference-theme findings in
  [`docs/reference-themes.md`](docs/reference-themes.md)
- the physical-device install and test procedure in
  [`docs/testing.md`](docs/testing.md)
- the CheckWPS, simulator, screenshot, and final device procedure in
  [`docs/final-validation.md`](docs/final-validation.md)
- release installation instructions in
  [`docs/installation.md`](docs/installation.md)
- release and submission readiness notes in
  [`docs/release.md`](docs/release.md) and
  [`docs/submission.md`](docs/submission.md)
- the installable source tree under `src/h1x0/.rockbox/`

Revised Milestone 1 combines `MUSIC /`, `FILES /`, and `CONFIG /` with
Rockbox's native Database, File, and Settings titles. These headers scroll
inside a fixed title viewport and preserve the upper-right battery region.

The three comparison profiles share one SBS layout:

- `Cyan-14.cfg` — 14-Terminus
- `Cyan-14-Bold.cfg` — 14-Terminus-Bold
- `Cyan-16.cfg` — 16-Terminus

`Cyan.cfg` remains the default 14-Terminus profile. All four configurations now
load the shared `Cyan.wps`, which adds the PRD hierarchy of large track title,
artist, album, playback state, progress, time, transient volume, and power.

The revised Milestone 3 playback-state system adds compact repeat-all,
repeat-one, repeat-A-B, shuffle, Hold, sleep, and charging indicators;
directional seek headers with a diamond marker; a discrete terminal-shaped
battery; a temporary expanded volume meter; and a calm seven-second Up Next
cue. Inactive status modes consume no permanent icon space.

The current polish pass freezes the refined geometry, adds scrolling for long browser
headers, verifies generated bitmap dimensions, and expands the long-string,
clipping, punctuation, alignment, and contrast test matrix.

Revised Milestone 4 integrates Current Playlist, native Track Info, Context
Menu, Playlist Catalogue, and Shortcuts. `%cs` gives each surface intentional
SBS chrome while preserving firmware data and actions. Track Info uses dense
12-Terminus rows; queue rows convert Rockbox's current-track callback into an
explicit `NOW>` marker independent of the inverse navigation cursor;
Context Menu and Shortcuts use command-palette prompts. Cyan// does not force
the configurable WPS hotkey. It enables the playlist-icon callback because the
approved Queue A renderer depends on that firmware-owned current-track signal.

Revised Milestone 5 adds a dedicated `RADIO//` FMS and integrates the native
recorder as a denser `RECORD//` instrument surface. Mic, Line, FM, recording
format/frequency, S/PDIF input selection, and S/PDIF output-enable state come
from verified Rockbox settings; peak meters and recording control remain
firmware-owned.

Milestone 6 adds dedicated 128×64×1 `Cyan.rwps`, `Cyan.rsbs`, and `Cyan.rfms`
surfaces. The remote
uses a larger 10-ProFont scale, a glanceable two-line playback hierarchy,
compact progress/time and playback state, a discrete battery, and explicit
`M.HOLD` versus `R.HOLD` states. Remote lists keep five larger native rows with
Cyan's full-width inverse selection and native list context.

Milestone 7 adds `QUICK//`, focused Setting Chooser chrome, dense
`SYSTEM//INFO`, `BOOKMARKS//`, and `TOOLS//` treatments through the shared SBS.
QuickScreen retains Rockbox's native four-way names, values, arrows, and
actions. Current Rockbox implements Pitch as the self-drawing
`pitch_screen.rock` plugin, arbitrary plugin runtimes remain theme-external,
and the H120 target has no RTC; those boundaries are documented rather than
simulated in the installable skin.

Milestone 8 closes the complete current `%cs` audit: 17 categories are themed
or conditionally integrated, Pitch and arbitrary Plugin runtime are explicitly
plugin-owned, and Time/Date is explicitly unavailable on the no-RTC H120.
`tools/check-screen-coverage.py` prevents any of the 20 categories from becoming
undocumented.

Milestone 9 completes the source and browser polish gate. One hundred eleven viewport
declarations are checked against the main and remote LCD bounds, and the
browser matrix exercises long content, seek endpoints, inversion, power and
transient states, FM, recording, playlist transitions, and the remote. The
PRD's separate physical-device observations remain pending.

The pre-final terminal/instrument pass adds operational footers, bracketed
technical headers, receiver-style FM geometry, recording-state graphics,
QuickScreen datum rails, and a generated 13-pixel semantic list icon set while
retaining the approved `>>` and `::` prompt language. Pure one-bit rendering
remains the v0.1 contrast baseline; grayscale experimentation is deferred.

Milestone 10 packages the 0.1.0 H1x0 release candidate for official Rockbox
4.0 and current compatible `iriverh120` builds. The distribution includes
installation and compatibility notes, checksums, license, and clearly labeled
browser-proxy screenshots. Theme-site submission remains gated on CheckWPS,
simulator/device captures, physical testing, and submitter contact details.

## Build the current test archive

From the repository root:

```sh
./tools/package.sh
```

This validates the required release files and creates
`dist/Cyan-0.1.0-h1x0.zip`. Development-only typography profiles are excluded
from the clean archive. The optional Rockbox font pack must already be installed
on the player; Cyan// does not redistribute its fonts.

To verify generated one-bit asset dimensions before packaging:

```sh
python3 tools/check-assets.py
```

To verify that every current Rockbox screen category remains classified:

```sh
python3 tools/check-screen-coverage.py
```

To verify viewport bounds and frozen high-risk geometry:

```sh
python3 tools/check-layout.py
```

To build the complete documented release-candidate bundle:

```sh
./tools/package-distribution.sh
```

## Target

- iRiver H120/H140 (`iriverh120` Rockbox target)
- main LCD: 160×128, 2-bit grayscale
- required fonts: `12-Terminus.fnt`, `14-Terminus.fnt`,
  `14-Terminus-Bold.fnt`, `16-Terminus.fnt`, and `18-Terminus-Bold.fnt`
- remote font: `10-ProFont.fnt`

## License

Cyan// original theme and documentation files are licensed under
[CC BY-SA 3.0](LICENSE). Files in `reference/` are unmodified research inputs
and retain their original authorship and licensing.
