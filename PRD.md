# PRD: Cyan// — Large-Type TUI-Inspired Rockbox Theme

You are helping design and implement a custom Rockbox theme named **Cyan//**.

Your job is to research the current Rockbox theme-development conventions, inspect existing themes for reusable patterns, create a maintainable source repository, and implement the first working version for the **iRiver H120/H140 family**.

Do not modify Rockbox firmware unless absolutely necessary. This project should be implemented as a normal Rockbox theme using supported theme, skin, font, bitmap, viewport, status-bar, and configuration mechanisms.

## 1. Product Vision

Cyan// is a highly readable Rockbox theme for classic small-screen digital audio players.

The reference device is an **iRiver H120 running Rockbox**, with a **160×128 grayscale LCD and blue backlight**.

The design should combine:

- modern Apple Music-style information hierarchy and simplicity
- modern terminal/TUI interaction patterns
- subtle visual inspiration from Codex, Claude Code, UNIX tools, classic workstation interfaces, and late-1980s through early-2000s computer interfaces
- sparse graphical status indicators
- high legibility for aging eyes
- an aesthetic that feels deliberate, technical, and modern rather than nostalgic for the iPod

The theme must **not look like an original iPod**.

Do not imitate classic Apple fonts, click-wheel-era UI conventions, skeuomorphic controls, or old iPod menus.

The Apple influence should be limited to information-design principles:

- clear hierarchy
- strong primary content
- generous spacing where practical
- restrained metadata
- obvious selection state
- uncluttered screens
- important information shown at a glance

## 2. Name and Visual Identity

Theme name:

**Cyan//**

The name is inspired by:

1. the blue backlight of the iRiver H120
2. cyan as a classic computer-display color
3. cyan/magenta CGA-era visual culture
4. a deliberate contrast with the existing Rockbox theme **Gray**, which originally inspired this project

The screen itself is grayscale. Do not attempt to simulate cyan using gray artwork.

The physical blue H120 backlight provides the “cyan” visual effect.

The `//` in Cyan// should inform the theme's visual personality, but should not be plastered decoratively throughout the interface.

Think:

- terse
- technical
- clean
- high contrast
- terminal-adjacent
- cyberpunk only in restraint

Avoid stereotypical “hacker skin” decoration.

## 3. Primary User Goals

Rank interface priorities in this order:

### 1. Browse / Search / Selection

This is the most important interface.

The user must be able to comfortably browse:

- artists
- albums
- songs
- playlists
- files
- database results

The player is often sitting beside the user in a car or coffee shop rather than being held directly in front of the face.

Optimize for **glanceable readability at approximately 18–30 inches**.

The user accepts lower information density in exchange for larger text.

The browser should show enough rows to make navigation practical, but readability is more important than maximizing row count.

Target approximately **5–8 useful visible choices**, depending on the final font metrics and Rockbox UI constraints.

### 2. Now Playing

The Now Playing screen is the second-highest priority.

It should emphasize:

1. track title
2. artist
3. album
4. playback progress
5. playback state
6. battery
7. volume

Everything else is optional.

Codec, bitrate, sample rate, file format, disk information, and other technical metadata should be omitted by default unless there is spare space and a compelling usability reason.

### 3. Rockbox Menus and Settings

Normal Rockbox menus should remain readable, consistent, and familiar.

Do not optimize the WPS while leaving menus difficult to read.

## 4. Typography

Use the optional Rockbox font pack.

The available H120 font pack includes Terminus at multiple sizes, including:

- 12-Terminus
- 14-Terminus
- 14-Terminus-Bold
- 16-Terminus
- 16-Terminus-Bold
- 18-Terminus
- 18-Terminus-Bold
- 20-Terminus
- larger Terminus sizes

It also includes:

- Fixed
- Fixed-Bold
- Fixed-SemiCond
- ProFont
- Nimbus
- Adobe Helvetica
- Artwiz Snap
- Jackash
- other Rockbox fonts

The initial design should use **Terminus** unless testing shows that another font materially improves readability.

Initial typography targets:

- browser/menu rows: **14-Terminus**
- headers: **14-Terminus-Bold**
- Now Playing track title: **18-Terminus-Bold**
- artist: **16-Terminus**
- album and secondary metadata: **12-Terminus**
- compact status values: **12-Terminus**

These are starting points, not immutable constants.

Test:

- 14-Terminus vs 14-Terminus-Bold for browsing
- 14-Terminus vs 16-Terminus if readability requires it
- semi-condensed Fixed variants if horizontal truncation becomes a major problem
- ProFont only if it retains sufficient readability

Do not choose a smaller font merely to fit more information.

The theme exists partly to solve the problem of tiny Rockbox typography.

The official optional font pack confirms Terminus variants at the intended sizes, including 12, 14, 16, 18, 20 and larger, with bold variants available at relevant sizes. 

## 5. Selection Model

The preferred browser selection treatment is:

**full-width inverse selection row + `>` prompt-style marker**

Conceptually:

```text
  Portishead
> Radiohead
  R.E.M.
  Soundgarden
```

The selected row should be visually unmistakable.

The `>` marker is intentional because it simultaneously evokes:

- command-line prompts
- terminal menus
- classic text interfaces
- early embedded interfaces

Avoid Apple-style right-facing chevrons after menu items.

Do not build an iPod-style menu.

If Rockbox does not cleanly permit inverse highlighting and a `>` marker together, prioritize:

1. strong high-contrast selected row
2. prompt-style marker
3. visual simplicity

Test native Rockbox selector behavior before implementing custom hacks.

## 6. Overall Layout Language

Use the following screen hierarchy wherever practical:

```text
HEADER / CONTEXT

PRIMARY CONTENT
PRIMARY CONTENT
PRIMARY CONTENT

STATUS / STATE
```

The interface should feel related to a good modern TUI, not a movie depiction of a hacker terminal.

Good inspiration:

- Codex
- Claude Code
- modern CLI tools
- `vim`
- `htop`
- `mc`
- UNIX workstation software
- text-mode configuration tools
- BIOS/setup interfaces
- NeXT/X11-era visual restraint
- modern Apple Music information hierarchy

Bad inspiration:

- Matrix rain
- fake hexadecimal telemetry
- fake shell commands everywhere
- tiny diagnostic readouts
- excessive ASCII borders
- neon cyberpunk ornament
- skeuomorphic media controls
- original iPod menus

## 7. Browser Screen Concept

Preferred conceptual direction:

```text
MUSIC / ALBUMS

> Doolittle
  Dummy
  In Rainbows
  Mezzanine
  Violator

05                     ▰▰▰▱
```

Alternative context syntax that may be tested:

```text
~/music/albums
```

However, do not sacrifice clarity for terminal cosplay.

`MUSIC / ALBUMS` may be more readable and generally preferable.

Avoid excessive path detail.

Use uppercase sparingly, primarily for headers and status labels.

Do not uppercase album, artist, or track names automatically.

## 8. Now Playing Screen

The Now Playing screen should use a hybrid text-and-graphics design.

Large text should carry semantic content.

Small graphical elements should carry state efficiently.

Target hierarchy:

```text
NOW PLAYING              [play icon]

TRACK TITLE
ARTIST
Album

03:18 [progress bar] 03:53

[volume]             [battery]
```

Track title should be the largest visual element.

Artist is second.

Album is tertiary.

Do not waste a full text row saying `PLAYING` if a small playback icon can communicate the same state.

## 9. Tactical Graphics

The theme is **not required to be entirely text-based**.

Use tiny monochrome/grayscale graphics where they communicate information more efficiently than text.

Good graphical candidates:

- Play
- Pause
- Fast-forward
- Rewind
- Seeking/scrubbing
- Battery level
- Charging
- Progress
- Volume
- Shuffle
- Repeat
- Repeat-one

Graphics should be:

- tiny
- functional
- high contrast
- one-bit or restrained grayscale where possible
- stylistically consistent
- understandable without explanation

Every graphic must answer one of these questions:

- What is happening?
- How much?
- Where am I?
- What is selected?

If it does not answer one of those questions, remove it.

Do not add graphics merely for decoration.

## 10. Playback State

Prefer a tiny state icon rather than textual state.

Possible states:

- play
- pause
- fast-forward
- rewind
- stop where relevant

Example concept:

```text
NOW PLAYING                 ▶
```

Paused:

```text
NOW PLAYING                 ‖
```

Implement these with supported Rockbox bitmap/state mechanisms rather than relying on Unicode glyph availability unless testing proves the font handles the glyphs properly.

## 11. Progress and Scrubbing

Create a thin graphical playback-progress rail.

It should be visually prominent enough to read but consume little vertical space.

Normal playback could resemble:

```text
━━━━━━━●━━━━━━
```

Scrubbing/seeking could use a stronger state marker:

```text
━━━━━━━◆━━━━━━
```

Do not assume these literal glyphs will be used.

Prefer native Rockbox bars or small bitmap assets when more reliable.

Investigate what Rockbox allows for:

- playback progress bars
- seek indicators
- WPS conditional state
- custom bar images
- bitmap strips

The progress bar may become a signature element of Cyan//.

## 12. Bottom Status Rail

Develop a compact **bottom status rail** as a signature design element.

Potential content:

- elapsed time
- playback state
- volume
- battery
- repeat/shuffle only when active

Potential conceptual layout:

```text
━━━━━━━━━━━━━━━━━━━━━━━━━━
▶ 03:18        -28dB   ▰▰▰▱
```

Or allow the progress bar itself to form the upper edge of the status rail.

Keep it sparse.

Do not let the footer become a diagnostic dashboard.

## 13. Battery

Prefer a compact graphical battery representation rather than the word `BAT`.

Potential design:

```text
▰▰▰▱
```

or a custom bitmap with approximately 4–5 discrete visual states.

If supported and useful, create additional charging state.

Percentage display may be shown conditionally where helpful, but should not consume permanent space if the graphical meter is sufficient.

## 14. Volume

Volume should not dominate the screen.

Potential representations:

- compact `-28 dB`
- thin meter
- small segmented indicator
- temporary expanded volume display when actively changing volume

Investigate Rockbox's supported behavior for dedicated volume screens and WPS overlays.

If changing volume can trigger a temporary larger graphical meter without complicating normal playback, consider that.

## 15. Shuffle and Repeat

Do not reserve permanent text fields for shuffle and repeat.

Use tiny graphical indicators that appear only when enabled.

Prefer no more than a few simultaneous status icons.

Avoid turning the status area into an icon strip.

## 16. Borders and Geometry

Use:

- one-pixel rules
- thin separators
- occasional hard rectangular geometry
- restrained framing

Avoid boxing every UI element.

Do not waste scarce pixels on elaborate borders.

The visual reference can loosely include:

- CGA text applications
- classic UNIX workstation software
- embedded system interfaces
- modern terminal panes

A single header separator and the bottom status rail may be sufficient.

## 17. Information Density

Use information hierarchy aggressively.

Remove metadata before shrinking fonts.

If a screen becomes crowded, reduce:

1. decorative elements
2. low-value metadata
3. secondary labels
4. redundant state text

Do **not** first solve crowding by reducing primary font sizes.

Track/album/artist readability has priority over technical metadata.

## 18. Accessibility and Readability

Readability is a first-class product requirement, not an optional enhancement.

Target conditions:

- aging eyes
- player sitting beside user
- quick glances
- blue backlight
- early-2000s grayscale LCD
- variable ambient lighting

Test:

- backlight on
- backlight off
- menu selection contrast
- long album names
- long artist names
- mixed-case text
- numerals
- punctuation
- track numbers
- playlist names

Pay particular attention to differentiating:

- 0 / O
- 1 / l / I
- 5 / S
- punctuation
- parentheses
- slashes

## 19. Initial Target Scope

Version 0.1 targets:

**iRiver H120 / H140 / H1x0 160×128 grayscale family**

Do not generalize prematurely.

However, structure the repository so that later ports to related display families are practical.

Do not hardwire project organization around only one physical device.

Potential future targets include:

- iAudio M5
- iPod 4G grayscale
- iAudio X5
- iPod Mini
- other Rockbox targets with similar display constraints

Do not implement these ports in v0.1 unless trivial.

## 20. Repository Structure

Create a clean Git repository.

Suggested structure:

```text
cyan-rockbox/
├── README.md
├── LICENSE
├── docs/
│   ├── design.md
│   ├── rockbox-notes.md
│   ├── testing.md
│   └── screenshots/
├── reference/
│   ├── gray/
│   ├── mind/
│   ├── ipodVOL/
│   └── other-useful-themes/
├── src/
│   └── h1x0/
│       ├── Cyan.cfg
│       ├── Cyan.sbs
│       ├── Cyan.wps
│       ├── Cyan.fms
│       └── assets/
├── dist/
└── tools/
```

Adjust this structure if official Rockbox conventions make another layout substantially better.

Explain any changes.

Do not modify reference themes directly.

## 21. Reference Themes

Use existing Rockbox themes as implementation references, not as visual templates.

At minimum inspect:

- Gray
- mind
- ipodVOL
- Cabbiev2
- other well-maintained themes that demonstrate:
  - custom fonts
  - SBS/browser layout
  - custom selection behavior
  - battery bitmaps
  - playback-state images
  - progress bars
  - grayscale assets
  - 160×128 layouts

Gray is especially important because this project originated from wanting a more readable alternative to Gray.

Preserve useful interaction familiarity where it helps.

Do not preserve Gray's small typography.

## 22. Official Rockbox Research

Before significant implementation, locate and review current authoritative Rockbox documentation for:

- theme configuration
- CustomWPS / skin engine
- `.cfg`
- `.wps`
- `.sbs`
- `.fms`
- fonts
- viewports
- images
- image strips
- conditional tags
- playback-state tags
- progress bars
- battery state
- menu selectors
- volume behavior
- UI simulator
- theme validation
- theme packaging
- theme submission requirements

Prefer official Rockbox documentation and current Rockbox source.

Use third-party tutorials only to clarify gaps.

Document relevant findings in:

```text
docs/rockbox-notes.md
```

Do not assume old Rockbox syntax is still valid.

## 23. Simulator and Validation

Investigate whether the current Rockbox development environment provides a practical H120/H1x0 UI simulator or theme preview workflow.

If so:

- document how to build/run it
- use it during development
- add helper scripts where useful

Physical H120 testing remains authoritative because:

- LCD contrast matters
- physical pixel size matters
- blue backlight changes appearance
- viewing distance matters

Simulator correctness does not equal usability.

## 24. Development Strategy

Do not try to build the entire finished theme in one pass.

Use incremental milestones.

### Milestone 0 — Research

Produce:

- current Rockbox skin/theme syntax notes
- relevant official links
- reference-theme observations
- simulator/validation options
- identified technical constraints

### Milestone 1 — Readable Browser

Start from a known-good H120 theme configuration, preferably Gray where practical.

Implement only:

- 14-Terminus browser font
- high-contrast selection
- `>` selection prompt if possible
- simple header/context
- readable menu spacing
- minimal footer

Do not redesign Now Playing yet.

This milestone is successful when browsing music is materially easier to read than Gray.

### Milestone 2 — Typography Testing

Create easy-to-test alternatives for:

- 14-Terminus
- 14-Terminus-Bold
- 16-Terminus

Do not create three separate codebases.

Make font comparison easy.

### Milestone 3 — Cyan// Now Playing

Implement:

- large track title
- artist
- album
- graphical playback state
- graphical progress rail
- compact elapsed/remaining time
- graphical battery
- compact volume

### Milestone 4 — Status System

Add and test:

- pause
- seek
- repeat
- repeat-one
- shuffle
- charging
- volume changes

Only expose states that are useful.

### Milestone 5 — Polish

Refine:

- spacing
- clipping
- long strings
- truncation
- contrast
- icon alignment
- status-rail proportions
- backlight readability

### Milestone 6 — Packaging

Produce a clean Rockbox-installable package.

Document installation.

If appropriate, prepare for eventual submission to the Rockbox theme repository.

## 25. Testing Dataset

Use realistic long and short strings.

Test names such as:

```text
Pixies
R.E.M.
Nine Inch Nails
The Smashing Pumpkins
Queens of the Stone Age
The Presidents of the United States of America
```

Albums:

```text
Doolittle
Dummy
Disintegration
The Downward Spiral
Mellon Collie and the Infinite Sadness
Songs for the Deaf
```

Track titles should include examples substantially longer than screen width.

Test:

- clipping
- scrolling behavior
- truncation
- current-track emphasis

Do not optimize only for short demo text.

## 26. Non-Goals for v0.1

Do not:

- modify Rockbox firmware
- create a universal theme for every player
- support color targets
- recreate Apple Music visually
- reproduce iPod UI
- add album artwork unless later evidence strongly supports it
- add decorative code/hex output
- add fake terminal commands
- add unnecessary metadata
- create custom fonts if existing Terminus works
- build a complex theming framework
- over-abstract layout code
- optimize for theme-repository popularity before usability

## 27. Maintainability Requirements

Treat all theme source as maintained software.

Use:

- Git
- readable formatting
- comments where useful
- sensible naming
- documented asset dimensions
- documented font choices
- documented device assumptions

Avoid unexplained magic numbers.

Where pixel coordinates are unavoidable, document the reason for major layout values.

Keep source assets separate from packaged output.

## 28. Future Portability

Although v0.1 targets H1x0 only, make design decisions that preserve eventual portability.

Separate:

- design rules
- target-specific coordinates
- icons/assets
- font choices
- packaging

Future theme families may include:

```text
160x128-gray
160x128-color
138x110-gray
176x132-color
220x176-color
```

Do not implement these yet.

The long-term goal is:

**one visual language, multiple deliberately designed layouts**

—not a single automatically scaled layout.

## 29. Design Principles

Use these as hard decision rules:

1. Readability beats information density.
2. Remove metadata before shrinking fonts.
3. Text communicates meaning; graphics communicate state.
4. Every graphic must have a functional purpose.
5. High contrast beats subtlety.
6. TUI influence should feel authentic, not theatrical.
7. Apple influence means hierarchy, not appearance.
8. Avoid iPod visual language.
9. The screen should look good because it is disciplined, not because it is busy.
10. Physical H120 testing overrides simulator aesthetics.
11. Simple Rockbox-native mechanisms are preferable to clever hacks.
12. H120 usability comes before cross-device generalization.

## 30. Desired Emotional Character

Cyan// should feel like:

> A tiny, beautifully designed technical instrument.

Not:

> An old MP3 player wearing a hacker skin.

And not:

> An iPod clone.

It should plausibly look at home beside:

- a terminal
- a hardware debugger
- a DEF CON badge
- a UNIX workstation
- a modern coding-agent interface

while still functioning first and foremost as a practical music player.

## 31. Initial Deliverables

For the first Codex work session, do **not** attempt the whole project.

Produce:

1. A repository scaffold.
2. `docs/design.md` summarizing the frozen Cyan// design system.
3. `docs/rockbox-notes.md` documenting current official Rockbox theme mechanisms relevant to the project.
4. An inventory of the Gray theme files and dependencies.
5. An inventory of at least 3–5 useful reference themes.
6. Identification of the font currently used by Gray where possible.
7. A technical assessment of how browser/menu font and selector behavior are controlled on H1x0.
8. A proposed implementation for Milestone 1.
9. A minimal first working Cyan// theme derived from known-good H1x0 theme code, changing as little as necessary to achieve:
   - 14-Terminus
   - high-contrast selection
   - clear header
   - sparse status area
10. Exact installation instructions for testing the build on a physical H120.
11. A short test checklist for me to report back:
   - readability
   - number of visible rows
   - truncation
   - selection clarity
   - backlight-on appearance
   - backlight-off appearance

Stop after the first usable browser-focused prototype.

Do not proceed into a full WPS redesign until the browser typography has been physically evaluated.

## 32. Working Style

When uncertain:

- inspect official Rockbox documentation
- inspect existing working themes
- prefer proven Rockbox patterns
- state assumptions
- preserve rollback ability

Do not silently invent unsupported theme syntax.

Do not make broad architectural changes without explaining why.

If an idea from this PRD is unsupported by Rockbox, identify the limitation and propose the simplest visually similar alternative.

The objective of the first iteration is not perfection.

The objective is to establish a **known-good, readable Cyan// foundation on the physical iRiver H120** that we can iterate on.