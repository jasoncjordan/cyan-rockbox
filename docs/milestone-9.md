# Milestone 9 — Polish

Milestone 9 completes the browser- and source-testable polish pass across the
current H1x0 implementation. It does not claim the separate physical-device
gate defined by the PRD.

## Automated results

- `tools/check-assets.py` verifies every generated bitmap is one-bit and has
  the exact dimensions expected by the skins.
- `tools/check-screen-coverage.py` verifies all 20 current Rockbox screen
  categories remain classified: 17 themed, two external, and one unavailable
  on the no-RTC H120.
- `tools/check-layout.py` parses all numeric `%V`, `%Vl`, and `%Vi` declarations
  in the five main/remote skins. All 81 viewports fit the 160×128 or 128×64
  target, and frozen header, battery, progress, seek, footer, and remote
  fragments remain intact.
- `tools/package.sh` and ZIP integrity testing verify the installable snapshot.

The progress rail remains five pixels tall in normal playback and seek mode.
Visual review prompted a seek-asset refinement: the rail's upper and lower
border lines now extend two pixels into the marker field from each side, then
stop at the diamond's one-pixel white edge.

## Browser stress matrix

The `?milestone=9` preview collects these cases in one review surface:

- long browser header, rows, punctuation, and ambiguous glyphs
- long WPS title, artist, and album
- low battery and charging
- Hold, volume takeover, sleep, and final-seven-second playlist transition
- seek marker at exactly 0%, 50%, and 100%
- inverted one-bit LCD proxy
- FM scanning, S/PDIF recording, and long-text 128×64 remote playback

The proxies preserve the theme's target pixel dimensions and bitmap assets.
They verify composition and clipping, not firmware behavior or real LCD
appearance.

## Physical gate still open

Follow the Milestone 9 matrix in [`testing.md`](testing.md) on an H120/H140 and
compatible remote. Required observations include backlight on/off, actual LCD
inversion, low-battery and charging transitions, FM reception, native recording
meters, Hold, seeking, volume, sleep, playlist transition timing, navigation,
and comfortable-distance readability. Physical usability wins over the proxy.
