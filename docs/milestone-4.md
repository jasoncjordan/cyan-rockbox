# Revised Milestone 4 — Native playback support surfaces

Implementation snapshot: 2026-08-20. All five surfaces remain firmware-owned;
Cyan supplies only shared SBS chrome, list geometry, typography, and selection
language.

## Requirement mapping

| Surface | Cyan treatment | Native behavior preserved | Verification |
|---|---|---|---|
| Current Playlist | `QUEUE//`, 14-Terminus, `%LN` numbering, inverse selected row | Rockbox order, edits, queued state, and bracketed current-playing entry | Source/browser complete; physical pending |
| Track Info | `[ TRACK//INFO ]`, dense 12-Terminus rows, `>>`/`::`, technical footer | Native metadata fields, omission rules, scrolling, refresh, and navigation | Source/browser complete; physical pending |
| Context Menu | `ACTION//`, command-palette prompts, inverse selection | Native action names, availability, execution, and cancel behavior | Source/browser complete; physical pending |
| Playlist Catalogue | `PLAYLISTS//`, normal readable list treatment | Playlist names, catalogue operations, and navigation | Source/browser complete; physical pending |
| Shortcuts | `SHORTCUTS//`, command-palette prompts, inverse selection | User-configured names, targets, order, and execution | Source/browser complete; physical pending |

## Queue state distinction

Current Rockbox source tracks the playing row independently from the selected
row. The playlist text callback wraps the playing track in `[` and `]`, while
the list engine separately exposes the selected cursor through `%Lc`. Cyan
therefore shows both states without hard-coding playlist indices or forcing the
user's playlist-icon setting:

- bracketed row — currently playing
- full-width inverse row with `>` — current cursor/selection

The native icon callback also exposes current, moving, and queued icons, but
Cyan does not depend on it because the flagship browser intentionally keeps
global icons disabled.

[Current playlist viewer implementation](https://github.com/Rockbox/rockbox/blob/master/apps/playlist_viewer.c)
and [current list skin tags](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex).

## Track Info boundary

Track Info is not a second WPS. `ON + MODE` opens Rockbox's native screen while
playback continues; `LEFT` or `OFF` returns. Cyan does not force the optional
WPS hotkey or reproduce the firmware's metadata callbacks.

## Exit gate

Implementation and browser review are ready. Milestone 4 remains physically
pending until all five screens pass the native-support checklist in
[`testing.md`](testing.md), including edits, cancel/back, track changes, long
metadata, and user-defined shortcuts.
