#!/usr/bin/env python3
"""Generate Cyan// target bitmaps from documented pixel primitives."""

from pathlib import Path

from PIL import Image, ImageDraw


ROOT = Path(__file__).resolve().parents[1]
OUTPUT = ROOT / "src/h1x0/.rockbox/wps/Cyan"
ICON_OUTPUT = ROOT / "src/h1x0/.rockbox/icons"
FRAME_WIDTH = 11
FRAME_HEIGHT = 11
REMOTE_FRAME_WIDTH = 9
REMOTE_FRAME_HEIGHT = 9


def frame(index):
    """Return the vertical origin of one strip frame."""
    return index * FRAME_HEIGHT


def generate_playback_strip():
    """Create stop, play, pause, fast-forward, and rewind frames."""
    image = Image.new("1", (FRAME_WIDTH, FRAME_HEIGHT * 5), 1)
    draw = ImageDraw.Draw(image)

    y = frame(0)
    draw.rectangle((3, y + 3, 7, y + 7), fill=0)

    y = frame(1)
    draw.polygon(((2, y + 1), (2, y + 9), (9, y + 5)), fill=0)

    y = frame(2)
    draw.rectangle((2, y + 1, 4, y + 9), fill=0)
    draw.rectangle((7, y + 1, 9, y + 9), fill=0)

    y = frame(3)
    draw.polygon(((0, y + 1), (0, y + 9), (5, y + 5)), fill=0)
    draw.polygon(((5, y + 1), (5, y + 9), (10, y + 5)), fill=0)

    y = frame(4)
    draw.polygon(((5, y + 5), (10, y + 1), (10, y + 9)), fill=0)
    draw.polygon(((0, y + 5), (5, y + 1), (5, y + 9)), fill=0)

    OUTPUT.mkdir(parents=True, exist_ok=True)
    image.save(OUTPUT / "playback.bmp")


def battery_outline(draw, y, fill_width=0):
    """Draw an 18x7 terminal-shaped battery and an optional interior fill."""
    draw.rectangle((0, y, 15, y + 6), outline=0)
    draw.rectangle((16, y + 2, 17, y + 4), fill=0)
    if fill_width:
        draw.rectangle((2, y + 2, 1 + fill_width, y + 4), fill=0)


def generate_battery_strip():
    """Create unknown, empty, 25, 50, 75, and full battery frames."""
    width, height = 18, 7
    image = Image.new("1", (width, height * 6), 1)
    draw = ImageDraw.Draw(image)
    for index, fill_width in enumerate((0, 0, 3, 6, 9, 12)):
        y = index * height
        battery_outline(draw, y, fill_width)
    # Unknown-level mark in the first frame.
    draw.point((7, 2), fill=0)
    draw.point((8, 1), fill=0)
    draw.point((9, 2), fill=0)
    draw.point((8, 3), fill=0)
    draw.point((8, 5), fill=0)
    image.save(OUTPUT / "battery.bmp")


def generate_charging_icon():
    image = Image.new("1", (18, 7), 1)
    draw = ImageDraw.Draw(image)
    battery_outline(draw, 0)
    draw.line(((9, 1), (6, 3), (9, 3), (7, 5)), fill=0)
    image.save(OUTPUT / "charging.bmp")


def generate_powered_icon():
    """Create a distinct external-power/fully-fed battery state."""
    image = Image.new("1", (18, 7), 1)
    draw = ImageDraw.Draw(image)
    battery_outline(draw, 0, 12)
    # White notch makes this distinguishable from both charging and 100%.
    draw.rectangle((7, 2, 9, 4), fill=1)
    draw.line(((8, 1), (6, 3), (8, 3), (7, 5)), fill=0)
    image.save(OUTPUT / "powered.bmp")


def generate_disk_icon():
    """Create a terse 5x5 disk-activity pulse for SBS technical chrome."""
    image = Image.new("1", (5, 5), 1)
    draw = ImageDraw.Draw(image)
    draw.rectangle((0, 0, 4, 4), outline=0)
    draw.point((2, 2), fill=0)
    draw.line(((1, 4), (3, 4)), fill=0)
    image.save(OUTPUT / "disk.bmp")


def generate_repeat_strip():
    """Create repeat-all, repeat-one, and repeat-A-B frames."""
    width, height = 13, 9
    image = Image.new("1", (width, height * 3), 1)
    draw = ImageDraw.Draw(image)
    for index in range(3):
        y = index * height
        draw.line(((2, y + 1), (10, y + 1), (12, y + 3)), fill=0)
        draw.line(((10, y + 7), (2, y + 7), (0, y + 5)), fill=0)
    # Repeat-one mark.
    y = height
    draw.line(((6, y + 3), (6, y + 6)), fill=0)
    # A-B range mark in the third frame.
    y = height * 2
    draw.line(((4, y + 3), (4, y + 5)), fill=0)
    draw.line(((8, y + 3), (8, y + 5)), fill=0)
    draw.line(((4, y + 4), (8, y + 4)), fill=0)
    image.save(OUTPUT / "repeat.bmp")


def generate_sleep_icon():
    """Create a compact bitmap-rendered Zzz sleep-timer mark."""
    image = Image.new("1", (13, 9), 1)
    draw = ImageDraw.Draw(image)
    # Five-pixel capital Z.
    draw.line(((0, 1), (4, 1)), fill=0)
    draw.line(((4, 1), (0, 7)), fill=0)
    draw.line(((0, 7), (4, 7)), fill=0)
    # Two compact lowercase z glyphs.
    for x in (6, 10):
        draw.line(((x, 3), (x + 2, 3)), fill=0)
        draw.line(((x + 2, 3), (x, 7)), fill=0)
        draw.line(((x, 7), (x + 2, 7)), fill=0)
    image.save(OUTPUT / "sleep.bmp")


def generate_hold_icon():
    """Create a compact padlock for the main-unit Hold switch."""
    image = Image.new("1", (9, 9), 1)
    draw = ImageDraw.Draw(image)
    draw.line(((2, 4), (2, 2), (3, 1), (5, 1), (6, 2), (6, 4)), fill=0)
    draw.rectangle((1, 4, 7, 8), outline=0)
    draw.point((4, 6), fill=0)
    image.save(OUTPUT / "hold.bmp")


def generate_shuffle_icon():
    image = Image.new("1", (13, 9), 1)
    draw = ImageDraw.Draw(image)
    draw.line(((0, 1), (3, 1), (9, 7), (12, 7)), fill=0)
    draw.line(((0, 7), (3, 7), (9, 1), (12, 1)), fill=0)
    draw.line(((10, 0), (12, 1), (10, 2)), fill=0)
    draw.line(((10, 6), (12, 7), (10, 8)), fill=0)
    image.save(OUTPUT / "shuffle.bmp")


def generate_seek_slider():
    # The black diamond remains seven pixels high. Its 9x9 white bitmap field
    # clears one pixel around it, separating it from the progress fill. Two
    # pixels of the rail's upper and lower borders enter from each side before
    # stopping at that white edge, visually seating the marker in the rail.
    image = Image.new("1", (9, 9), 1)
    draw = ImageDraw.Draw(image)
    draw.line(((0, 2), (1, 2)), fill=0)
    draw.line(((7, 2), (8, 2)), fill=0)
    draw.line(((0, 6), (1, 6)), fill=0)
    draw.line(((7, 6), (8, 6)), fill=0)
    draw.polygon(((4, 1), (7, 4), (4, 7), (1, 4)), fill=0)
    image.save(OUTPUT / "seek.bmp")


def generate_remote_playback_strip():
    """Create compact stop/play/pause/seek frames for the 128x64 remote."""
    image = Image.new(
        "1", (REMOTE_FRAME_WIDTH, REMOTE_FRAME_HEIGHT * 5), 1
    )
    draw = ImageDraw.Draw(image)

    y = 0
    draw.rectangle((3, y + 3, 6, y + 6), fill=0)

    y = REMOTE_FRAME_HEIGHT
    draw.polygon(((2, y + 1), (2, y + 7), (7, y + 4)), fill=0)

    y = REMOTE_FRAME_HEIGHT * 2
    draw.rectangle((2, y + 1, 3, y + 7), fill=0)
    draw.rectangle((6, y + 1, 7, y + 7), fill=0)

    y = REMOTE_FRAME_HEIGHT * 3
    draw.polygon(((0, y + 1), (0, y + 7), (4, y + 4)), fill=0)
    draw.polygon(((4, y + 1), (4, y + 7), (8, y + 4)), fill=0)

    y = REMOTE_FRAME_HEIGHT * 4
    draw.polygon(((4, y + 4), (8, y + 1), (8, y + 7)), fill=0)
    draw.polygon(((0, y + 4), (4, y + 1), (4, y + 7)), fill=0)
    image.save(OUTPUT / "remote-playback.bmp")


def generate_remote_battery_strip():
    """Create six 14x7 battery frames sized for the remote header."""
    width, height = 14, 7
    image = Image.new("1", (width, height * 6), 1)
    draw = ImageDraw.Draw(image)
    for index, fill_width in enumerate((0, 0, 2, 4, 6, 8)):
        y = index * height
        draw.rectangle((0, y, 11, y + 6), outline=0)
        draw.rectangle((12, y + 2, 13, y + 4), fill=0)
        if fill_width:
            draw.rectangle((2, y + 2, 1 + fill_width, y + 4), fill=0)
    draw.point((5, 2), fill=0)
    draw.point((6, 1), fill=0)
    draw.point((7, 2), fill=0)
    draw.point((6, 3), fill=0)
    draw.point((6, 5), fill=0)
    image.save(OUTPUT / "remote-battery.bmp")


def remote_battery_outline(draw, fill_width=0):
    draw.rectangle((0, 0, 11, 6), outline=0)
    draw.rectangle((12, 2, 13, 4), fill=0)
    if fill_width:
        draw.rectangle((2, 2, 1 + fill_width, 4), fill=0)


def generate_remote_charging_icon():
    image = Image.new("1", (14, 7), 1)
    draw = ImageDraw.Draw(image)
    remote_battery_outline(draw)
    draw.line(((7, 1), (5, 3), (7, 3), (6, 5)), fill=0)
    image.save(OUTPUT / "remote-charging.bmp")


def generate_remote_powered_icon():
    image = Image.new("1", (14, 7), 1)
    draw = ImageDraw.Draw(image)
    remote_battery_outline(draw, 8)
    draw.rectangle((5, 2, 7, 4), fill=1)
    draw.line(((6, 1), (4, 3), (6, 3), (5, 5)), fill=0)
    image.save(OUTPUT / "remote-powered.bmp")


def generate_fm_state_strip():
    """Create lock, search, stereo, and mono receiver-state frames."""
    size = 13
    image = Image.new("1", (size, size * 4), 1)
    draw = ImageDraw.Draw(image)
    # Lock: receiver reticle with a solid acquired center.
    y = 0
    draw.rectangle((2, y + 2, 10, y + 10), outline=0)
    draw.line(((6, y), (6, y + 3)), fill=0)
    draw.line(((6, y + 9), (6, y + 12)), fill=0)
    draw.rectangle((5, y + 5, 7, y + 7), fill=0)
    # Search: opposing scan arrows.
    y = size
    draw.line(((1, y + 4), (10, y + 4)), fill=0)
    draw.line(((8, y + 2), (10, y + 4), (8, y + 6)), fill=0)
    draw.line(((11, y + 9), (2, y + 9)), fill=0)
    draw.line(((4, y + 7), (2, y + 9), (4, y + 11)), fill=0)
    # Stereo: paired linked channels.
    y = size * 2
    draw.rectangle((1, y + 3, 5, y + 9), outline=0)
    draw.rectangle((7, y + 3, 11, y + 9), outline=0)
    draw.line(((5, y + 6), (7, y + 6)), fill=0)
    # Mono: one centered channel.
    y = size * 3
    draw.rectangle((3, y + 2, 9, y + 10), outline=0)
    draw.line(((5, y + 4), (7, y + 8)), fill=0)
    draw.line(((7, y + 4), (5, y + 8)), fill=0)
    image.save(OUTPUT / "fm-state.bmp")


def generate_record_state_strip():
    """Create prominent record-active and record-paused frames."""
    size = 13
    image = Image.new("1", (size, size * 2), 1)
    draw = ImageDraw.Draw(image)
    draw.ellipse((2, 2, 10, 10), fill=0)
    y = size
    draw.rectangle((2, y + 2, 5, y + 10), fill=0)
    draw.rectangle((8, y + 2, 11, y + 10), fill=0)
    image.save(OUTPUT / "record-state.bmp")


def generate_remote_hold_strip():
    """Create main- and remote-unit lock frames for the remote LCD."""
    size = 9
    image = Image.new("1", (size, size * 2), 1)
    draw = ImageDraw.Draw(image)
    for index in range(2):
        y = index * size
        draw.line(((2, y + 4), (2, y + 2), (3, y + 1),
                   (5, y + 1), (6, y + 2), (6, y + 4)), fill=0)
        draw.rectangle((1, y + 4, 7, y + 8), outline=0)
    draw.line(((3, 6), (5, 6)), fill=0)
    y = size
    draw.rectangle((3, y + 6, 5, y + 7), fill=0)
    image.save(OUTPUT / "remote-hold.bmp")


def generate_remote_fm_state_strip():
    """Create compact lock/search/stereo/mono receiver frames."""
    size = 9
    image = Image.new("1", (size, size * 4), 1)
    draw = ImageDraw.Draw(image)
    draw.rectangle((1, 1, 7, 7), outline=0)
    draw.rectangle((3, 3, 5, 5), fill=0)
    y = size
    draw.line(((0, y + 3), (7, y + 3), (5, y + 1)), fill=0)
    draw.line(((8, y + 6), (1, y + 6), (3, y + 8)), fill=0)
    y = size * 2
    draw.rectangle((0, y + 2, 3, y + 7), outline=0)
    draw.rectangle((5, y + 2, 8, y + 7), outline=0)
    y = size * 3
    draw.rectangle((2, y + 1, 6, y + 7), outline=0)
    image.save(OUTPUT / "remote-fm-state.bmp")


def generate_list_icon_strip():
    """Create the 32 Rockbox themable icons on a large 13-pixel grid."""
    size, count = 13, 32
    image = Image.new("1", (size, size * count), 1)
    draw = ImageDraw.Draw(image)

    def y(index, offset=0):
        return index * size + offset

    # Audio, folder, playlist, cursor, and WPS.
    draw.line(((7, y(0, 2)), (7, y(0, 9))), fill=0)
    draw.line(((7, y(0, 2)), (11, y(0, 3))), fill=0)
    draw.ellipse((3, y(0, 8), 7, y(0, 11)), fill=0)
    draw.polygon(((1, y(1, 4)), (4, y(1, 4)), (5, y(1, 2)),
                  (11, y(1, 2)), (11, y(1, 10)), (1, y(1, 10))), outline=0)
    for off in (3, 6, 9):
        draw.line(((2, y(2, off)), (10, y(2, off))), fill=0)
    draw.polygon(((2, y(3, 2)), (2, y(3, 10)), (10, y(3, 6))), fill=0)
    draw.polygon(((3, y(4, 2)), (3, y(4, 10)), (10, y(4, 6))), outline=0)
    # Firmware, font, language, config, plugin, bookmark, preset.
    draw.rectangle((2, y(5, 2), 10, y(5, 10)), outline=0)
    for off in (3, 6, 9):
        draw.point((0, y(5, off)), fill=0); draw.point((12, y(5, off)), fill=0)
    draw.line(((2, y(6, 10)), (6, y(6, 2)), (10, y(6, 10))), fill=0)
    draw.line(((4, y(6, 7)), (8, y(6, 7))), fill=0)
    draw.line(((3, y(7, 2)), (3, y(7, 10)), (10, y(7, 10))), fill=0)
    for x, h in ((2, 7), (6, 4), (10, 9)):
        draw.line(((x, y(8, 2)), (x, y(8, 10))), fill=0)
        draw.rectangle((x - 1, y(8, h), x + 1, y(8, h + 2)), fill=0)
    draw.rectangle((3, y(9, 2), 9, y(9, 7)), outline=0)
    draw.line(((5, y(9, 7)), (5, y(9, 11))), fill=0)
    draw.line(((8, y(9, 7)), (8, y(9, 11))), fill=0)
    draw.polygon(((3, y(10, 2)), (9, y(10, 2)), (8, y(10, 11)),
                  (6, y(10, 8)), (4, y(10, 11))), outline=0)
    draw.line(((6, y(11, 3)), (6, y(11, 10))), fill=0)
    draw.line(((2, y(11, 7)), (6, y(11, 3)), (10, y(11, 7))), fill=0)
    # Queued, moving, keyboard, reverse cursor, question.
    draw.rectangle((1, y(12, 3), 8, y(12, 10)), outline=0)
    draw.line(((9, y(12, 4)), (12, y(12, 4))), fill=0)
    draw.line(((10, y(12, 2)), (10, y(12, 6))), fill=0)
    draw.line(((1, y(13, 6)), (11, y(13, 6))), fill=0)
    draw.polygon(((1, y(13, 6)), (4, y(13, 3)), (4, y(13, 9))), fill=0)
    draw.polygon(((11, y(13, 6)), (8, y(13, 3)), (8, y(13, 9))), fill=0)
    draw.rectangle((1, y(14, 3), 11, y(14, 10)), outline=0)
    for x in (3, 6, 9):
        draw.point((x, y(14, 6)), fill=0)
    draw.polygon(((11, y(15, 2)), (11, y(15, 10)), (3, y(15, 6))), fill=0)
    draw.arc((2, y(16, 1), 10, y(16, 8)), 190, 520, fill=0)
    draw.point((6, y(16, 11)), fill=0)
    # Setting, function, submenu states, record, voice.
    for off in (3, 6, 9):
        draw.line(((2, y(17, off)), (10, y(17, off))), fill=0)
    draw.rectangle((6, y(17, 5), 8, y(17, 7)), fill=0)
    draw.line(((2, y(18, 9)), (9, y(18, 9)), (9, y(18, 3))), fill=0)
    draw.polygon(((9, y(18, 3)), (6, y(18, 5)), (11, y(18, 6))), fill=0)
    draw.polygon(((3, y(19, 2)), (3, y(19, 10)), (10, y(19, 6))), outline=0)
    draw.polygon(((2, y(20, 3)), (10, y(20, 3)), (6, y(20, 10))), outline=0)
    draw.ellipse((2, y(21, 2), 10, y(21, 10)), fill=0)
    draw.ellipse((4, y(22, 1), 8, y(22, 7)), outline=0)
    draw.line(((2, y(22, 6)), (2, y(22, 8)), (6, y(22, 11)),
               (10, y(22, 8)), (10, y(22, 6))), fill=0)
    # General/system/playback/display/remote/radio/file/EQ/Rockbox.
    draw.rectangle((3, y(23, 3), 9, y(23, 9)), outline=0)
    for x, yy in ((6, 1), (6, 11), (1, 6), (11, 6)):
        draw.point((x, y(23, yy)), fill=0)
    draw.rectangle((2, y(24, 2), 10, y(24, 10)), outline=0)
    draw.rectangle((5, y(24, 5), 7, y(24, 7)), fill=0)
    draw.polygon(((3, y(25, 2)), (3, y(25, 10)), (10, y(25, 6))), fill=0)
    draw.rectangle((1, y(26, 2), 11, y(26, 9)), outline=0)
    draw.line(((4, y(26, 11)), (8, y(26, 11))), fill=0)
    draw.rectangle((2, y(27, 3), 10, y(27, 8)), outline=0)
    draw.line(((5, y(27, 10)), (7, y(27, 10))), fill=0)
    draw.line(((6, y(28, 3)), (6, y(28, 10))), fill=0)
    draw.line(((2, y(28, 7)), (6, y(28, 3)), (10, y(28, 7))), fill=0)
    draw.arc((2, y(28, 5), 10, y(28, 12)), 200, 340, fill=0)
    draw.polygon(((1, y(29, 4)), (4, y(29, 4)), (5, y(29, 2)),
                  (11, y(29, 2)), (11, y(29, 10)), (1, y(29, 10))), outline=0)
    for x, h in ((2, 7), (5, 3), (8, 5), (11, 1)):
        draw.rectangle((x, y(30, h), x + 1, y(30, 11)), fill=0)
    draw.rectangle((2, y(31, 2), 10, y(31, 10)), outline=0)
    draw.line(((4, y(31, 9)), (4, y(31, 4)), (8, y(31, 4)),
               (8, y(31, 6)), (4, y(31, 6)), (9, y(31, 10))), fill=0)

    ICON_OUTPUT.mkdir(parents=True, exist_ok=True)
    image.save(ICON_OUTPUT / "Cyan-13.bmp")


if __name__ == "__main__":
    generate_playback_strip()
    generate_battery_strip()
    generate_charging_icon()
    generate_powered_icon()
    generate_disk_icon()
    generate_repeat_strip()
    generate_sleep_icon()
    generate_hold_icon()
    generate_shuffle_icon()
    generate_seek_slider()
    generate_remote_playback_strip()
    generate_remote_battery_strip()
    generate_remote_charging_icon()
    generate_remote_powered_icon()
    generate_fm_state_strip()
    generate_record_state_strip()
    generate_remote_hold_strip()
    generate_remote_fm_state_strip()
    generate_list_icon_strip()
