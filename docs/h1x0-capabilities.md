# Cyan// H120/H140 capability matrix

Research snapshot: 2026-08-20. Hardware support is taken from the current
`iriverh120` target configuration and the project hardware brief. “Skin
exposure” distinguishes a real theme tag/screen from a setting that Rockbox can
use internally but a theme cannot directly inspect.

| Capability | Hardware / Rockbox support | Skin exposure | Cyan// decision | Priority / status |
|---|---|---|---|---|
| Main LCD | 160×128, 2-bit grayscale, vertical packing | Main `.sbs`, `.wps`, `.fms` and shared tags | Flagship geometry; pure high-contrast grayscale | P0, implemented for SBS/WPS |
| Blue backlight | Hardware backlight; PWM fading | No color tag required; normal backlight settings remain native | Treat physical blue as Cyan identity; test on/off and varied ambient light | P0, physical test pending |
| LCD inversion | `HAVE_LCD_INVERT` | User setting, not a theme state Cyan should force | Test both modes and document recommendation | P3, pending |
| LCD contrast | `HAVE_LCD_CONTRAST`, range 14–63, default 27 | Native setting; not forced by theme | Test readability across reasonable values | P3, pending |
| Remote LCD | 128×64, 1-bit, vertical packing | `rwps`, `rsbs`, remote font and remote status-bar settings | Dedicated 10-ProFont RWPS plus five-row RSBS; never scale the main skin | P2 / Milestone 6, implemented pending hardware |
| Main Hold | Physical Hold switch | `%mh`; no verified activation-timer tag | Compact lock state while active; do not fake a one-shot transient | P1 / Milestone 3, implemented pending hardware |
| Remote Hold | Remote driver reports remote hold | `%mr`; main Hold remains `%mh` | Show explicit `R.HOLD` versus `M.HOLD`, with remote state taking display priority | P2 / Milestone 6, implemented pending validation |
| FM tuner | TEA5767 tuner | Dedicated `.fms`; tuned, mode, stereo, frequency, preset, RDS and RSSI tags | `RADIO//`; never fabricate RDS/preset names | P2 / Milestone 5, implemented pending hardware |
| Recording | `HAVE_RECORDING`, AGC and histogram support | `%cs=3`; native recorder owns time, size, meters, clipping, trigger, gain, AGC and filename | Dense `RECORD//` SBS viewport; preserve native instrumentation | P2 / Milestone 5, implemented to native boundary pending hardware |
| Microphone input | `SRC_CAP_MIC` | `%St(rec source)` plus native recorder | Surface the real selected source | P2, implemented pending hardware |
| Line input | `SRC_CAP_LINEIN` | `%St(rec source)` plus native recorder | Surface the real selected source | P2, implemented pending hardware |
| FM recording input | `SRC_CAP_FMRADIO` | `%St(rec source)` plus native recorder | Surface the real selected source | P2, implemented pending hardware |
| S/PDIF recording input | `SRC_CAP_SPDIF` | `%St(rec source)`; native recorder exposes live S/PDIF sample rate | Show selected digital input without claiming signal lock | P2, implemented to exposed boundary pending hardware |
| S/PDIF output | `HAVE_SPDIF_OUT` and controllable power | `%St(spdif enable)` | Show `D.OUT` only when the output-enable setting is on | P2, implemented pending hardware |
| Sample rates | Playback supports 44.1/22.05/11.025 kHz; recording supports same mask | File frequency `%ff/%fk`; native recorder settings/body | Track Info remains native; recorder display only where exposed | P0 technical / P2 recording |
| Battery level | Voltage-measured battery model | `%bl`, `%bv`, `%bt` | Graphical level on everyday screens; detailed values only on technical screens | P0, graphical level implemented |
| Charging | Simple hardware-controlled charging | `%bp`; `%bc` may depend on software charge reporting and must be physically verified | Charging image already implemented; verify actual H120 reporting | P1, implemented pending hardware |
| Sleep timer | Rockbox feature | `%bs` remaining time | Compact bitmap mark only while active | P1 / Milestone 3, implemented pending hardware |
| Disk storage/activity | ATA, LBA48, disk storage, ATA LED control | `%lh` virtual LED | Tiny activity indicator only on technical/system surfaces unless unobtrusive | P3, pending |
| QuickScreen | `HAVE_QUICKSCREEN` | `%cs=10`, themed UI viewport, and four name/value tag pairs | Preserve native four-way behavior inside `QUICK//` chrome | P2 / Milestone 7, implemented pending hardware |
| Programmable hotkey | `HAVE_HOTKEY`; short `REC` in WPS | WPS hotkey is a user setting, not a visual tag | Never force it; document optional Show Track Info assignment | P0 policy, complete |
| A-B repeat | `AB_REPEAT_ENABLE` | `%mm` includes A-B; WPS actions exist | Dedicated third repeat-strip frame | P1 / Milestone 3, implemented pending hardware |
| Peak meters | Firmware peak-meter support; recorder draws native L/R meters, clip counter and trigger | Recorder-owned instrumentation inside Cyan viewport | Preserve native refresh and controls | P2 / Milestone 5, integrated pending hardware |
| Database | Tag cache enabled | Normal database list and metadata tags | `MUSIC//`/native contextual browser | P0, implemented generically |
| Album art/JPEG | Album art, bitmap scaling and JPEG decoding enabled | Album-art tags | Deliberately omitted from flagship WPS unless later testing justifies it | Non-goal for current WPS |
| Plugins | 512 KiB plugin buffer; plugin framework | Plugin browser is a normal list; runtime normally plugin-owned; current Pitch is `pitch_screen.rock` | Style `TOOLS//` launcher; document external runtime surfaces and native Pitch | P3 / Milestone 7, complete to native boundary |
| RTC / clock | No `CONFIG_RTC` in current H120 target config | `%cs=17` exists globally but should not occur on this target | Retain conditional `CLOCK//` compatibility chrome; do not invent an H120 clock body | Unavailable and documented |
| Backlight-off power use | Hardware-supported display remains visible without backlight | Not a skin tag | Physical contrast test remains mandatory | P0, pending |

## Confirmed native-first boundaries

1. Cyan can fully supply WPS and FM skins and shared SBS/list styling.
2. Recording, Pitch, Time/Date, and many utility bodies are native screens;
   `%cs` can select surrounding Cyan chrome but does not grant arbitrary body
   replacement.
3. S/PDIF capability is real hardware support, but no current general skin tag
   has yet been verified for digital input/output state.
4. Cyan must not write the WPS hotkey or force contrast/inversion settings.

## Sources

- [H120/H140 target configuration](https://github.com/Rockbox/rockbox/blob/master/firmware/export/config/iriverh120.h)
- [Current theme-tag appendix](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex)
- [H1x0 button implementation](https://github.com/Rockbox/rockbox/blob/master/firmware/target/coldfire/iriver/h100/button-h100.c)
