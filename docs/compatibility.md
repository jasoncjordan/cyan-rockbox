# Cyan// compatibility

## Supported baseline

- Theme version: Cyan// 0.1.0 H1x0 release candidate
- Rockbox baseline: [official Rockbox 4.0](https://www.rockbox.org/wiki/ReleaseNotes400)
- Target: `iriverh120`, covering iRiver H120/H140
- Main LCD: 160×128×2
- Remote LCD: 128×64×1 with a compatible H1x0 LCD remote

The skin was also audited against current upstream Rockbox documentation and
source. Current development builds are expected to work, but they are not a
substitute for testing the exact installed build.

## Required optional font pack

Install the official optional Rockbox font pack matching the firmware build.
Cyan// references these files without redistributing them:

- `10-ProFont.fnt`
- `12-Terminus.fnt`
- `14-Terminus.fnt`
- `14-Terminus-Bold.fnt`
- `16-Terminus.fnt`
- `18-Terminus-Bold.fnt`

## Intentional platform boundaries

- H120/H140 has no RTC, so the Time/Date screen is unavailable.
- Current Pitch and arbitrary plugin runtime screens draw their own pixels.
- Native Track Info, recording controls/meters, QuickScreen controls, list
  contents, and navigation remain firmware-owned beneath Cyan chrome.
- FM and remote skins require the corresponding hardware.
- Cyan// is not packaged for H3xx, iPod, or any other Rockbox target.

## Validation boundary

Asset, viewport, screen-coverage, screenshot-dimension, package-content, and
ZIP-integrity checks pass locally. CheckWPS, H120/H140 simulator loading, and
physical main/remote testing are still required before the release candidate
can be described as certified or theme-site-ready. Follow the exact commands
and pass criteria in [`final-validation.md`](final-validation.md), then the full
state matrix in [`testing.md`](testing.md).
