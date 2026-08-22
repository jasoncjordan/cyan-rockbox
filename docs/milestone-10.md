# Milestone 10 — Distribution

Milestone 10 produces a reproducible release-candidate distribution without
overstating the still-open simulator and physical-device gates.

## Outputs

- `dist/Cyan-0.1.0-h1x0.zip` — clean player-root install archive
- `dist/Cyan-0.1.0-h1x0-distribution.zip` — install archive, documentation,
  checksums, license, and labeled browser-proxy screenshots
- [`installation.md`](installation.md) — install, upgrade, rollback, and font
  prerequisites
- [`compatibility.md`](compatibility.md) — Rockbox 4.0 baseline, target, remote,
  firmware-owned surfaces, and validation boundary
- [`screenshots/`](screenshots/) — exact-dimension release-note proxies for WPS,
  menus, FM, recording, and remote
- [`submission.md`](submission.md) — current theme-site field requirements and
  the explicit reasons submission is not yet appropriate

The pre-final maximalist systems pass adds real main/remote FM RSSI rails,
native recording technical chrome, distinct external-power and disk-activity
states, exact sleep countdowns, transient volume, promoted control typography,
and larger selection prompts. Queue prototype A was selected: Cyan enables the
native playlist icon callback and translates its current-track value into a
large `NOW>` marker that remains independent of the navigation cursor.

The terminal/instrument refinement retains `>>` and `::`, replaces generic
branding footers with operational state/actions, establishes content/action/
technical header grammars, rebuilds FM as a communications-receiver panel,
strengthens native recording chrome, adds a 32-frame semantic list icon strip
and tactical FM/record/remote-lock assets, segments technical rules, and frames
QuickScreen's native directional control with short datum rails. Grayscale
dithering remains explicitly deferred beyond v0.1.

Build and verify the distribution from the repository root:

```sh
python3 tools/check-assets.py
python3 tools/check-screen-coverage.py
python3 tools/check-layout.py
python3 tools/check-screenshots.py
./tools/package-distribution.sh
```

## Theme-site decision

A formal theme-site upload package is intentionally not produced yet. The site
requires genuine Rockbox WPS/menu screenshots, successful server-side
validation/CheckWPS, and submitter identity/contact fields. Browser proxies do
not satisfy those requirements. Once genuine captures and submitter metadata
exist, the clean inner ZIP and metadata in [`submission.md`](submission.md) are
ready to populate the official upload form.
