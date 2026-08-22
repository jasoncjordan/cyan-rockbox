# Revised Milestone 2 — Core WPS

Implementation snapshot: 2026-08-20. The current `PRD.md` remains
authoritative. Earlier WPS work already present in the repository was audited
against the revised milestone and retained where it satisfies the requirement.

## Requirement mapping

| PRD requirement | Cyan implementation | Verification state |
|---|---|---|
| Title | `%it` in an 18-Terminus-Bold viewport; `%fn` fallback | Source and browser proxy complete; physical pending |
| Artist | `%ia` in a 16-Terminus viewport; `Unknown Artist` fallback | Source and browser proxy complete; physical pending |
| Album | `%id` in a 12-Terminus viewport; `Unknown Album` fallback | Source and browser proxy complete; physical pending |
| Progress rail | Native `%pb`, 156×5 pixels, above elapsed/remaining time | Source and browser proxy complete; physical pending |
| Playback icon | Five-frame one-bit `%xl` strip selected by `%mp`; play centered in lower rail | Source and browser proxy complete; physical pending |
| Battery | Six-frame one-bit level strip selected by `%bl`, fixed at upper right | Source and browser proxy complete; physical pending |
| Pause state | `%mp` selects the distinct two-bar pause frame | Source and browser proxy complete; physical pending |
| Long-string handling | Separate `%s` viewports clip and scroll title, artist, and album independently | Source and browser proxy complete; physical pending |

## Frozen geometry

- Header: `x=0, y=0, w=160, h=16`, with `Now Playing` and fixed battery.
- Title: `x=2, y=20, w=156, h=22`.
- Artist: `x=2, y=45, w=156, h=18`.
- Album: `x=2, y=66, w=156, h=14`.
- Progress: `x=2, y=84, w=156, h=5`.
- Time: `y=94, h=12`.
- Playback state: centered in the bottom rail at `x=75, y=113`.

The progress rail stays above the time values, the header uses normal case, and
the playback icon stays at bottom center, preserving the previously approved
layout decisions.

## Browser review set

The browser proxy now exposes four Milestone 2 cases:

1. Playing — ordinary complete metadata and play state.
2. Paused — identical hierarchy with the two-bar pause state.
3. Long Text — deliberately oversized title, artist, and album values clipped
   to their independent firmware viewports.
4. Missing Tags — filename title fallback plus explicit unknown artist/album.

This proxy verifies geometry and one-bit asset silhouettes only. It cannot
prove Rockbox parsing, real scroll timing, physical contrast, or backlight-off
legibility.

## Exit gate

Implementation and browser review are ready. Revised Milestone 2 is not
physically complete until the WPS gate in [`testing.md`](testing.md) passes on
an H120/H140 with the optional font pack. Do not advance the physical-release
claim based only on the browser proxy.
