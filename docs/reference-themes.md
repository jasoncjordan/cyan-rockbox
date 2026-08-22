# Reference-theme inventory

Research was performed from the original archives in `reference/`; those files
were not modified. Bitmap dimensions below are the encoded sheet dimensions,
so vertically stacked state strips can be much taller than one displayed icon.

## Gray (`reference/gray.zip`)

Gray is an H120-era 160×128 theme and the direct comparison baseline.

- Main dependencies: `gray.cfg`, `gray.wps`, `gray.rwps`, two 160×128
  backgrounds, a bundled font, two Tango icon sheets, and 18 WPS bitmap sheets.
- The configured browser font is **`12-Adobe-Helvetica.fnt`**.
- Browser selector: `bar (inverse)`; native status bar off; backdrop enabled.
- The WPS uses a full-screen backdrop and bitmap strips for volume (10 states),
  battery (10), play mode (5), repeat (4), codec (22), shuffle, lock, encoding,
  and progress.
- Useful pattern: proven H120 paths, grayscale BMP assets, and inverse selector.
- Cyan// change: retain the robust native inverse fallback, remove the crowded
  icon/backdrop dependence, and move browser type to 14-Terminus.

## mind (`reference/mind.zip`)

mind is a 2020 H120/H140 theme and the most useful base-skin reference.

- Main dependencies: `mind.cfg`, `.wps`, `.sbs`, `.fms`, two Tango icon sheets,
  two 160×128 4-shade backgrounds, and battery/volume/play/repeat/shuffle/progress
  strips.
- Browser font: `12-Sazanami-Mincho.fnt`; SBS additionally loads 14 Adobe
  Helvetica Bold, 12 Sazanami Mincho, and 12 Adobe Helvetica.
- The SBS uses `%VI`/`%Vi` to reserve a 152×111 UI viewport and a bottom status
  rail. This is the known-good H120 mechanism reused conceptually by Cyan//.
- Useful pattern: H120-specific SBS geometry and compact conditional status.

## ipodVOL (`reference/ipodVOL.zip`)

ipodVOL is a small 160×128 example with minimal dependencies.

- Main dependencies: `ipodVOL.cfg`, `ipodVOL.wps`, one 160×128 1-bit
  background, and battery/play/repeat/hold strips.
- Configured font: `12-Nimbus.fnt`; built-in status bars enabled.
- Useful pattern: tiny one-bit state strips and a very small package.
- Not reused visually because the Cyan// brief explicitly rejects iPod styling.

## CoverMax-XXL (`reference/CoverMax-XXL.zip`)

CoverMax-XXL is a recent 160×128 skin-engine example (revision 5, 2024).

- Main dependencies: `.cfg`, `.wps`, `.sbs`, padded 14-Nimbus font, a 3-pixel
  icon sheet, and nine state/indicator sheets.
- Uses `%Fl`, named viewports, `%VI`/`%Vi`, `%dr`, modern logical conditionals,
  numeric/graphic battery alternatives, and temporary volume state.
- Useful pattern: current syntax, restrained top status design, and conditional
  viewport composition.
- Not used as a browser layout base because its 108-pixel content viewport and
  iPod-labelled header pursue different priorities.

## Cabbiev2 (current Rockbox source)

The Rockbox `WPSLIST` still defines Cabbiev2 as an official multi-resolution
theme and maps the 160×128×2 family to a dedicated WPS and FMS while selecting
`12-Adobe-Helvetica.fnt`. It also maps the H1x0 remote's 128×64×1 resolution to
a compact WPS and `08-Rockfont.fnt`. It does not provide an SBS. It is useful
as a current packaging, FM, and remote-layout reference, but not as the
Milestone 1 browser base.

The current 160×128×2 FMS demonstrates a frequency bar, scan/preset and
mono/stereo conditions, signal strength, preset navigation with `%Vp`, and RDS
text without replacing the native tuner. The 128×64×1 WPS demonstrates a
remote-sized information hierarchy and compact lock, battery, volume, shuffle,
repeat, and play-state rail.

Sources: [Rockbox `wps/WPSLIST`](https://github.com/Rockbox/rockbox/blob/master/wps/WPSLIST),
[Cabbiev2 160×128×2 FMS](https://github.com/Rockbox/rockbox/blob/master/wps/cabbiev2-160x128x2.fms),
and [Cabbiev2 128×64×1 WPS](https://github.com/Rockbox/rockbox/blob/master/wps/cabbiev2.128x64x1.wps).

## Additional implementation-reference map

Milestone 0 also audited current upstream implementation references that are
not supplied as theme archives:

| Need | Verified reference | What it establishes |
|---|---|---|
| Skinnable-screen boundary | [`skin_engine.h`](https://github.com/Rockbox/rockbox/blob/master/apps/gui/skin_engine/skin_engine.h) | Only SBS, WPS, and FM are dedicated skin classes. Other screens retain native bodies. |
| Lists and contextual chrome | [Current tag appendix](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex) | `%Lt`, `%LT`, `%Lb`, `%Lc`, `%cs`, conditional viewports, and line styling. |
| QuickScreen | [Current tag appendix](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex) | Four native name/value pairs: `%QT/%Qt`, `%QR/%Qr`, `%QB/%Qb`, and `%QL/%Ql`. No maintained bundled theme example was found, so later work must follow the documented tags and pass simulator/CheckWPS validation. |
| FM | [Cabbiev2 FMS](https://github.com/Rockbox/rockbox/blob/master/wps/cabbiev2-160x128x2.fms) | Maintained 160×128×2 use of tuner, RDS, signal, bar, and preset-viewer tags. |
| Remote | [`WPSLIST`](https://github.com/Rockbox/rockbox/blob/master/wps/WPSLIST) and [128×64×1 WPS](https://github.com/Rockbox/rockbox/blob/master/wps/cabbiev2.128x64x1.wps) | Remote package selection and a maintained one-bit layout at the H1x0 remote resolution. |
| Recording and utilities | [`skin_engine.h`](https://github.com/Rockbox/rockbox/blob/master/apps/gui/skin_engine/skin_engine.h) and [target config](https://github.com/Rockbox/rockbox/blob/master/firmware/export/config/iriverh120.h) | Hardware support is real, but recording, Pitch, System Info, and similar screens are not independent theme files. |
| Package roles | [`WPSLIST`](https://github.com/Rockbox/rockbox/blob/master/wps/WPSLIST) | Current WPS/RWPS/SBS/RSBS/FMS/RFMS naming and resolution selection. |

## Resulting Milestone 1 approach

Use the path/config conventions proven by Gray, the H120 SBS/UI-viewport model
proven by mind, and the current documented skin tags demonstrated by
CoverMax-XXL and Rockbox source. Do not copy any bitmap asset. Cyan// Milestone 1
is text-driven and has no image dependency.
