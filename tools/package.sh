#!/bin/sh
set -eu

repo_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
source_root="$repo_root/src/h1x0"
output_dir="$repo_root/dist"
output_file="$output_dir/Cyan-0.1.0-h1x0.zip"

required_files="
.rockbox/themes/Cyan.cfg
.rockbox/wps/Cyan.sbs
.rockbox/wps/Cyan.wps
.rockbox/wps/Cyan.fms
.rockbox/wps/Cyan.rfms
.rockbox/wps/Cyan.rwps
.rockbox/wps/Cyan.rsbs
.rockbox/wps/Cyan/battery.bmp
.rockbox/wps/Cyan/charging.bmp
.rockbox/wps/Cyan/powered.bmp
.rockbox/wps/Cyan/disk.bmp
.rockbox/wps/Cyan/hold.bmp
.rockbox/wps/Cyan/playback.bmp
.rockbox/wps/Cyan/repeat.bmp
.rockbox/wps/Cyan/seek.bmp
.rockbox/wps/Cyan/shuffle.bmp
.rockbox/wps/Cyan/sleep.bmp
.rockbox/wps/Cyan/remote-battery.bmp
.rockbox/wps/Cyan/remote-charging.bmp
.rockbox/wps/Cyan/remote-powered.bmp
.rockbox/wps/Cyan/remote-playback.bmp
.rockbox/wps/Cyan/fm-state.bmp
.rockbox/wps/Cyan/record-state.bmp
.rockbox/wps/Cyan/remote-hold.bmp
.rockbox/wps/Cyan/remote-fm-state.bmp
.rockbox/icons/Cyan-13.bmp
"

for relative_path in $required_files; do
    if [ ! -f "$source_root/$relative_path" ]; then
        echo "Missing release file: $relative_path" >&2
        exit 1
    fi
done

mkdir -p "$output_dir"
rm -f "$output_file"

(
    cd "$source_root"
    zip -q -X -r "$output_file" \
        .rockbox/themes/Cyan.cfg \
        .rockbox/wps/Cyan.sbs \
        .rockbox/wps/Cyan.wps \
        .rockbox/wps/Cyan.fms \
        .rockbox/wps/Cyan.rfms \
        .rockbox/wps/Cyan.rwps \
        .rockbox/wps/Cyan.rsbs \
        .rockbox/wps/Cyan \
        .rockbox/icons/Cyan-13.bmp
)

unzip -tq "$output_file" >/dev/null

echo "Created $output_file"
shasum -a 256 "$output_file"
