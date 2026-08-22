# Rockbox theme-site submission readiness

Research checked against the current Rockbox theme-site source on 2026-08-20.

The upload workflow requires:

- theme name and target device
- real author name and contact email
- description and attribution for reused assets
- main theme ZIP
- WPS screenshot in PNG format at the exact LCD dimensions
- optional menu/additional screenshots at the exact LCD dimensions
- acceptance of CC BY-SA 3.0
- successful server-side ZIP validation and CheckWPS

Official source:

- [upload form](https://github.com/Rockbox/themesite/blob/master/private/templates/upload.tpl)
- [validation implementation](https://github.com/Rockbox/themesite/blob/master/www/upload.php)

## Cyan// readiness

- Name: `Cyan//`
- Target: iRiver H120/H140, `iriverh120`, 160×128×2
- License: CC BY-SA 3.0
- Original assets: generated in this repository; no reference-theme bitmap is
  redistributed
- Candidate ZIP: `dist/Cyan-0.1.0-h1x0.zip`
- Supported baseline: official Rockbox 4.0, target `iriverh120`
- Suggested description: “Large-type, high-contrast, TUI-inspired theme for
  the iRiver H120/H140. Prioritizes readable browsing and a sparse Now Playing
  hierarchy with functional one-bit status graphics.”

## Submission blockers

Do not upload yet. The current browser images are labeled design proxies, not
Rockbox simulator or physical-device screenshots. Produce genuine 160×128 PNG
screenshots after CheckWPS and simulator/device validation, then record the
author name and email supplied by the person submitting the theme.

The exact-dimension files under `docs/screenshots/` are explicitly named
`browser-proxy` and are distribution illustrations only. They must not be
renamed or presented as simulator/device evidence.
