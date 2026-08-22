# Revised Milestone 3 — Playback-state system

Implementation snapshot: 2026-08-20. The approved core WPS hierarchy and
geometry remain unchanged; Milestone 3 adds only conditional state treatment.

## Requirement mapping

| PRD requirement | Native mechanism | Cyan behavior | Verification |
|---|---|---|---|
| Transient volume | `%mv(2)`, `%pv` | Full bottom-rail meter for two seconds; normal icons hidden | Source/browser complete; physical pending |
| Fast-forward | `%mp` | `SEEK//FORWARD`, double-forward mark, five-pixel rail with straddling diamond | Source/browser complete; physical pending |
| Rewind | `%mp` | `SEEK//REWIND`, double-rewind mark, same seek rail | Source/browser complete; physical pending |
| Seek | `%pb` slider | Seven-pixel diamond overlaps both rail edges inside a one-pixel white separation border | Source/browser complete; physical pending |
| Shuffle | `%ps` | Compact crossing-arrow bitmap only while active | Source/browser complete; physical pending |
| Repeat | `%mm` | Distinct all, one, and A-B bitmap frames | Source/browser complete; physical pending |
| Hold | `%mh` | Compact padlock only while main Hold is active | Source/browser complete; physical pending |
| Sleep timer | `%bs` | Compact `Zzz` bitmap only while a timer is active | Source/browser complete; physical pending |
| Charging | `%bc` | Charging bitmap replaces the normal battery-level frame | Source/browser complete; H120 reporting pending |
| Up Next | `%pE(7)`, `%It/%Ia/%Fn` | Final seven seconds replace only album with next title/artist; no-next-track keeps album | Source/browser complete; physical pending |

## Native limitation recorded

The verified skin API reports whether main Hold is active but does not report
the activation edge or supply a Hold-specific timeout. Cyan therefore cannot
reliably show `LOCKED//` once and then collapse it. The compact active lock is
the conservative native implementation and does not permanently consume a row.

## Browser review set

The Milestone 3 proxy includes volume, seek forward, seek rewind, shuffle plus
repeat, repeat-one, repeat-A-B, Hold, sleep, charging, and Up Next alongside the
Milestone 2 playing/paused baselines.

## Exit gate

Implementation and browser review are ready. Milestone 3 remains physically
pending until every state is exercised on an H120/H140 using the checklist in
[`testing.md`](testing.md), including end-of-playlist behavior and actual
charging/Hold reporting.
