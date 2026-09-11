# Product Requirements Document

# Cyan//

## A maximalist TUI/cyberpunk Rockbox theme for the iRiver H120/H140

---

## 1. Product Summary

**Cyan//** is a comprehensive Rockbox theme and visual system initially designed for the **iRiver H120/H140/H1x0 family**.

Its primary goals are:

1. Make the iRiver H120/H140 significantly easier to read for users who find traditional Rockbox themes too small or information-dense.
2. Give essentially every theme-addressable Rockbox screen a coherent, deliberately designed Cyan// treatment.
3. Exploit the unusually broad hardware capabilities of the iRiver H-series rather than designing only for generic music playback.
4. Combine modern information hierarchy with a strong TUI, terminal, UNIX-workstation, coding-agent, embedded-instrument, and restrained cyberpunk visual vocabulary.
5. Preserve native Rockbox behavior wherever possible rather than modifying firmware.
6. Eventually form a portable theme family for other classic Rockbox targets, while treating the H120/H140 implementation as the flagship edition.

Cyan// should feel like:

> A compact technical instrument from an alternate future where a high-end 2003 digital audio recorder evolved into a modern TUI-driven cyberdeck.

It must not feel like:

> An iPod clone.

It also must not feel like:

> A novelty “hacker skin” full of fake code and decorative telemetry.

---

# 2. Core Design Philosophy

Cyan// combines approximately:

- **40% modern Apple Music information hierarchy**
- **30% modern coding-agent / TUI interface**
- **20% late-1980s through early-2000s UNIX/workstation/embedded UI**
- **10% restrained cyberpunk**

Apple influence means:

- clear hierarchy
- large important text
- few competing information levels
- strong selected state
- understandable navigation
- restrained clutter
- useful whitespace

It does **not** mean:

- iPod menu structure
- classic Apple typography
- click-wheel visual conventions
- Apple chevrons
- skeuomorphic music-player imagery
- imitation of current iOS graphics

The TUI/coding-agent influence should come from:

- monospace typography
- compact status rails
- path/context headers
- panes
- terse labels
- key/value technical information
- strong selection state
- functional glyphs
- one-pixel rules
- dynamic state indicators
- concise command-like language

The cyberpunk influence should come from:

- hard geometry
- black/white/grayscale contrast
- the physical H120 blue backlight
- occasional `//` syntax
- compact machine-state displays
- technical instrumentation
- deliberate asymmetry where useful

Do not use:

- Matrix rain
- random hexadecimal values
- fake source code
- fake command execution
- meaningless blinking widgets
- pseudo-futuristic fonts
- excessive border boxes
- diagnostic clutter solely because it looks technical

---

# 3. Name and Identity

Theme name:

**Cyan//**

The name comes from:

1. the physical blue backlight of the iRiver H120/H140
2. classic cyan computer displays
3. CGA-era cyan/magenta associations
4. terminal/workstation aesthetics
5. a deliberate conceptual response to the existing Rockbox theme **Gray**

The main LCD remains grayscale.

Do not attempt to fake cyan through grayscale artwork.

The hardware backlight itself provides Cyan//'s signature physical color.

The `//` suffix is part of the identity and may occasionally appear in context labels such as:

```text
MUSIC//
QUEUE//
RADIO//
RECORD//
TRACK//INFO
SYSTEM//
```

Do not append `//` to every visible word.

---

# 4. Reference Hardware

Initial flagship target:

**iRiver H120/H140**

Relevant target capabilities include:

- 160×128 main LCD
- 2-bit grayscale display
- blue backlight
- LCD inversion capability
- 128×64 remote LCD
- FM tuner
- audio recording
- microphone input
- line input
- FM recording
- S/PDIF recording input
- S/PDIF output
- disk storage
- hardware charging
- QuickScreen
- configurable hotkey
- Hold state
- remote Hold state
- adjustable LCD contrast
- backlight fading
- battery voltage measurement
- playlist/database browsing
- Rockbox plugins

The H120/H140 must not be treated merely as another 160×128 music player.

Its additional capabilities are part of Cyan//'s identity.

---

# 5. User Priorities

Implementation priority remains:

## P0 — Daily-use core

1. Browser / database / file navigation
2. Primary Now Playing screen
3. Standard Rockbox menus/settings
4. Native Track Info integration

## P1 — High-value state and playback surfaces

5. Current Playlist / queue
6. transient volume interface
7. seek / fast-forward / rewind interface
8. FM Radio screen
9. Hold/lock state
10. repeat / shuffle / sleep / charging indicators
11. context-aware SBS headers

## P2 — H-series showcase functionality

12. remote WPS
13. remote list/menu treatment where possible
14. Recording screen
15. QuickScreen
16. Pitch screen
17. Setting chooser
18. System Info
19. Shortcuts
20. Bookmarks
21. Time/date
22. Playlist catalogue
23. context menus

## P3 — maximalist completion and polish

24. Plugin browser
25. plugin shell/chrome where themeable
26. disk activity indication
27. peak meters where useful
28. additional native screens exposed by current firmware
29. special state handling
30. future target ports

The priority controls **implementation order**, not final scope.

The desired final scope is maximalist.

---

# 6. Maximalist Scope Rule

Rockbox currently exposes a `%cs` Current Screen value representing 20 screen categories.

Cyan// should eventually intentionally address **all twenty**.

The currently documented categories are:

1. Menus
2. WPS
3. Recording screen
4. FM Radio screen
5. Current Playlist screen
6. Settings menus
7. File browser
8. Database browser
9. Plugin browser
10. QuickScreen
11. Pitch screen
12. Setting chooser
13. Playlist Catalogue Viewer
14. Plugin
15. Context menu
16. System Info screen
17. Time and Date screen
18. Bookmark browser
19. Shortcuts menu
20. Track Info screen

Before implementation, verify this list against the current upstream Rockbox documentation.

Do not assume the list will remain fixed forever.

If later Rockbox versions expose additional screen types, document and evaluate them.

The rule is:

> If Rockbox exposes a screen state to the skin system and Cyan// can improve its visual coherence without firmware modification, Cyan// should eventually address it.

---

# 7. Screen Identity System

Each major screen should have an optional concise Cyan// context label.

Suggested vocabulary:

| Rockbox screen | Cyan// label |
|---|---|
| Main menus | `SYSTEM//` or native list title |
| WPS | `NOW PLAYING` |
| Recording | `RECORD//` |
| FM Radio | `RADIO//` |
| Current Playlist | `QUEUE//` |
| Settings | `CONFIG//` |
| File Browser | `FILES//` |
| Database Browser | `MUSIC//` |
| Plugin Browser | `TOOLS//` |
| QuickScreen | `QUICK//` |
| Pitch Screen | `PITCH//` |
| Setting Chooser | contextual native title |
| Playlist Catalogue | `PLAYLISTS//` |
| Plugin | `PLUGIN//` when appropriate |
| Context Menu | `ACTION//` |
| System Info | `SYSTEM//INFO` |
| Time and Date | `CLOCK//` |
| Bookmark Browser | `BOOKMARKS//` |
| Shortcuts | `SHORTCUTS//` |
| Track Info | `TRACK//INFO` |

These labels are design starting points.

Do not replace useful native contextual information merely to display Cyan branding.

When Rockbox provides a meaningful list title, prefer combining or styling it rather than discarding it.

---

# 8. Typography

Use the official optional Rockbox font pack.

Primary design family:

**Terminus**

Starting assignments:

- Browser/menu list rows: `14-Terminus`
- Headers: `14-Terminus-Bold`
- Main WPS title: `18-Terminus-Bold`
- Artist: `16-Terminus`
- Album: `12-Terminus`
- Status/footer: `12-Terminus`
- Technical/diagnostic lists: `12-Terminus`
- Remote: determine best font from available sizes and remote constraints

Candidate alternatives:

- Terminus Bold
- Fixed
- Fixed-Bold
- Fixed-SemiCond
- ProFont

Use narrower fonts only when horizontal truncation materially harms usability.

Rules:

1. Remove low-value information before shrinking primary text.
2. Never reduce browser text merely to maximize row count.
3. Prefer approximately 5–8 useful visible rows on the main browser.
4. Use smaller text intentionally on technical screens where density is the purpose.
5. Test actual readability on the physical LCD.

---

# 9. Browser and List System

This remains Cyan//'s most important surface.

Primary selection concept:

**inverse full-width selected row + `>` prompt marker**

Example:

```text
MUSIC / ALBUMS

  Doolittle
> Dummy
  In Rainbows
  Mezzanine
  Violator
```

The selected item must be unmistakable.

Use Rockbox's list skin capabilities where practical.

Investigate:

- `%LT`
- `%LI`
- `%LN`
- `%LR`
- `%LC`
- `%Lc`
- `%LB`
- `%Lb`

These permit Cyan// to go beyond merely changing the font.

Potential capabilities include:

- custom numbered lists
- strong selected-item styling
- custom scrollbar
- list-row-specific formatting
- contextual list headers
- compact list icons

Design rule:

> Cyan// lists should feel like a modern TUI data navigator, not a generic Rockbox list with a large font.

---

# 10. Browser Header System

Preferred syntax:

```text
MUSIC / ALBUMS
```

Acceptable alternative:

```text
~/music/albums
```

Default preference:

**human-readable contextual labels over literal fake shell paths**

Examples:

```text
MUSIC / ARTISTS
MUSIC / ALBUMS
FILES / MUSIC
PLAYLISTS//
CONFIG / SOUND
```

Use uppercase for context labels.

Preserve original capitalization for user content.

---

# 11. Main Now Playing Screen

The primary WPS must remain visually disciplined despite the maximalist project scope.

The maximalist philosophy applies across the whole theme.

It does **not** mean putting everything on the WPS.

Primary hierarchy:

1. Track title
2. Artist
3. Album
4. progress
5. elapsed/remaining time
6. playback state
7. battery
8. active exceptional states

Conceptual layout:

```text
NOW PLAYING              ▶

WHERE IS MY MIND?
PIXIES
Surfer Rosa

03:18 ━━━━━━━●━━━ 03:53

                         ▰▰▰▱
```

Do not permanently show:

- codec
- bitrate
- sample rate
- file size
- filename
- replaygain
- path
- play count
- technical storage state

Those belong elsewhere.

---

# 12. Tactical Graphics

Cyan// is a hybrid TUI/graphic theme.

Use tiny bitmap graphics when they convey state more efficiently than text.

Preferred graphical targets:

- Play
- Pause
- Stop
- Fast-forward
- Rewind
- Seek
- Battery
- Charging
- Volume
- Shuffle
- Repeat
- Repeat-one
- A-B repeat if supported
- Hold
- Remote Hold
- Sleep timer
- Disk activity
- FM stereo/tuned state
- Recording state
- recording pause
- signal level
- optional peak meters

Graphics must be:

- small
- monochrome or restrained grayscale
- hard-edged
- clear
- functional
- consistent

No decorative icons without informational purpose.

---

# 13. Cyan// Status Rail

Create a signature bottom status rail.

Potential layout:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━
▶ 03:18            ▰▰▰▱
```

or:

```text
03:18 ━━━━━●━━━━ 03:53
```

The rail may carry:

- playback state
- elapsed time
- progress
- battery
- exceptional temporary icons

Do not permanently overload it.

Status priority:

1. current interaction state
2. battery
3. active unusual modes
4. everything else

---

# 14. Transient Volume Interface

Use `%mv` or equivalent current supported behavior.

Normal WPS should not permanently allocate substantial space to volume.

When volume changes, display a temporary Cyan// overlay or alternate viewport:

```text
VOLUME//

-28 dB

██████████░░░░
```

Requirements:

- appears immediately
- remains visible briefly after input
- automatically returns to WPS
- uses large readable type
- preferably includes graphical meter
- does not require firmware changes

This should feel like a modern modal HUD inside a TUI.

---

# 15. Seek / Fast-Forward / Rewind

Create intentional seeking states.

Normal:

```text
03:18 ━━━━━━━●━━━ 03:53
```

Seeking:

```text
SEEK//FORWARD

03:41 ━━━━━━━━━◆━ 03:53
```

or a more compact version.

Use Rockbox playback state conditionals.

Differentiate:

- normal playback
- pause
- fast-forward
- rewind

Do not create a full new screen unless required.

---

# 16. Track Start and Up Next

Rockbox exposes beginning/end-of-track conditions.

Use them carefully.

Possible behavior near track end:

```text
UP NEXT//

Gigantic
Pixies
```

Potential approach:

- during final 5–7 seconds
- temporarily replace lower-priority album/status line
- do not replace title/artist of current track prematurely
- make the transition visually calm

Do not imitate Apple's exact Up Next UI.

The purpose is useful glanceable information.

---

# 17. Current Playlist

Treat Current Playlist as a major Cyan// surface.

Suggested label:

```text
QUEUE//
```

Concept:

```text
QUEUE//

12  Where Is My Mind?
13  Gigantic
14  River Euphrates
15  Vamos
16  I'm Amazed
```

Explore numbered-list styling using current Rockbox list tags.

Goals:

- obvious currently playing item
- strong selection state
- useful upcoming-track visibility
- consistent Terminus typography
- minimal icons

This screen should look particularly good because its structure naturally resembles a coding-agent task list or terminal queue.

---

# 18. Native Track Info

Do not create a second WPS.

Use Rockbox's native Track Info screen.

On the H120, preserve native behavior such as the existing Track Info access mechanism.

Do not force a WPS hotkey assignment.

Style the native screen through Cyan//'s SBS/list system.

Preferred identity:

```text
TRACK//INFO
```

Use dense but readable technical typography.

Expected useful fields include native Rockbox-provided metadata such as:

- title
- artist
- album
- genre
- year
- codec
- bitrate
- sample rate
- ReplayGain
- file size
- path
- playlist position
- duration

Do not duplicate Rockbox metadata logic.

Let Rockbox decide what fields exist and omit unavailable values.

---

# 19. FM Radio

FM is a flagship H-series feature.

Cyan// must provide a deliberately designed `.fms`.

Preferred identity:

```text
RADIO//
```

Useful display candidates:

- current frequency
- preset name
- preset number
- scan/preset mode
- tuned state
- stereo/mono
- signal strength
- mute state
- battery

Concept:

```text
RADIO//

KUTX
98.9 MHz

━━━━━━━━━━●━━━

STEREO      SIG ▰▰▰▱
```

Where hardware lacks RDS, do not fabricate station names.

Use actual exposed data only.

FM should feel like operating a compact communications receiver.

This is an opportunity to lean slightly more cyberpunk than the normal WPS.

---

# 20. Recording

Recording is another flagship H120/H140 differentiator.

Treat the Recording screen as a serious instrumentation surface.

Preferred identity:

```text
RECORD//
```

Potential information:

- source
- codec/format
- sample rate
- stereo/mono
- elapsed recording time
- recording filename where available
- free space where available
- L/R levels
- clipping/peak state
- pause state
- battery

Concept:

```text
RECORD//

SRC     LINE
RATE    44.1 kHz
FORMAT  WAV

L ███████████░
R █████████░░░

00:18:42
```

Use real Rockbox-exposed state only.

Recording should be visually more technical than playback.

This is one of Cyan//'s best opportunities for a convincing cyberdeck/instrument aesthetic.

---

# 21. H120 Recording Sources

The H120/H140 can record from multiple hardware sources.

Account for:

- microphone
- line input
- FM radio
- S/PDIF

Where current Rockbox skin APIs allow source identification, surface it prominently.

Examples:

```text
SRC // MIC
SRC // LINE
SRC // FM
SRC // SPDIF
```

Do not assume every recording source is exposed to skins.

Research current implementation before designing around it.

If a source is not directly accessible through the theme engine, document the limitation.

---

# 22. S/PDIF

The H120/H140 supports S/PDIF output and S/PDIF as a recording input capability.

Investigate whether current Rockbox theme or settings tags expose:

- S/PDIF output enabled state
- digital input state
- related recording-source data

If exposed:

give S/PDIF a distinctive but restrained state indicator.

Possible syntax:

```text
DIGITAL//OUT
SPDIF//IN
```

If not exposed to skins, do not modify firmware merely to obtain it during the initial project.

Document it as a potential future firmware-enhanced integration.

This is a showcase feature because relatively few classic MP3 players have optical digital I/O.

---

# 23. Remote LCD

The H1x0 remote LCD is part of the flagship experience.

Main remote display:

- 128×64
- 1-bit
- separate remote skin capability

Create a dedicated Cyan// remote WPS.

Goal:

**maximum glanceability**

Concept:

```text
CYAN//

Where Is My Mind?
Pixies

▶ ━━━━━●━━ 03:18
```

Keep the remote simpler than the main screen.

Potential remote information:

- title
- artist
- progress
- elapsed time
- play/pause
- battery
- Hold/remote Hold where useful

Do not attempt to replicate every main-screen feature.

---

# 24. Remote Menus and States

Investigate how much of Cyan//'s SBS/list styling applies to the remote UI.

Where supported:

- consistent Terminus-like or appropriate remote fonts
- clear selected row
- compact status
- Cyan// context language
- remote Hold state

Treat the remote as a genuine secondary interface, not an afterthought.

---

# 25. QuickScreen

Give QuickScreen a custom Cyan// treatment.

Preferred identity:

```text
QUICK//
```

Preserve Rockbox's native four-way behavior.

Display each setting's:

- name
- current value
- directional relationship

Possible visual concept:

```text
          Shuffle
            OFF

Repeat ALL       EQ OFF

           Bass
            +2
```

or a more pane-like TUI version if interaction remains obvious.

Do not make QuickScreen visually ambiguous just to look futuristic.

---

# 26. Pitch Screen

Give Pitch screen intentional styling.

Preferred identity:

```text
PITCH//
```

Possible display:

```text
PITCH//

100.0%

────────●────────
```

If Rockbox exposes timestretch/pitch details, show them where useful.

The screen should resemble a calibration/control instrument.

---

# 27. Settings Menus

Settings should inherit Cyan//'s main list system.

Preferred top-level identity:

```text
CONFIG//
```

Prioritize:

- readable names
- current values
- clear selected row
- strong hierarchy
- consistent scrolling

Do not unnecessarily abbreviate setting names.

---

# 28. Setting Chooser

Give Setting Chooser a focused modal treatment where possible.

Possible visual identity:

```text
CONFIG / REPEAT
```

or simply retain the native setting title.

The selected value should be unmistakable.

Avoid adding decorative branding that competes with the setting being changed.

---

# 29. Context Menu

Context Menu should feel like an action palette.

Preferred identity:

```text
ACTION//
```

This is a natural Codex/Claude Code-inspired surface.

Example:

```text
ACTION//

> Insert
  Queue Next
  Add to Playlist
  Track Info
  Delete
```

Do not alter native action names.

Use the normal list selection system.

---

# 30. Plugin Browser

Plugin Browser should feel like launching utilities from a toolbox.

Preferred identity:

```text
TOOLS//
```

Preserve:

- plugin names
- categories
- selection clarity

Potential subtle iconography:

- utility
- game
- application

Only use icons if Rockbox exposes them reliably.

---

# 31. Plugin Runtime

Rockbox plugins may draw their own interfaces and may not respect the theme.

Cyan// should not attempt to redesign arbitrary plugin rendering.

Where an SBS or wrapper surface remains visible, style it.

Otherwise document plugin screens as:

> theme-external rendering owned by the plugin.

This is a scope boundary, not a failure.

---

# 32. System Info

Give System Info a deliberately technical appearance.

Preferred identity:

```text
SYSTEM//INFO
```

This can lean harder into the TUI aesthetic.

Use:

- key/value formatting
- aligned labels
- compact monospace text
- restrained separators

Example:

```text
SYSTEM//INFO

battery    78%
disk       34.2 GB free
buffer     ...
version    ...
```

Do not invent fields.

Use Rockbox's native list/content.

---

# 33. Time and Date

Preferred identity:

```text
CLOCK//
```

Use large readable values.

Potential concept:

```text
CLOCK//

21:05

2026-08-20
```

Only use actual device time/date support.

Do not prioritize this screen over music functionality.

---

# 34. Bookmark Browser

Preferred identity:

```text
BOOKMARKS//
```

Use normal Cyan// list styling.

Potentially emphasize:

- track/book name
- position
- resume state

Do not over-customize if Rockbox supplies limited bookmark metadata.

---

# 35. Shortcuts

Preferred identity:

```text
SHORTCUTS//
```

This should resemble a command palette or launcher.

Example:

```text
SHORTCUTS//

> Track Info
  Sleep Timer
  Equalizer
  Recording
  Files
```

Preserve user-configured shortcut names/actions.

This is another surface where modern coding-agent UI influence is appropriate.

---

# 36. Playlist Catalogue Viewer

Preferred identity:

```text
PLAYLISTS//
```

Use:

- large readable list
- clear selected playlist
- minimal metadata

Treat it consistently with the file/database browsers.

---

# 37. Menu Screen

General menu screens should use contextual list titles rather than forcing one universal header.

If no meaningful title is present, use:

```text
SYSTEM//
```

Do not make all menus look identical at the cost of context.

---

# 38. File Browser

Preferred identity:

```text
FILES//
```

Use Cyan//'s strongest browser treatment.

Possible technical cues:

- folder/file icons
- path hint
- list numbering only if useful
- scroll indicator

Avoid showing full filesystem paths permanently if they reduce readability.

---

# 39. Database Browser

Preferred identity:

```text
MUSIC//
```

This is the user's primary music-navigation surface.

Potential contexts:

```text
MUSIC / ARTISTS
MUSIC / ALBUMS
MUSIC / SONGS
MUSIC / GENRES
```

This screen receives the highest usability priority in the project.

---

# 40. Hold / Lock

Use Hold state intentionally.

Upon activation, consider a short prominent transient:

```text
LOCKED//
```

Then reduce it to a small lock icon.

If remote Hold can be detected, distinguish:

- main Hold
- remote Hold

Do not permanently consume a full row for Hold state.

---

# 41. Sleep Timer

When active, display a small status icon.

If space permits, temporary expanded state may show remaining time.

Example:

```text
SLEEP 32m
```

Do not show anything when inactive.

---

# 42. Charging

Battery display should have multiple states:

- normal
- low
- charging
- full/charged if exposed

Potential charging treatment:

```text
▰▰▰▱⚡
```

Use bitmaps instead of relying on unsupported glyphs.

When charging, percentage may be more useful than during normal playback.

---

# 43. Battery

Normal WPS:

graphical indicator only where possible.

Technical screens may show:

- percentage
- estimated time
- voltage if exposed and useful

Do not show voltage on the normal WPS.

---

# 44. Disk Activity

Rockbox exposes disk activity state.

Experiment with a very small virtual activity LED.

Possible design:

```text
■
```

or a tiny 2×2 / 3×3 bitmap.

This can be a period-appropriate technical detail.

If it becomes distracting, remove it from normal WPS and retain it only on technical/system surfaces.

---

# 45. Repeat and Shuffle

Use compact state indicators.

Possible modes include:

- repeat off
- repeat all
- repeat one
- shuffle
- A-B where supported

Do not reserve full text labels permanently.

Only show active modes.

---

# 46. Peak Meters

Use peak meters where they have real value.

Best targets:

1. recording
2. technical audio screens
3. possible transient playback instrumentation

Do not permanently place large VU meters on the normal WPS.

---

# 47. Runtime Database Metadata

Rockbox may expose:

- play count
- rating
- autoscore

Do not put these on the default WPS.

Possible future uses:

- Track Info where natively surfaced
- database views
- technical inspector

Do not build custom interaction around them without evidence of usability.

---

# 48. Music Metadata

Rockbox skin capabilities include rich metadata.

Potential available values include:

- title
- artist
- composer
- album artist
- album
- grouping
- genre
- track number
- disc number
- year
- comment
- filename
- path
- file size
- codec
- bitrate
- sample rate
- VBR/CBR
- ReplayGain
- pitch
- playlist position
- playlist length
- next-track metadata

Use metadata contextually.

Rule:

> Just because Rockbox exposes it does not mean it belongs on every screen.

The maximalist philosophy means Cyan// should have a sensible place for useful information somewhere in the overall interface.

---

# 49. Next-Track Metadata

Rockbox supports accessing next-track values for many metadata tags.

Use this selectively.

Primary use:

- Up Next near the end of the current track
- Queue screen

Do not permanently duplicate next-track information on the main WPS unless later physical testing shows compelling value.

---

# 50. Progress Bars

Create a coherent Cyan// bar language.

Bars should share geometry for:

- track progress
- volume
- pitch
- FM frequency
- battery where appropriate
- signal
- recording level
- settings

Visual vocabulary:

- hard rectangular fill
- one-pixel borders
- block segments
- clear current-position marker

Avoid pseudo-3D styling.

---

# 51. Icons

Create a small shared Cyan// bitmap icon set.

Potential assets:

```text
play
pause
stop
ff
rew
seek
battery_0
battery_1
battery_2
battery_3
battery_4
charging
hold
remote_hold
shuffle
repeat_all
repeat_one
repeat_ab
sleep
fm_stereo
fm_tuned
record
record_pause
disk_activity
```

Use sprite strips where Rockbox's image mechanisms make that sensible.

Document:

- dimensions
- states
- grayscale depth
- intended surfaces

---

# 52. Color and Grayscale

H120 flagship edition:

- grayscale only
- high contrast
- physical blue backlight supplies Cyan identity

Use grayscale tactically for:

- secondary information
- disabled state
- progress background
- subtle separators

Do not use low-contrast gray for essential text.

---

# 53. LCD Inversion

The H120 supports LCD inversion.

Investigate whether Cyan// behaves acceptably with inversion enabled.

Do not assume the default visual mode.

If necessary, document:

- recommended normal/inverted setting
- any visual limitations

Do not force a user setting unless clearly justified.

---

# 54. Backlight

Physical testing must include:

- backlight on
- backlight off
- dim ambient conditions
- daylight/coffee shop lighting
- car use

The physical blue backlight is part of Cyan//'s identity.

Do not optimize solely against emulator screenshots.

---

# 55. Accessibility Requirements

Primary physical use:

- approximately 18–30 inch viewing distance
- quick glances
- aging eyesight
- device sitting beside user

Test:

- long artist names
- long track names
- long album names
- punctuation
- numbers
- mixed case
- playlist names
- folders
- deeply nested paths

Test character differentiation:

- `0/O`
- `1/l/I`
- `5/S`
- slash/backslash
- punctuation
- parentheses
- colon
- hyphen

---

# 56. Target Portability

Long-term port order remains:

## v0.x
iRiver H120/H140

## next
iAudio M5

## next
iPod 4G grayscale

## next
iAudio X5

## next
iPod Mini 1G/2G

The H-series edition may remain the most feature-rich Cyan// implementation.

That is acceptable.

Do not reduce H-series functionality merely to maintain feature parity with simpler targets.

The theme family may use:

```text
Cyan// H1x0
Cyan// M5
Cyan// 4G
Cyan// X5
Cyan// Mini
```

while sharing one design language.

---

# 57. H-Series Flagship Principle

Cyan// H1x0 should become the **showcase edition**.

If H120/H140 exposes hardware not present on other players, Cyan// should use it where the skin APIs permit.

Potential flagship areas:

- remote LCD
- FM
- recording
- multiple recording inputs
- digital S/PDIF capability
- hard-disk activity
- backlight identity
- extensive physical controls
- technical status screens

Do not force other target ports to mimic unavailable functionality.

---

# 58. Repository Structure

Recommended:

```text
cyan-rockbox/
├── README.md
├── PRD.md
├── HARDWARE.md
├── LICENSE
├── docs/
│   ├── design.md
│   ├── rockbox-notes.md
│   ├── h1x0-capabilities.md
│   ├── screen-matrix.md
│   ├── testing.md
│   ├── portability.md
│   └── screenshots/
├── reference/
│   ├── fontslist.txt
│   ├── gray/
│   ├── mind/
│   ├── ipodVOL/
│   ├── CoverMax-XXL/
│   └── additional-themes/
├── src/
│   └── h1x0/
│       ├── Cyan.cfg
│       ├── Cyan.sbs
│       ├── Cyan.wps
│       ├── Cyan.fms
│       ├── Cyan.rwps
│       ├── Cyan.rsbs
│       └── assets/
├── tools/
├── tests/
└── dist/
```

Adjust filenames/extensions to actual supported Rockbox conventions.

Do not invent files merely because this PRD names them.

Verify first.

---

# 59. Screen Matrix

Create:

```text
docs/screen-matrix.md
```

For every `%cs` screen, record:

- screen number
- upstream Rockbox name
- H120 availability
- themeable?
- relevant skin file
- relevant tags
- Cyan// header
- target font
- custom list behavior
- icons/state
- implementation status
- screenshot status
- physical test status

Every screen must eventually be one of:

- fully styled
- partially styleable
- not exposed sufficiently to theme engine
- rendered externally by plugin/application

Do not silently leave a screen unaddressed.

---

# 60. Capability Matrix

Create:

```text
docs/h1x0-capabilities.md
```

Document:

- main LCD
- remote LCD
- FM
- recording
- microphone
- line-in
- FM recording
- S/PDIF input
- S/PDIF output
- battery
- charging
- Hold
- remote Hold
- hard disk
- QuickScreen
- hotkey
- RTC if applicable
- backlight
- contrast
- plugin environment

For each:

- hardware supports it?
- Rockbox supports it?
- skin exposes it?
- Cyan// can theme it?
- Cyan// should display it?
- implementation priority

---

# 61. Reference Theme Research

Keep the four original reference themes:

- Gray
- mind
- ipodVOL
- CoverMax-XXL

Also identify additional reference themes specifically demonstrating:

- custom list drawing
- QuickScreen customization
- FM skins
- recording-related skin behavior
- remote skins
- transient volume viewports
- seek viewports
- battery strips
- bitmap indicators
- grayscale status systems
- custom scrollbars

Do not copy visual identity.

Study implementation patterns.

Preserve all author/license information.

---

# 62. Official Research Requirement

Before implementing any mechanism, prefer current upstream Rockbox sources.

Research:

- skin syntax
- `%cs`
- SBS
- RSBS
- WPS
- RWPS
- FMS
- RFMS if applicable
- list skin tags
- image tags
- bitmap strips
- progress bars
- settings tags
- FM tags
- recording tags
- remote tags
- Hold
- playback state
- next-track metadata
- runtime database metadata
- QuickScreen tags
- current-screen detection
- simulator
- validation tools
- theme packaging
- submission requirements

Do not rely on old wiki syntax without current-source verification.

---

# 63. Native Rockbox First

Cyan// should be maximalist visually, but conservative architecturally.

Preferred order:

1. native theme feature
2. native conditional viewport
3. native list skin
4. bitmap assets
5. documented target-specific behavior

Avoid firmware modification.

If a desired feature requires firmware changes:

- document it
- mark it as optional/future
- do not block the main theme

---

# 64. Development Milestones

## Milestone 0 — Research and matrices

Produce:

- repository scaffold
- screen matrix
- H1x0 capability matrix
- official Rockbox notes
- reference-theme inventory
- simulator assessment

No visual overbuilding yet.

---

## Milestone 1 — Browser foundation

Implement:

- 14-Terminus
- high-contrast list
- inverse selected row
- `>` prompt where feasible
- header system
- basic status rail
- Database browser
- File browser
- standard menus
- Settings menus

Physical test before proceeding.

---

## Milestone 2 — Core WPS

Implement:

- title
- artist
- album
- progress rail
- playback icon
- battery
- pause state
- long-string handling

Physical test.

---

## Milestone 3 — Playback-state system

Implement:

- transient volume
- FF
- rewind
- seek
- shuffle
- repeat
- Hold
- sleep timer
- charging
- Up Next

Physical test.

---

## Milestone 4 — Native playback support surfaces

Implement/style:

- Current Playlist
- Track Info
- Context Menu
- Playlist Catalogue
- Shortcuts

---

## Milestone 5 — H-Series media instrumentation

Implement:

- FM screen
- Recording screen
- recording meters
- source/status information
- S/PDIF state where exposed

This milestone should intentionally look slightly more cyberpunk/technical than ordinary playback.

---

## Milestone 6 — Remote

Implement:

- RWPS
- remote status
- remote Hold
- remote menus/SBS where supported

Test on actual remote if hardware is available.

---

## Milestone 7 — Utility surfaces

Implement:

- QuickScreen
- Pitch screen
- Setting chooser
- System Info
- Time/Date
- Bookmark browser
- Plugin browser
- plugin chrome where possible

---

## Milestone 8 — Full `%cs` coverage audit

Review every current screen category.

No screen may remain undocumented.

For every missing treatment:

- implement
- document skin limitation
- document plugin-owned rendering

---

## Milestone 9 — Polish

Test:

- every screen
- every status
- long content
- edge cases
- backlight
- inversion
- low battery
- charging
- FM
- recording
- Hold
- seeking
- volume
- sleep
- playlist transitions
- remote

---

## Milestone 10 — Distribution

Produce:

- installable package
- screenshots
- installation instructions
- font-pack prerequisite
- supported Rockbox version
- compatibility notes
- theme-site submission package if appropriate

---

# 65. Physical Test Philosophy

Simulator testing verifies:

- syntax
- clipping
- layout
- state conditions
- assets

Physical H120 testing verifies:

- actual readability
- contrast
- backlight appearance
- button interaction
- glanceability
- perceived density

Physical-device usability wins.

---

# 66. Acceptance Criteria — Browser

The browser passes when:

- user can read it comfortably at expected distance
- selected item is immediately obvious
- at least approximately five useful rows are visible
- long text behavior is acceptable
- context is clear
- screen does not resemble an iPod menu

---

# 67. Acceptance Criteria — WPS

Primary WPS passes when:

- track title is dominant
- artist is easy to read
- album remains available
- progress is obvious
- play/pause can be understood visually
- battery is visible but unobtrusive
- no unnecessary technical metadata competes with music information

---

# 68. Acceptance Criteria — Maximalist Coverage

The project reaches feature-complete Cyan// status only when:

1. all currently documented Rockbox `%cs` screen types have been audited
2. every styleable screen has an intentional Cyan// treatment
3. every unstyleable screen has its limitation documented
4. H-series-specific media capabilities have been evaluated
5. FM has dedicated Cyan// treatment
6. recording has dedicated Cyan// treatment
7. remote has dedicated Cyan// treatment
8. native Track Info is visually integrated
9. Current Playlist is visually integrated
10. QuickScreen is visually integrated
11. major transient states are styled
12. the entire result remains readable

---

# 69. Non-Goals

Do not:

- imitate iPod UI
- imitate old Apple fonts
- imitate modern Apple graphics
- modify Rockbox firmware for ordinary theme functionality
- invent fake telemetry
- add meaningless cyberpunk decoration
- reduce primary font size merely to fit more widgets
- make every screen equally dense
- force every other Rockbox target to support H-series features
- compromise H120 functionality for theoretical portability

---

# 70. Design Rule for Maximalism

Cyan//'s maximalism means:

> Maximum intentional coverage, not maximum simultaneous information.

This distinction is critical.

A maximalist Cyan//:

- styles every available surface
- uses every useful device capability
- exposes technical information where appropriate
- treats exceptional states intentionally
- makes deep Rockbox functionality feel coherent

It does **not**:

- put every piece of metadata on every screen
- fill every pixel
- make the WPS a diagnostic dashboard

---

# 71. Desired Character by Surface

## Everyday surfaces

Browser, WPS, normal menus:

**clean modern TUI**

## Technical surfaces

Track Info, System Info, Pitch:

**coding-agent / workstation**

## Hardware-instrument surfaces

FM, Recording, S/PDIF:

**stronger cyberpunk / instrumentation**

## Remote

**minimal high-contrast terminal**

## QuickScreen / Context Menu / Shortcuts

**command palette**

This variation is intentional.

The screens should share one visual system without all looking identical.

---

# 72. Initial Codex Instruction

After reading this PRD:

1. Verify every current Rockbox mechanism referenced here.
2. Do not assume all desired behavior is supported.
3. Build `docs/screen-matrix.md`.
4. Build `docs/h1x0-capabilities.md`.
5. Inventory current reference themes.
6. Identify additional implementation references.
7. Implement only Milestones 0 and 1 initially.
8. Produce an installable browser-focused Cyan// prototype.
9. Provide exact physical-H120 testing instructions.
10. Stop for physical evaluation before implementing the WPS and later screens.

The long-term project is maximalist.

The first implementation remains deliberately incremental.

---

# 73. Final Product Definition

Cyan// is not merely a large-font Rockbox theme.

It is intended to become:

> A complete TUI visual system for Rockbox, with the iRiver H120/H140 serving as its flagship cyberdeck-like implementation.

The normal music experience should remain clean enough for everyday use.

The deeper the user travels into Rockbox—queue, Track Info, FM, recording, system information, shortcuts, settings, remote operation—the more Cyan//'s technical and cyberpunk personality should reveal itself.

The H120/H140 should feel not merely preserved, but upgraded into a coherent modern technical instrument.