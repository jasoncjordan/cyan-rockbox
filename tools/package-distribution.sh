#!/bin/sh
set -eu

distribution_root=$(CDPATH= cd -- "$(dirname -- "$0")/.." && pwd)
distribution_dir="$distribution_root/dist"
distribution_name="Cyan-0.1.0-h1x0-distribution"
distribution_file="$distribution_dir/$distribution_name.zip"
distribution_stage=$(mktemp -d)
distribution_python=${CYAN_PYTHON:-python3}

cleanup_distribution_stage() {
    rm -rf "$distribution_stage"
}
trap cleanup_distribution_stage EXIT HUP INT TERM

"$distribution_root/tools/package.sh"
"$distribution_python" "$distribution_root/tools/check-screenshots.py"

mkdir -p "$distribution_stage/$distribution_name/screenshots"
cp "$distribution_dir/Cyan-0.1.0-h1x0.zip" \
    "$distribution_stage/$distribution_name/"
cp "$distribution_root/LICENSE" \
    "$distribution_stage/$distribution_name/"
cp "$distribution_root/docs/installation.md" \
    "$distribution_stage/$distribution_name/INSTALLATION.md"
cp "$distribution_root/docs/compatibility.md" \
    "$distribution_stage/$distribution_name/COMPATIBILITY.md"
cp "$distribution_root/docs/release.md" \
    "$distribution_stage/$distribution_name/RELEASE-NOTES.md"
cp "$distribution_root/docs/final-validation.md" \
    "$distribution_stage/$distribution_name/final-validation.md"
cp "$distribution_root/docs/testing.md" \
    "$distribution_stage/$distribution_name/testing.md"
cp "$distribution_root/docs/screenshots/README.md" \
    "$distribution_stage/$distribution_name/screenshots/README.md"
cp "$distribution_root"/docs/screenshots/*.png \
    "$distribution_stage/$distribution_name/screenshots/"

(
    cd "$distribution_stage/$distribution_name"
    shasum -a 256 Cyan-0.1.0-h1x0.zip screenshots/*.png > SHA256SUMS
)

rm -f "$distribution_file"
(
    cd "$distribution_stage"
    zip -q -X -r "$distribution_file" "$distribution_name"
)
unzip -tq "$distribution_file" >/dev/null

echo "Created $distribution_file"
shasum -a 256 "$distribution_file"
