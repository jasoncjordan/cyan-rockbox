# Cyan// 0.1.0 final validation

This guide turns the remaining release gates into reproducible procedures. Run
CheckWPS first, then the H120 simulator, then the physical H120 matrix. Do not
rename the release candidate or submit it to the Rockbox theme site until every
required gate has a recorded pass.

The commands below use two task-specific paths. Replace them with absolute
paths on the validation computer:

```sh
export CYAN_REPO="/absolute/path/to/Cyan Rockbox"
export ROCKBOX_SRC="/absolute/path/to/rockbox-4.0"
```

## One-time host setup

Use the official Rockbox 4.0 source, not an arbitrary current checkout:

```sh
git clone --branch v4.0-final --depth 1 \
    https://github.com/Rockbox/rockbox.git "$ROCKBOX_SRC"
```

On this Mac, Apple Command Line Tools are not currently active and
`sdl2-config` is not installed. Install the command-line tools from a normal
interactive macOS session:

```sh
xcode-select --install
```

Accept the Apple installer dialog. After it completes, verify:

```sh
xcode-select -p
cc --version
make --version
```

For the simulator, install SDL2. If Homebrew is already installed:

```sh
brew install sdl2
sdl2-config --version
```

If native macOS setup is inconvenient, an Ubuntu VM is a suitable validation
host. Install the equivalent prerequisites there:

```sh
sudo apt update
sudo apt install build-essential git perl libsdl2-dev unzip
```

No ColdFire cross-compiler is required for CheckWPS or the UI simulator; both
are host tools. A cross-compiler is required only to build firmware for the
physical player, which Cyan// does not require.

## Gate 1: CheckWPS for `iriverh120`

1. Build the target-specific checker from Rockbox 4.0:

   ```sh
   mkdir -p "$ROCKBOX_SRC/build-h120-checkwps"
   cd "$ROCKBOX_SRC/build-h120-checkwps"
   ../tools/configure --target=iriverh120 --type=C
   make -j4
   ```

2. Run one verbose check over all six installable skins. Supplying the original
   source paths lets CheckWPS find each same-named bitmap directory:

   ```sh
   set -o pipefail
   ./checkwps.iriverh120 -vv \
       "$CYAN_REPO/src/h1x0/.rockbox/wps/Cyan.sbs" \
       "$CYAN_REPO/src/h1x0/.rockbox/wps/Cyan.wps" \
       "$CYAN_REPO/src/h1x0/.rockbox/wps/Cyan.fms" \
       "$CYAN_REPO/src/h1x0/.rockbox/wps/Cyan.rsbs" \
       "$CYAN_REPO/src/h1x0/.rockbox/wps/Cyan.rwps" \
       "$CYAN_REPO/src/h1x0/.rockbox/wps/Cyan.rfms" \
       2>&1 | tee "$CYAN_REPO/dist/checkwps-iriverh120.txt"
   ```

3. Pass criteria:

   - exit status is zero;
   - every file reports `WPS parsed OK`;
   - no parsing failure, invalid extension, missing bitmap, or unavailable
     feature appears in the log.

If the command fails, preserve the complete log and fix the skin source before
moving to the simulator. Do not treat a browser proxy as parser evidence.

## Gate 2: H120 UI simulator and genuine screenshots

1. Configure and build the Rockbox 4.0 H120 simulator:

   ```sh
   mkdir -p "$ROCKBOX_SRC/build-h120-sim"
   cd "$ROCKBOX_SRC/build-h120-sim"
   ../tools/configure --target=iriverh120 --type=S
   make -j4
   make fullinstall
   ```

   `fullinstall` populates the generated `simdisk` with a complete Rockbox
   installation, including fonts.

2. Build Cyan's clean install archive and merge it into the simulated disk:

   ```sh
   cd "$CYAN_REPO"
   ./tools/package.sh
   unzip -o dist/Cyan-0.1.0-h1x0.zip \
       -d "$ROCKBOX_SRC/build-h120-sim/simdisk"
   ```

3. Put at least two tagged test tracks in `simdisk/Music/`. Include one with
   long metadata and one with missing tags so scrolling, fallbacks, Up Next,
   Queue, and Track Info can be exercised.

4. Start the simulator from its build directory:

   ```sh
   cd "$ROCKBOX_SRC/build-h120-sim"
   ./rockboxui
   ```

5. In simulated Rockbox, open
   `Settings -> Theme Settings -> Browse Theme Files`, select `Cyan.cfg`, and
   inspect Files, Database, Settings, Now Playing, Current Playlist, Track
   Info, FM, Recording, QuickScreen, and the utility lists. The simulator may
   not provide meaningful tuner reception, recording I/O, charging, disk, or
   physical contrast; those remain device checks.

6. Press `F5` while the simulator has focus to create a main-LCD screendump.
   Rockbox numbers these as `dump_0001.bmp`, `dump_0002.bmp`, and so on. Locate
   them if necessary:

   ```sh
   find "$ROCKBOX_SRC/build-h120-sim/simdisk" -name 'dump_*.bmp' -print
   ```

7. Capture at minimum Now Playing and a representative Cyan list. Convert the
   BMP dumps without resizing them. On macOS:

   ```sh
   sips -s format png \
       "$ROCKBOX_SRC/build-h120-sim/simdisk/dump_0001.bmp" \
       --out "$CYAN_REPO/docs/screenshots/cyan-wps-simulator.png"
   sips -s format png \
       "$ROCKBOX_SRC/build-h120-sim/simdisk/dump_0002.bmp" \
       --out "$CYAN_REPO/docs/screenshots/cyan-menu-simulator.png"
   sips -g pixelWidth -g pixelHeight \
       "$CYAN_REPO/docs/screenshots/cyan-wps-simulator.png"
   ```

   Both main-display images must remain exactly 160×128. Keep the existing
   `browser-proxy` files clearly labeled; genuine simulator captures are new
   evidence and do not retroactively make the proxies official screenshots.

8. Pass criteria:

   - Cyan loads with no `ERR`, parser, missing-font, or missing-image message;
   - all reachable surfaces retain native actions and return paths;
   - metadata, prompts, icons, rails, headers, and footers fit their viewports;
   - the two genuine 160×128 PNG files are visually reviewed and retained.

## Gate 3: physical H120 validation

1. Record the player and environment before installation:

   - exact Rockbox version/build;
   - H120 or H140 model;
   - LCD contrast and inversion settings;
   - optional font-pack presence;
   - available compatible LCD remote, if any.

2. Back up the current theme name and `/.rockbox/config.cfg`. Build the archive
   with `./tools/package.sh`, install it using
   [`installation.md`](installation.md), cleanly eject the player, and load
   `Cyan.cfg` through Theme Settings.

3. Run [`testing.md`](testing.md) in order. At minimum, cover:

   - Files, Database, Settings, and long selected rows;
   - normal playback, pause, seek endpoints, volume takeover, Up Next, Hold,
     repeat, shuffle, sleep, power, charging, and disk activity;
   - Queue, native Track Info, Context Menu, Playlist Catalogue, and Shortcuts;
   - real FM reception/RSSI and a disposable Mic/Line/FM recording;
   - QuickScreen, Setting Chooser, Rockbox Info, Bookmarks, Plugin Browser,
     Pitch, and representative plugins;
   - all reachable `%cs` categories in `screen-matrix.md`.

4. Repeat the readability and high-risk state checks with:

   - backlight on and off;
   - LCD inversion on and off;
   - viewing distances of approximately 18, 24, and 30 inches;
   - long titles, artists, albums, paths, settings, and queue entries.

5. For each failure, record the screen, state, exact text, lighting, contrast,
   inversion, and a photo if useful. A physical photo is supporting evidence;
   the exact 160×128 theme-site screenshot should come from the simulator.

6. Pass criteria:

   - no parser/font/image errors, blank bodies, stale viewports, or broken
     native actions;
   - all user choices remain readable at the agreed viewing distances;
   - live FM, recording, power, Hold, disk, and transient playback states
     match firmware state;
   - long strings scroll or clip only inside their assigned viewport;
   - backlight-off and inversion checks remain legible.

The compatible LCD remote remains a separate required release gate because
`HARDWARE.md` lists no remote. A main-unit physical pass does not silently
convert that missing-hardware check into a pass.

## Record the result

Add the following block to the release notes or validation issue after each
run:

```text
Rockbox source/tag: v4.0-final
CheckWPS: PASS/FAIL, log path:
Simulator: PASS/FAIL, host OS:
WPS capture: path, 160x128 verified YES/NO
Menu capture: path, 160x128 verified YES/NO
Physical player: H120/H140, Rockbox build:
Backlight/inversion matrix: PASS/FAIL
FM/recording/live-state matrix: PASS/FAIL
Remote: PASS/FAIL/NOT TESTED, model:
Open defects:
Tester/date:
```
