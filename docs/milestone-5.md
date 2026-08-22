# Revised Milestone 5 — H-Series media instrumentation

Implementation snapshot: 2026-08-20. This milestone uses the strongest native
surface available for each feature: a dedicated FMS for FM and native recorder
instrumentation inside Cyan's conditional SBS chrome.

## FM receiver

`Cyan.fms` provides `RADIO//`, large frequency, native preset identity,
regional-band tuner rail, scan/preset, tuned/search, stereo/mono, RDS text when
actually available, audio live/muted, signal strength, and battery/charging.
No station name is invented when neither a preset nor RDS exists.

## Recording

Rockbox does not define a recording skin class. Its native recorder already
owns recording time, size, filename, L/R peak meters, clipping, trigger state,
gain, AGC, pause/resume, and live S/PDIF input sample rate. Cyan reserves a
dense 12-Terminus instrument viewport and adds:

- `RECORD//` identity
- `SRC//` plus the real `rec source` setting
- real recording frequency and format settings
- `D.OUT` only when the real `spdif enable` setting is on
- the shared upper-right battery

Mic, Line, FM, and S/PDIF are therefore surfaced through Rockbox's own setting;
native controls and meters are not duplicated.

## S/PDIF boundary

The H120 target supports S/PDIF recording input, output, and controllable output
power. Current setting tags expose the selected S/PDIF recording source and the
output-enable setting. The theme does not claim lock quality or digital signal
presence because no verified skin tag exposes those states.

## Exit gate

Implementation and browser proxies are ready. Milestone 5 remains physically
pending until FM tuning, mute, stereo, signal, all available recording sources,
native peak/clipping behavior, and S/PDIF input/output reporting are exercised
on an H120/H140 using [`testing.md`](testing.md).

Sources: [current recording implementation](https://github.com/Rockbox/rockbox/blob/master/apps/recorder/recording.c),
[current settings definitions](https://github.com/Rockbox/rockbox/blob/master/apps/settings_list.c),
and [current theme tags](https://github.com/Rockbox/rockbox/blob/master/manual/appendix/wps_tags.tex).
