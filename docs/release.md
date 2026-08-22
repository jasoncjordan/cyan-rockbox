# Cyan// 0.1.0 H1x0 release candidate

Target: iRiver H120/H140 (`iriverh120`), 160×128 2-bit grayscale.

## Included

- readable 14-Terminus browser and menu typography
- bold scrolling context header with upper-right graphical battery
- full-width inverse selected row with large prompt-style `>>` marker
- generated 13-pixel semantic list icons where firmware callbacks are reliable
- large title, artist, and album hierarchy on Now Playing
- five-pixel progress rail and seven-pixel seek diamond
- graphical stop, play, pause, fast-forward, and rewind states
- repeat, repeat-one, shuffle, charging, and discrete battery indicators
- temporary full-rail volume meter
- native Track Info integration with a conditional 12-Terminus TUI treatment
- numbered Queue rows with independent `NOW>` playback and inverse cursor states
- dedicated H1x0 FM receiver skin
- dedicated remote FM receiver skin with native RSSI rail
- native recording instrumentation with Cyan source/output/state/time/rate/encoder/channel chrome
- dedicated 128×64 remote WPS and five-row large-type remote SBS
- distinct main-unit and remote Hold reporting
- distinct battery, charging, externally powered, sleep-countdown, and disk-I/O states
- integrated QuickScreen, Setting Chooser, System Info, Bookmark, and Plugin Browser chrome
- operational action/state footers and bracketed technical-instrument headers
- generated one-bit assets with executable dimension checks

## Test archive policy

`Cyan-0.1.0-h1x0.zip` contains only the canonical `Cyan.cfg`, main and remote
SBS/WPS files, main/remote FM skins, eighteen screen/status bitmaps, and the
generated `Cyan-13.bmp` icon strip. The development-only
typography comparison configurations remain in source for development but are
deliberately excluded from the user archive.
Fonts are not redistributed; users install the official optional font pack.

## Validation status

Completed locally:

- generated asset dimension and one-bit mode checks
- required release-file checks
- clean archive-content selection
- ZIP CRC/integrity verification
- exact 160×128 browser-proxy geometry review
- long-string clipping and state-layout review
- complete 20-category `%cs` source/documentation audit
- all 111 numeric viewport declarations within main/remote LCD bounds
- browser polish matrix for long content, seek endpoints, inversion, power,
  transient playback states, FM, recording, playlist transition, and remote

Milestones 0–10 are implemented through their source/browser and distribution
gates, but the physical checks below are still open. The inner ZIP is the clean
player install archive; `Cyan-0.1.0-h1x0-distribution.zip` adds documentation,
license, checksums, and clearly labeled browser-proxy screenshots. Neither is
yet a theme-site-ready final release.

Still required before calling 0.1.0 final:

- CheckWPS for `iriverh120`
- H120/H140 simulator load
- physical H120 test with backlight on and off
- physical long-string scrolling and state-transition test
- compatible H1x0 remote test, including remote Hold and RSBS coverage

The exact command sequence and pass criteria for these gates are in
[`final-validation.md`](final-validation.md). The complete physical screen and
state matrix remains in [`testing.md`](testing.md). Both files are included in
the distribution bundle.

Until those checks pass, the archive remains a release candidate rather than a
theme-site-ready final release.
