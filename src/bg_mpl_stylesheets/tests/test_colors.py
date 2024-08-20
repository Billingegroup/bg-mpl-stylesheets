import pytest

from bg_mpl_stylesheets.colors import Colors


@pytest.mark.parametrize(
    "hex, expected_hex",
    [
        (Colors.BG_BLUE, "#0B3C5D"),
        (Colors.BG_RED, "#B82601"),
        (Colors.BG_GREEN, "#1C6B0A"),
        (Colors.BG_LIGHT_BLUE, "#328CC1"),
        (Colors.BG_LIGHT_GREY, "#A8B6C1"),
        (Colors.BG_YELLOW, "#D9B310"),
        (Colors.BG_BROWN, "#6C5050"),
        (Colors.BG_BURGUNDY, "#76323F"),
        (Colors.BG_OLIVE_GREEN, "#626E60"),
        (Colors.BG_MUTED_OLIVE, "#918770"),
        (Colors.BG_BEIGE, "#C09F80"),
        (Colors.BG_GREY, "#B0B0B0FF"),
    ],
)
def test_color_values(hex, expected_hex):
    # Test the hex values of the colors
    assert hex == expected_hex


@pytest.mark.parametrize(
    "hex, expected_name",
    [
        (Colors.BG_BLUE, "BG_BLUE"),
        (Colors.BG_RED, "BG_RED"),
        (Colors.BG_GREEN, "BG_GREEN"),
        (Colors.BG_LIGHT_BLUE, "BG_LIGHT_BLUE"),
        (Colors.BG_LIGHT_GREY, "BG_LIGHT_GREY"),
        (Colors.BG_YELLOW, "BG_YELLOW"),
        (Colors.BG_BROWN, "BG_BROWN"),
        (Colors.BG_BURGUNDY, "BG_BURGUNDY"),
        (Colors.BG_OLIVE_GREEN, "BG_OLIVE_GREEN"),
        (Colors.BG_MUTED_OLIVE, "BG_MUTED_OLIVE"),
        (Colors.BG_BEIGE, "BG_BEIGE"),
        (Colors.BG_GREY, "BG_GREY"),
    ],
)
def test_get_color_name_from_hex(hex, expected_name):
    # Test retriving the color name based on the hex value
    assert Colors.get_color_name(hex) == expected_name


def test_get_color_name_from_hex_with_unknown_color():
    # Test returning ValueError when hex value is not in the Colors enum
    unknown_hex_value = "#123456"
    with pytest.raises(ValueError):
        Colors.get_color_name(unknown_hex_value)


def test_bg_colors():
    # Test the get_bg_colors function
    bg_colors = Colors.get_bg_colors()
    expected_colors = [
        Colors.BG_BLUE,
        Colors.BG_RED,
        Colors.BG_GREEN,
        Colors.BG_LIGHT_BLUE,
        Colors.BG_LIGHT_GREY,
        Colors.BG_YELLOW,
        Colors.BG_BROWN,
        Colors.BG_BURGUNDY,
        Colors.BG_OLIVE_GREEN,
        Colors.BG_MUTED_OLIVE,
        Colors.BG_BEIGE,
        Colors.BG_GREY,
    ]
    assert bg_colors == expected_colors
