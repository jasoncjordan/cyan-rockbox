# Revised Milestone 0 completion report

Completed 2026-08-20 against the updated `PRD.md`, `HARDWARE.md`, all supplied
material under `reference/`, and current official Rockbox source and manual
material. This milestone changed research documentation only. No theme skin,
asset, package, or reference file was modified.

## Deliverable audit

| PRD deliverable | Result | Evidence |
|---|---|---|
| Repository scaffold | Complete | `src/h1x0/.rockbox/`, `tools/`, `docs/`, `dist/`, README, license, and ignore rules are separated by role. The install tree mirrors the player filesystem. |
| Screen matrix | Complete | [`screen-matrix.md`](screen-matrix.md) audits all 20 current `%cs` categories for H120 availability, theming route, type, status, screenshot, and physical-test state. |
| H1x0 capability matrix | Complete | [`h1x0-capabilities.md`](h1x0-capabilities.md) separates hardware support from verified skin exposure and records do-not-fake decisions. |
| Official Rockbox notes | Complete | [`rockbox-notes.md`](rockbox-notes.md) records current target facts, install paths, legal mechanisms, native-screen boundaries, remote roles, and validation routes. |
| Reference-theme inventory | Complete | [`reference-themes.md`](reference-themes.md) inventories every supplied archive and adds maintained upstream references for FM, remote, QuickScreen, lists, and package roles. |
| Simulator assessment | Complete | H120 UI-simulator and CheckWPS configuration commands, dependencies, value, and limitations are documented. Execution is an environment/physical-test gate, not silently claimed. |

## Research decisions that constrain later milestones

1. The H120 main LCD is 160×128×2 grayscale; the remote is a distinct
   128×64×1 surface. Main and remote skins must be authored and tested
   separately.
2. Rockbox has only three independent skin classes: SBS, WPS, and FMS. `%cs`
   detection does not grant control of a native screen's body.
3. Recording, QuickScreen, Pitch, System Info, Track Info, and similar utility
   screens remain native-first. Cyan may harmonize shared chrome and lists but
   must not duplicate firmware logic.
4. The H120 target supports recording from microphone, line, FM, and S/PDIF,
   plus S/PDIF output, but current general skin tags do not expose every state.
   Unsupported state must be omitted rather than inferred.
5. The target has no configured RTC. The global Time and Date `%cs` category
   stays in the audit, but it is not an H120 deliverable.
6. Current official QuickScreen name/value tags are verified, but no maintained
   bundled theme example was found. Its eventual design requires CheckWPS,
   simulator, and physical behavior validation.
7. Plugins generally own their runtime drawing. Cyan styles the plugin launcher
   and only those plugin surfaces that deliberately use native Rockbox UI.
8. Browser previews are useful layout proxies only. They do not validate skin
   syntax, LCD contrast, controls, the blue backlight, or device performance.

## Exit state

Revised Milestone 0 is complete as a research-and-matrix milestone. It does not
claim simulator or physical-device validation; those checkpoints remain
explicitly pending in the matrices. Existing visual implementation is retained
as project state, but no additional visual surface was built or revised while
closing this milestone.

The project can now resume revised Milestone 1 from the audited constraints.
