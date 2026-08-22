# H120/H140 0.1.0 release-candidate test

This test validates the complete current installable snapshot: browser, Now
Playing, playback and power states, native playback-support lists, FM,
recording, remote, utilities, complete screen coverage, and
clipping/alignment/contrast behavior. It installs only normal theme files and
does not modify firmware.

## Prerequisites

- iRiver H120 or H140 already running Rockbox
- optional Rockbox font pack already installed
- these files present on the player:
  - `/.rockbox/fonts/14-Terminus.fnt`
  - `/.rockbox/fonts/14-Terminus-Bold.fnt`
  - `/.rockbox/fonts/16-Terminus.fnt`
  - `/.rockbox/fonts/18-Terminus-Bold.fnt`
  - `/.rockbox/fonts/12-Terminus.fnt`
  - `/.rockbox/fonts/10-ProFont.fnt`
- a backup of the player's current Rockbox settings, or at minimum a note of
  the current theme name

## Install from the ZIP

1. Run `./tools/package.sh` in this repository. Confirm that
   `dist/Cyan-0.1.0-h1x0.zip` is created.
2. Connect the powered-off H120 to the computer by USB, then power it on in the
   normal USB-storage mode.
3. Open the player's filesystem. Confirm that a `.rockbox` folder already
   exists at its root. Do not format the player and do not replace the Rockbox
   firmware.
4. Extract `Cyan-0.1.0-h1x0.zip` directly into the player's root. Merge the
   included `.rockbox` folder with the existing `.rockbox` folder.
5. Verify the installed release files:
   - `/.rockbox/themes/Cyan.cfg`
   - `/.rockbox/wps/Cyan.sbs`
   - `/.rockbox/wps/Cyan.wps`
   - `/.rockbox/wps/Cyan.fms`
   - `/.rockbox/wps/Cyan.rwps`
   - `/.rockbox/wps/Cyan.rsbs`
   - `/.rockbox/wps/Cyan.rfms`
   - `/.rockbox/icons/Cyan-13.bmp`
   - `/.rockbox/wps/Cyan/playback.bmp`
   - `/.rockbox/wps/Cyan/battery.bmp`
   - `/.rockbox/wps/Cyan/charging.bmp`
   - `/.rockbox/wps/Cyan/hold.bmp`
   - `/.rockbox/wps/Cyan/repeat.bmp`
   - `/.rockbox/wps/Cyan/shuffle.bmp`
   - `/.rockbox/wps/Cyan/sleep.bmp`
   - `/.rockbox/wps/Cyan/seek.bmp`
   - `/.rockbox/wps/Cyan/remote-playback.bmp`
   - `/.rockbox/wps/Cyan/remote-battery.bmp`
   - `/.rockbox/wps/Cyan/powered.bmp`
   - `/.rockbox/wps/Cyan/disk.bmp`
   - `/.rockbox/wps/Cyan/fm-state.bmp`
   - `/.rockbox/wps/Cyan/record-state.bmp`
   - `/.rockbox/wps/Cyan/remote-charging.bmp`
   - `/.rockbox/wps/Cyan/remote-powered.bmp`
   - `/.rockbox/wps/Cyan/remote-hold.bmp`
   - `/.rockbox/wps/Cyan/remote-fm-state.bmp`
6. Eject/unmount the player cleanly, disconnect USB, and allow Rockbox to boot.
7. In Rockbox open `Settings → Theme Settings → Browse Theme Files`, select
   `Cyan.cfg`, and confirm.
8. Browse both `Files` and `Database` (artists, albums, and tracks). Also open a
   normal Settings menu to exercise list titles and non-music rows.

## Revised Milestone 1 physical gate

Do not change browser typography again until this gate has been run on the
physical H120/H140.

1. In Database, confirm headers combine `MUSIC /` with the native context such
   as Artists, Albums, Songs, and Genres.
2. In Files, confirm headers combine `FILES /` with the current native title or
   folder context. Test the filesystem root and a deeply nested music folder.
3. In Settings, confirm headers combine `CONFIG /` with the native settings
   title without colliding with the upper-right battery.
4. Confirm six complete 16-pixel rows appear in the canonical 14-Terminus
   profile and that at least five remain practically readable at 18–30 inches.
5. Confirm every selected row is full-width inverse with a visible `>>` prompt,
   including while scrolling quickly. Where Rockbox supplies a semantic list
   callback, confirm the generated 13-pixel icon remains separate from the
   selection prompt and does not cover text.
6. Wait for a long header and long row to scroll. Confirm each remains clipped
   to its viewport and never touches the battery or footer.
7. Repeat with backlight on, backlight off, LCD inversion on, and LCD inversion
   off. Record the Rockbox version, contrast value, lighting, and viewing
   distance with every result.

Milestone 1 passes only when Database, Files, standard menus, and Settings all
remain readable and navigable under these conditions. Simulator/browser proxy
approval alone is insufficient.

## Compare the three fonts

This is a developer-only regression test. The clean release ZIP intentionally
contains only `Cyan.cfg`. To repeat the typography comparison, copy
`Cyan-14.cfg`, `Cyan-14-Bold.cfg`, and `Cyan-16.cfg` from
`src/h1x0/.rockbox/themes/` into the same directory on the test player.

Use the same list position and viewing conditions for each profile. Change only
the theme file through `Settings → Theme Settings → Browse Theme Files`:

1. Load `Cyan-14.cfg` and record the baseline.
2. Load `Cyan-14-Bold.cfg` and compare stroke weight, inverse-row clarity, and
   long-name legibility.
3. Load `Cyan-16.cfg` and compare viewing-distance legibility, clipping, and
   whether six complete rows still render cleanly.
4. Return to the preferred profile and repeat with the backlight off.

Do not alter font, line spacing, scrollbar, or icon settings between profiles;
each `.cfg` supplies the controlled comparison settings.

## Test Now Playing

This is the revised Milestone 2 physical gate. Milestone 2 passes only when
all eight checks below succeed on an H120/H140 with the backlight both on and
off. Record the Rockbox build, contrast setting, inversion setting, viewing
distance, and any parser or font error.

1. Start a track with complete title, artist, and album tags, then enter the
   While Playing Screen.
2. Confirm that title, artist, and album appear in descending type size and that
   long values scroll independently without crossing into adjacent regions.
3. Pause and resume. Confirm that the bottom-center icon changes between the
   larger play triangle and pause bars.
4. Hold rewind and fast-forward briefly. Confirm the corresponding double-arrow
   icons appear and the progress rail follows the seek position.
5. Confirm the five-pixel progress rail sits above elapsed/remaining time, no
   persistent volume text consumes the normal rail, and power remains graphical
   in the upper-right header.
6. Test a file with missing tags. Title should fall back to its filename;
   artist and album should show `Unknown Artist` and `Unknown Album`.
7. Repeat with the backlight off and from approximately 18, 24, and 30 inches.
8. Test the long-string and missing-tag cases shown in the browser proxy.
   Confirm every field stays within its viewport, the title falls back to the
   filename, and the artist/album fallbacks remain readable.

## Test playback states

1. Toggle repeat-all, repeat-one, and off. Confirm the repeat mark appears
   only for the two active modes and that repeat-one is distinguishable.
2. Toggle shuffle. Confirm its crossing-arrow mark appears only when enabled
   and does not crowd the centered playback or repeat marks.
3. Hold rewind and fast-forward. Confirm the progress rail becomes a seek rail
   whose diamond protrudes one pixel above and below the progress line, with
   enough surrounding white space to remain distinct, then returns.
4. Adjust volume. Confirm the lower rail temporarily becomes a wide meter,
   hides all normal rail indicators, and returns to the normal playback/mode or
   sleep state about two seconds after release.
5. Observe several battery levels. Confirm the compact icon reads as a battery,
   its terminal remains visible, and the discrete fill increases correctly.
6. Connect power and confirm the charging mark replaces the level icon while
   charging. Record whether the H120 reports charging state correctly.
7. Engage the main Hold switch. Confirm the compact padlock appears without
   displacing the current metadata, progress, or centered playback icon, then
   disappears when Hold is released.
8. Start a sleep timer. Confirm the compact `Zzz` mark appears only while the
   timer is active and disappears after cancellation.
9. Set repeat A-B and confirm its range mark is distinguishable from repeat-all
   and repeat-one.
10. Play through the final seven seconds of a track. Confirm the album line
    calmly changes to `UP NEXT//` plus the next title/artist while the current
    title and artist remain unchanged. On the last playlist item, confirm the
    album remains instead of showing an empty next-track cue.

These ten checks are the revised Milestone 3 physical gate. Run them with the
backlight on and off; repeat Hold and charging checks on the actual player
rather than relying on the browser proxy.

## Test native Track Info

1. While a tagged track is playing, press `ON + MODE` from Now Playing.
2. Confirm playback continues and the header reads `[ TRACK//INFO ]`.
3. Confirm the screen uses compact 12-Terminus rows, `>>`/`::` TUI prompts,
   and the `META//NATIVE` / `LEFT:BACK` footer rather than the normal browser
   treatment.
4. Scroll through the complete native list. Check title, artist, album,
   codec/format, bitrate, sample frequency, ReplayGain, file size, and path.
   Rockbox should omit unavailable values rather than showing empty fields.
5. Change tracks while Track Info remains open and confirm the native list
   refreshes to the new track.
6. Press `LEFT` or `OFF` and confirm Cyan's Now Playing screen returns.
7. Confirm short `REC` retains the user's existing WPS-hotkey behavior. Cyan//
   must not silently reassign it. Optionally assign `Show Track Info` through
   `Settings → General Settings → WPS → WPS Hotkey` and verify short `REC` as
   an alternate entry path.

## Test native playback-support lists

Together with the Track Info checks above, this is the revised Milestone 4
physical gate. Run every surface with the backlight on and off and confirm that
Cyan changes presentation only—not native data, actions, or navigation.

1. Open Current Playlist and confirm the header reads `QUEUE//`, every visible
   row has a `%LN` number, `NOW>` follows the firmware's current-track callback,
   and a different selected row remains full-width inverse with `>>`.
2. Open Playlist Catalogue and confirm `PLAYLISTS//` appears without changing
   playlist names or actions.
3. Long-press `SELECT` from Now Playing to open the Context Menu. Confirm the
   header reads `ACTION//`, native actions are unchanged, and selected/unselected
   rows use `>>`/`::` prompts.
4. Open Shortcuts and confirm `SHORTCUTS//` uses the same command-palette row
   language while all user-defined shortcut names and actions remain intact.
5. Exercise scrolling, cancel/back, and selection in all four screens. Confirm
   no duplicated rows, stale headers, `ERR` text, or broken actions.

## Test FM and recording instrumentation

This is the revised Milestone 5 physical gate. Browser renders are not evidence
for tuner reception, recording-meter refresh, clipping, or digital I/O.

1. Open FM Radio and confirm `[ RADIO//RX ]`, left-aligned `FREQ//`, labeled
   native RSSI rail, power, mode, lock/search, stereo/mono, tactical state
   icons, and RX live/muted update without `ERR`.
2. Test a named preset and an unnamed frequency. Confirm the preset name appears
   only when supplied by Rockbox and that Cyan never invents an RDS name.
3. Scan across the regional band and confirm the RSSI rail follows real signal
   strength rather than frequency position; lock/search and stereo/mono must
   update without stale icons.
4. Mute/unmute FM and move between stereo and weak mono reception. Confirm the
   state cells update without stale text.
5. Open Recording with Mic, Line, and FM sources where available. Confirm the
   bracketed `[ RECORD//SOURCE ]` header, active/pause glyph, `REC//` time,
   rate/encoder/channel footer, size, filename, settings list, and native L/R
   meters agree with Rockbox.
6. Start, pause, resume, split, and stop a short disposable recording. Confirm
   native meters, pause, clipping/trigger, AGC, and filename behavior remain
   functional and no Cyan viewport covers a control.
7. Select S/PDIF input. Confirm `SPDIF` appears in the bracketed header and the
   native live input sample rate appears. Do not interpret source selection as
   proof of signal lock.
8. Toggle Rockbox's S/PDIF output setting and confirm `/OUT` follows the real
   setting exactly. Verify optical input/output behavior with appropriate
   external equipment if available.
9. Repeat FM and recording checks with the backlight on/off and LCD inversion
   on/off. Record Rockbox build, source, format, sample rate, and failures.

## Test the 128×64 remote

This is the Milestone 6 physical gate. The browser proxy verifies composition,
not remote-LCD packing, button handling, scroll timing, or the two physical
Hold reports.

1. Connect a compatible H1x0 LCD remote, boot Rockbox, load `Cyan.cfg`, and
   confirm the remote opens `Cyan.rwps` without a parser or missing-font error.
2. Start a tagged track. Confirm battery, title, artist, progress,
   elapsed/remaining time, centered playback icon, and state word all
   fit the native 128×64 display with no clipped pixels.
3. Pause, resume, fast-forward, and rewind. Confirm the icon and state word
   change together and progress continues to follow Rockbox.
4. Test long-title, long-artist, and missing-title cases. Confirm each metadata
   row scrolls independently and the filename fallback remains usable.
5. Engage only the main-unit Hold switch and confirm the main-lock glyph plus
   `M.HOLD`. Release it,
   engage only the remote Hold switch, and confirm `R.HOLD`. If both can be
   engaged, confirm `R.HOLD` takes display priority while both locks still work.
6. Enter Files, Database, Settings, Current Playlist, and Track Info from the
   remote. Where Rockbox uses the RSBS, confirm five ten-pixel rows, native
   context in the header, a full-width inverse selected row, `>>` prompt,
   and battery.
7. Verify remote list navigation, select, cancel/back, and scrolling. Cyan must
   not replace any native list data or action.
8. Open FM and confirm the RFMS shows frequency, preset, real RSSI rail,
   tuning/stereo state, audio live/muted state, and power without clipping.
9. Repeat with remote backlight on/off and remote LCD inversion on/off. Record
   the Rockbox build, remote model, contrast, and any screen that does not use
   the RSBS.

Milestone 6 is physically complete only after this gate passes on a real
remote. No compatible remote is listed in `HARDWARE.md`, so the repository
currently records this validation as pending.

## Test utility surfaces

This is the Milestone 7 physical gate. Test native behavior as carefully as
the surrounding Cyan chrome; browser samples are not proof of live data.

1. Assign four legal but visibly different QuickScreen settings through normal
   Rockbox menus. Open QuickScreen and confirm `QUICK//`, battery, all four
   native setting names/values, directional arrows, four short datum rails, and
   the compact N/S/W/E footer fit without overlap or `ERR`. Change every
   direction and confirm only the intended setting changes. Cyan must not
   replace the user's assignments.
2. Open a Setting Chooser such as Repeat. Confirm the header preserves the
   native title after `CONFIG /`, the selected value is full-width inverse with
   `>>`, other values use `::`, and Select applies the native value.
3. Open Rockbox Info. Confirm `[ SYSTEM//INFO ]`, `::` dense native rows, and
   the `DATA//LIVE` / `SELECT:REFRESH` footer expose the
   real battery/time estimate, buffer size, recording/root paths, Rockbox
   version, and internal-disk free/total data. Scroll the complete list and
   press Select to exercise Rockbox's native refresh action.
4. Open the Bookmark Browser. Confirm `BOOKMARKS//`, unchanged bookmark text,
   strong selection, resume behavior, cancel, and long-row scrolling.
5. Open the Plugin Browser. Confirm `TOOLS//`, native categories and plugin
   names, command-palette selection, and normal launch/cancel behavior.
6. Launch Pitch. On a current build, confirm `pitch_screen.rock` presents its
   native full-screen calibration controls and remains functional even though
   Cyan chrome is absent. Record the exact Rockbox build if `PITCH//` appears,
   since that indicates a different/legacy theme-integration route.
7. Confirm no Time/Date menu is offered on the reference H120 build. Do not
   treat the browser's `NO RTC` boundary card as an installable screen.
8. Launch at least one game, viewer, and application plugin. Confirm each
   plugin remains usable with its own rendering and that Cyan returns cleanly
   when the plugin exits to a native list.
9. Repeat QuickScreen, Setting Chooser, System Info, Bookmark Browser, and
   Plugin Browser with backlight on/off and LCD inversion on/off. Record any
   stale header, clipping, missing title, or changed native action.

Milestone 7 passes only when the five integrated surfaces preserve all native
behavior and the Pitch, no-RTC, and arbitrary-plugin boundaries match the
current build rather than the browser illustration.

## Run the full `%cs` coverage audit

This is the Milestone 8 source and physical-coverage gate.

1. Run `python3 tools/check-screen-coverage.py`. Confirm it reports exactly 17
   themed, two external, and one H120-unavailable category.
2. Use [`screen-matrix.md`](screen-matrix.md) as the checklist and visit every
   reachable category from 1 through 20 on the H120. Record the observed title,
   row/body owner, font, selection style, navigation, and return path.
3. For `%cs=11`, confirm current Pitch is plugin-owned or record the precise
   build if compatibility `PITCH//` chrome appears. For `%cs=14`, test multiple
   plugin types rather than assuming one runtime represents all plugins.
4. Confirm `%cs=17` is absent on the reference target. If a custom build makes
   it reachable, record its RTC implementation and test the conditional
   `CLOCK//` compatibility route rather than treating it as stock H120 behavior.
5. For every themed category, repeat at least one entry/exit cycle with
   backlight on/off. No category may produce an undocumented generic header,
   blank body, `ERR`, stale viewport, broken action, or lost return path.

Milestone 8's source audit passes when the checker succeeds. Its physical gate
passes only when all reachable categories have an observation and categories
11, 14, and 17 match their documented boundary classifications.

## Polish stress matrix

The Milestone 9 source/browser gate runs:

```sh
python3 tools/check-assets.py
python3 tools/check-screen-coverage.py
python3 tools/check-layout.py
./tools/package.sh
unzip -tq dist/Cyan-0.1.0-h1x0.zip
```

The browser preview's `?milestone=9` route covers long browser/WPS content,
low battery, charging, Hold, seek 0%/100%, volume, sleep, track transition,
inversion, FM, recording, and remote cases. These results do not satisfy the
following hardware procedure: real backlight, LCD inversion, controls, native
meters, tuner reception, power reporting, timing, and glance-distance
readability require the physical player.

Run every case with the backlight on and off. For long values, wait long enough
to confirm scrolling starts, remains clipped to its viewport, and completes a
readable cycle.

| Field | Test value |
|---|---|
| Artist | `The Presidents of the United States of America` |
| Artist | `Queens of the Stone Age` |
| Album | `Mellon Collie and the Infinite Sadness` |
| Album | `The Downward Spiral (Deluxe Edition)` |
| Track | `Everything in Its Right Place — Live at 01:05` |
| Track | `R.E.M. / 0 O / 1 l I / 5 S / (test)` |
| Browser title | a database or playlist title longer than 17 characters |
| Missing tags | filename fallback plus unknown artist and album |

Check at 18, 24, and 30 inches:

- no metadata crosses into the progress/time region
- upper-right battery never overlaps a scrolling context title
- progress fill and seek diamond remain distinct at 0%, 50%, and 100%
- all bottom icons share a visual center and remain separated
- inverse selection remains legible during fast scrolling
- punctuation and ambiguous glyph pairs remain distinguishable
- one-pixel rules remain visible without becoming dominant

## Expected screen

- bold context title at the top
- about six visible choices
- item text matching the selected 14, 14 Bold, or 16 Terminus profile
- selected row is full-width inverse and starts with `>>`
- normal unselected rows align beneath the semantic-icon column; dense
  technical rows retain `::`
- compact graphical battery in the upper-right header
- segmented bottom rule and functional action/state footer
- generated semantic icons where callbacks are reliable; no scrollbar

If the custom list does not render, the configured native inverse selector is
the intended fallback. Record exactly what appears instead of trying to repair
it on the device.

## Report-back checklist

Test once with the backlight on and once with it off, first while holding the
player and then at roughly 18, 24, and 30 inches.

- Readability: Rank 14, 14 Bold, and 16 for comfortable reading. In each, are
  `0/O`, `1/l/I`, `5/S`, slashes, parentheses, and punctuation distinct?
- Visible rows: How many complete choices appear? Is navigation practical?
- Truncation/scrolling: Try `The Presidents of the United States of America`,
  `Mellon Collie and the Infinite Sadness`, and a track title longer than the
  display width. What clips, scrolls, or overlaps?
- Selection clarity: Is the inverse row unmistakable? Is `>>` visible and
  aligned? Does selection remain clear while rapidly scrolling?
- Header: Does the context title remain correct in Files, Database, Settings,
  playlists, and context menus? Does the battery remain aligned at upper right?
- Backlight on: Is contrast strong and text stable at glance distance?
- Backlight off: Is the selected row still obvious? Does any text wash out?
- Footer: Is it useful and quiet, or does it steal too much vertical space?
- Now Playing hierarchy: Is the title immediately dominant, with artist second
  and album third? Does any line collide with another while scrolling?
- Playback state: Do play, pause, fast-forward, rewind, and stop icons render
  correctly without `ERR` or stale frames?
- Progress/status: Are the rail, times, transient volume meter, sleep time, and power readable without
  becoming a dashboard?
- Failures: Note any blank screen, `ERR`, malformed row, missing font, or theme
  load error and the exact Rockbox version shown under System information.

## Roll back

Load the previous theme from `Settings → Theme Settings → Browse Theme Files`.
To remove the release completely, reconnect USB and delete only:

- `/.rockbox/themes/Cyan.cfg`
- `/.rockbox/wps/Cyan.sbs`
- `/.rockbox/wps/Cyan.wps`
- `/.rockbox/wps/Cyan.fms`
- `/.rockbox/wps/Cyan.rfms`
- `/.rockbox/wps/Cyan.rwps`
- `/.rockbox/wps/Cyan.rsbs`
- `/.rockbox/wps/Cyan/playback.bmp`
- `/.rockbox/wps/Cyan/battery.bmp`
- `/.rockbox/wps/Cyan/charging.bmp`
- `/.rockbox/wps/Cyan/powered.bmp`
- `/.rockbox/wps/Cyan/disk.bmp`
- `/.rockbox/wps/Cyan/hold.bmp`
- `/.rockbox/wps/Cyan/repeat.bmp`
- `/.rockbox/wps/Cyan/shuffle.bmp`
- `/.rockbox/wps/Cyan/sleep.bmp`
- `/.rockbox/wps/Cyan/seek.bmp`
- `/.rockbox/wps/Cyan/remote-playback.bmp`
- `/.rockbox/wps/Cyan/remote-battery.bmp`
- `/.rockbox/wps/Cyan/remote-charging.bmp`
- `/.rockbox/wps/Cyan/remote-powered.bmp`
- `/.rockbox/wps/Cyan/remote-hold.bmp`
- `/.rockbox/wps/Cyan/remote-fm-state.bmp`
- `/.rockbox/wps/Cyan/fm-state.bmp`
- `/.rockbox/wps/Cyan/record-state.bmp`
- `/.rockbox/icons/Cyan-13.bmp`

If developer comparison profiles were copied separately, remove those three
additional `.cfg` files as well. No firmware file or music file is changed by
Cyan//.
