# Install Cyan// 0.1.0 on an iRiver H120/H140

Cyan// is a normal Rockbox theme. It does not replace or modify firmware and it
does not touch music files.

## Requirements

- iRiver H120 or H140 already running Rockbox
- official Rockbox 4.0 or a current compatible `iriverh120` build
- optional Rockbox font pack installed
- these font files present under `/.rockbox/fonts/`:
  - `12-Terminus.fnt`
  - `14-Terminus.fnt`
  - `14-Terminus-Bold.fnt`
  - `16-Terminus.fnt`
  - `18-Terminus-Bold.fnt`
  - `10-ProFont.fnt`

## Install

1. Build or obtain `Cyan-0.1.0-h1x0.zip`.
2. Connect the powered-off player by USB, then start it in normal USB-storage
   mode.
3. Confirm the player root already contains `.rockbox`. Do not format it and do
   not delete or replace Rockbox firmware files.
4. Extract the ZIP into the player root, merging its `.rockbox` directory with
   the existing one.
5. Confirm these files were installed:
   - `/.rockbox/themes/Cyan.cfg`
   - `/.rockbox/wps/Cyan.sbs`
   - `/.rockbox/wps/Cyan.wps`
   - `/.rockbox/wps/Cyan.fms`
   - `/.rockbox/wps/Cyan.rfms`
   - `/.rockbox/wps/Cyan.rwps`
   - `/.rockbox/wps/Cyan.rsbs`
   - `/.rockbox/wps/Cyan/` with eighteen screen/status BMP assets
   - `/.rockbox/icons/Cyan-13.bmp`
6. Eject the player cleanly and disconnect USB.
7. Open `Settings → Theme Settings → Browse Theme Files`, select `Cyan.cfg`,
   and confirm.
8. Check a Files or Database list and the While Playing Screen before relying
   on the theme away from the computer.

## Optional technical playback view

From Now Playing, press `ON + MODE` to open Rockbox's native Track Info screen.
Playback continues while its metadata list is open; press `LEFT` or `OFF` to
return. Cyan// styles this native screen with compact 12-Terminus rows and
`[ TRACK//INFO ]` chrome but does not replace Rockbox's metadata implementation.

Cyan// deliberately leaves the configurable WPS hotkey unchanged. Users who
want one-button access may choose `Show Track Info` under
`Settings → General Settings → WPS → WPS Hotkey`; short `REC` then opens it.

## Upgrade

Extract the newer Cyan// ZIP into the player root and allow it to overwrite
only the existing Cyan files. The theme has no settings database or migration
step.

## Roll back or uninstall

Load the previous theme through Rockbox Theme Settings. To remove Cyan//,
delete only:

- `/.rockbox/themes/Cyan.cfg`
- `/.rockbox/wps/Cyan.sbs`
- `/.rockbox/wps/Cyan.wps`
- `/.rockbox/wps/Cyan.fms`
- `/.rockbox/wps/Cyan.rfms`
- `/.rockbox/wps/Cyan.rwps`
- `/.rockbox/wps/Cyan.rsbs`
- `/.rockbox/wps/Cyan/`
- `/.rockbox/icons/Cyan-13.bmp`

The optional Terminus fonts may be shared by other themes and should not be
deleted as part of Cyan// removal.
