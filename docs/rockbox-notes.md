# Current Rockbox theme notes

Research snapshot: 2026-08-20, against Rockbox mirror commit
[`11817f99`](https://github.com/Rockbox/rockbox/tree/11817f99f80492ae9990e625828d7a161aea9928).
Official manual source and current Rockbox source are used as the authority.

## Target facts

The current `iriverh120` target covers H120/H140. Its main display is 160×128,
2-bit grayscale with vertical packing; its remote is 128×64, 1-bit. The config
also confirms LCD inversion, backlight, battery reporting, recording, FM, and a
remote display. [Current target config](https://github.com/Rockbox/rockbox/blob/11817f99f80492ae9990e625828d7a161aea9928/firmware/export/config/iriverh120.h).

## Files and installation paths

- Theme configuration: `/.rockbox/themes/Cyan.cfg`
- Base skin for menus/browsers: `/.rockbox/wps/Cyan.sbs`
- Main playback/radio skins: `/.rockbox/wps/Cyan.wps` and `Cyan.fms`
- Remote skins: `/.rockbox/wps/Cyan.rwps`, `Cyan.rsbs`, and `Cyan.rfms`
- Main and remote one-bit images: `/.rockbox/wps/Cyan/`
- Fonts: `/.rockbox/fonts/*.fnt`

The manual requires the `.cfg` in `themes`, skin files in `wps`, matching theme
names, UTF-8 text, and same-named image subdirectories. Fonts loaded at startup
belong in `/.rockbox/fonts`; the documented filename limit is 24 characters.
[Official customization manual source](https://github.com/Rockbox/rockbox/blob/11817f99f80492ae9990e625828d7a161aea9928/manual/advanced_topics/main.tex).

The repository source mirrors this install tree under `src/h1x0/.rockbox/`.
That differs from the PRD's flat illustrative `src/h1x0` layout because the
install tree makes packaging auditable and eliminates path-rewrite steps.

## `.cfg` controls relevant to Milestone 1

The current config-file appendix accepts `font`, `sbs`, `statusbar`,
`scrollbar`, `scrollbar width`, `selector type`, `show icons`, `iconset`,
`viewers iconset`, `backdrop`, and `ui viewport`. On a grayscale target the
selector choices are `pointer` and `bar (inverse)`; color-only selector modes do
not apply. [Official config options](https://github.com/Rockbox/rockbox/blob/11817f99f80492ae9990e625828d7a161aea9928/manual/appendix/config_file_options.tex).

Implication: a plain `.cfg` cannot request the native pointer and inverse bar at
the same time. `selector type: bar (inverse)` is therefore the fallback, not the
complete Cyan// selection design.

## Native skin boundary and remote roles

The current skin engine defines only `CUSTOM_STATUSBAR`, `WPS`, and—when a
tuner exists—`FM_SCREEN` as independent skinnable screens. A `%cs` condition
can identify many more native screens, but it does not make their bodies
replaceable. Recording, QuickScreen, Pitch, System Info, Track Info, and other
utility screens therefore keep Rockbox's native behavior and data; Cyan can
provide SBS/list styling and conditional chrome around them.

For remote-capable targets, the configuration format provides `rwps` plus
remote status-bar, font, viewport, icon, contrast, inversion, backlight, and
scroll settings. Rockbox's current theme build metadata additionally recognizes
RSBS and RFMS package roles. The maintained Cabbiev2 definition maps the H1x0
remote resolution, 128×64×1, to its compact WPS. Cyan now follows that native
route with `Cyan.rwps`, `Cyan.rsbs`, `10-ProFont.fnt`, and `remote statusbar:
off`. Its remote bitmaps are separately sized one-bit assets; the 160×128 main
layout is never scaled. `%mr` reports remote Hold while `%mh` reports main-unit
Hold, allowing the two locks to remain explicitly distinct.

[Current skinnable-screen enum](https://github.com/Rockbox/rockbox/blob/master/apps/gui/skin_engine/skin_engine.h),
[official config options](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/config_file_options.tex),
and [current theme build metadata](https://github.com/Rockbox/rockbox/blob/master/wps/WPSLIST).

## SBS and skinned lists

An SBS is the base skin shown around menus and browsers. `%Vi` declares a custom
UI viewport; `%VI` selects it. If `%Lt` appears in the SBS, the theme is
responsible for drawing list titles itself.

The documented skinned-list mechanism provides:

- `%Lb(viewport,width,height)` to draw each item with a labelled viewport
- `%Lc` to test whether the current item is selected
- `%LT` for item text
- `%Vs(invert)` and `%Vs(clear)` for line styles

Cyan// uses these supported tags to draw a full-width inverse row and a literal
escaped `>` only for the selected item. Six 16-pixel rows fit the 96-pixel list
viewport. `selector type: bar (inverse)` remains in the `.cfg` so Rockbox's
native list renderer still has a strong selection if the custom list cannot be
drawn. [Official skin-tag appendix](https://github.com/Rockbox/rockbox/blob/11817f99f80492ae9990e625828d7a161aea9928/manual/appendix/wps_tags.tex) and [current legal tag table](https://github.com/Rockbox/rockbox/blob/11817f99f80492ae9990e625828d7a161aea9928/lib/skin_parser/tag_table.c).

## Fonts and viewports

Font IDs 0 and 1 are reserved; extra fonts loaded with `%Fl` start at 2. Cyan//
sets 14-Terminus as the global UI font, then loads 14-Terminus-Bold as font 2
for the header and 12-Terminus as font 3 for the footer. The fonts exist in the
physical device's captured optional-font-pack inventory.

The Milestone 1 screen is divided into a 16-pixel header, 96-pixel list UI
viewport, and 16-pixel footer. This explicitly documents the otherwise
unavoidable H120 pixel coordinates.

## Native Track Info integration

Rockbox identifies Track Info as current-screen value 20 through `%cs` and
implements it as a standard `gui_synclist`. Cyan// conditionally selects a
12-Terminus UI viewport and 12-pixel list-item template for that screen while
leaving the native list and metadata callbacks intact. The native screen
provides title, artist, composer, album, album artist, grouping, disc and track
number, comment, genre, year, length, playlist position, codec/format, bitrate,
sample frequency, track and album gain, file size, path, date, and time; fields
without values are omitted by Rockbox.

On H1x0, `ON + MODE` maps directly to `ACTION_WPS_ID3SCREEN`, short `REC` maps
to the configurable WPS hotkey, and `LEFT` or `OFF` is the standard cancel
action. Cyan// does not write `context_wps` in its theme configuration, so the
user's hotkey remains untouched. “Show Track Info” may be assigned manually
under `Settings → General Settings → WPS → WPS Hotkey`.

[Current Track Info implementation](https://github.com/Rockbox/rockbox/blob/master/apps/screens.c),
[H1x0 keymap](https://github.com/Rockbox/rockbox/blob/master/apps/keymaps/keymap-h1x0_h3x0.c),
and [theme-tag appendix](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex).

## WPS, images, bars, and status conditions used in Milestones 3–4

Current supported mechanisms include `%xl` bitmap-strip preloading, `%xd`
sub-image display, `%mp` playback-state conditionals, `%pb` playback progress,
`%pv` volume, `%bl` battery level, `%bp` external power, `%bc` charging, and
logical `%if`/`%and`/`%or`. Images must be BMP; an image strip is tiled
vertically into equal-height states.

`Cyan.wps` now uses `%xl`/`%xd` with `%mp` for five playback-state frames,
native `%pb` and `%bl` bars for progress and battery, and the text value of
`%pv` for compact dB volume. The metadata fallbacks use documented conditionals
around `%it`, `%ia`, and `%id`. The current Rockbox Cabbiev2 160×128 grayscale
WPS confirms the same image-strip, playback conditional, progress, time, and
viewport patterns in a maintained target layout.
[Current Cabbiev2 H1x0-sized WPS](https://github.com/Rockbox/rockbox/blob/master/wps/cabbiev2.160x128x2.wps).

All status bitmaps are generated by `tools/generate-assets.py` from documented
pixel primitives. The playback strip has five vertical 11×11 frames. The battery
strip has six 18×7 frames and a terminal silhouette; charging, repeat,
repeat-one, shuffle, and seek each use purpose-built one-bit assets. This keeps
the editable source separate from packaged BMPs.

The playback-state work uses `%mm` for repeat-all, repeat-one, and A-B modes;
`%ps` for shuffle; `%bc` for charging; `%mh` for main Hold; `%bs` for an active
sleep timer; and `%mv(2)` for a temporary volume-adjustment viewport.
Fast-forward and rewind select a taller `%pb` rail with a diamond slider and
directional header through `%mp`. `%pE(7)` exposes Up Next only during the last
seven seconds, using `%It`, `%Ia`, and `%Fn` while retaining the current title
and artist. Rockbox exposes no Hold-activation timeout, so the theme shows a
compact active lock rather than an unreliable simulated transient. These
mechanisms and option order are documented in the current theme-tag appendix
linked above.

## FM and native recording instrumentation

FM is an independent skinnable screen. `Cyan.fms` and `Cyan.rfms` use the
current tuner tags for frequency, real RSSI, preset identity, scan/preset,
tuned/search, stereo/mono, RDS when available, signal strength, and playback
mute state.

Recording is not an independent skin class. The current recorder creates its
own top and list viewports, draws live L/R peak meters, and owns time, size,
filename, clip/trigger, gain, AGC, pause, and S/PDIF sample-rate behavior. Cyan
uses `%cs=3` only to select dense SBS geometry. Firmware recording tags expose
state/time (`%Rr`, `%Rh`, `%Rn`, `%Rs`), actual sample rate (`%Rf`), encoder
(`%Re`), and mono/stereo (`%Rm`); settings tags retain source and S/PDIF output
state. This does not claim S/PDIF signal lock or quality.

[Current recorder source](https://github.com/Rockbox/rockbox/blob/master/apps/recorder/recording.c),
[current setting definitions](https://github.com/Rockbox/rockbox/blob/master/apps/settings_list.c),
and [current skinnable-screen enum](https://github.com/Rockbox/rockbox/blob/master/apps/gui/skin_engine/skin_engine.h).

## Utility surfaces and current plugin boundaries

QuickScreen pushes `ACTIVITY_QUICKSCREEN`, enables the themed viewport through
`viewportmanager_theme_enable`, and then draws the user's four assigned setting
names, values, and arrows inside that UI viewport. Cyan can therefore provide
`QUICK//` chrome and dense geometry without duplicating its interaction logic
or forcing `qs top/bottom/left/right` settings.

Setting Chooser, System Info, Bookmark Browser, and Plugin Browser use native
list/simple-list routes and can receive Cyan headers and row templates. System
Info currently supplies battery/time, buffer size, recording and root paths,
Rockbox version, and volume free/total data; Cyan does not reconstruct these
values with skin tags.

Current master no longer implements Pitch as a core themed screen body. The
core loader launches `pitch_screen.rock`; the plugin draws directly through
plugin viewports and its activity calls are commented out. As a result, the
manual's `%cs=11`/`%Sp` route is retained only as compatibility chrome, not
claimed as current H120 Pitch theming. Arbitrary plugin runtimes have the same
theme-external ownership. The H120 target also lacks `CONFIG_RTC`, so the
Time/Date screen is unreachable even though `%cs=17` remains a global category.

[Current QuickScreen implementation](https://github.com/Rockbox/rockbox/blob/master/apps/gui/quickscreen.c),
[current Pitch loader](https://github.com/Rockbox/rockbox/blob/master/apps/gui/pitchscreen.c),
[current Pitch plugin](https://github.com/Rockbox/rockbox/blob/master/apps/plugins/pitch_screen.c),
and [current System Info implementation](https://github.com/Rockbox/rockbox/blob/master/apps/menus/main_menu.c).

## Simulator and validation

Current Rockbox source can configure the H120 UI simulator non-interactively:

```sh
mkdir build-h120-sim
cd build-h120-sim
../rockbox/tools/configure --target=iriverh120 --type=S
make
```

The simulator build requires a host compiler and SDL as detected by
`tools/configure`. Copy the prototype `.rockbox` tree into the generated
`simdisk`, run `./rockboxui`, and load Cyan from Theme Settings. The simulator
is valuable for parser/layout iteration but cannot judge LCD contrast, physical
pixel size, or the blue backlight.

CheckWPS can be configured with `--type=C` for the same target:

```sh
mkdir build-h120-checkwps
cd build-h120-checkwps
../rockbox/tools/configure --target=iriverh120 --type=C
make
```

This repository does not vendor Rockbox source or its host toolchain. The exact
Rockbox 4.0 CheckWPS, H120 simulator, screendump, and physical-device procedures
are maintained in [`final-validation.md`](final-validation.md). Browser proxies
remain design evidence, not parser or firmware proof. [Rockbox 4.0 configure
script](https://github.com/Rockbox/rockbox/blob/v4.0-final/tools/configure).

Milestone 0 assessment: the simulator and CheckWPS routes are viable and the
exact H120 build targets are known, but neither can be executed from this
repository alone. Validation uses the official `v4.0-final` source, a host
compiler, and SDL2 for the UI simulator. `make fullinstall` supplies the
simulated Rockbox tree and fonts before the Cyan archive is merged into it.

## Theme-site packaging (future)

The current official theme-site implementation expects a main ZIP, validates it
with CheckWPS, requires a WPS screenshot at exact LCD dimensions, accepts an
optional menu screenshot, and applies CC BY-SA 3.0 to uploads. Formal theme-site
submission is revised Milestone 10, not part of the current development snapshot.
[Official upload implementation](https://github.com/Rockbox/themesite/blob/master/www/upload.php) and [upload form](https://github.com/Rockbox/themesite/blob/master/private/templates/upload.tpl).
