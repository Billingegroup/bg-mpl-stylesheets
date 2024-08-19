import pytest

from bg_mpl_stylesheets.colors import Colors


@pytest.mark.parametrize(
    "color, expected_hex",
    [
        (Colors.BG_BLUE, "#0B3C5D"),
        (Colors.BG_RED, "#B82601"),
        (Colors.BG_GREEN, "#1c6b0a"),
        (Colors.BG_LIGHT_BLUE, "#328CC1"),
        (Colors.BG_LIGHT_GREY, "#a8b6c1"),
        (Colors.BG_YELLOW, "#D9B310"),
        (Colors.BG_BROWN, "#6C5050"),
        (Colors.BG_BURGUNDY, "#76323F"),
        (Colors.BG_OLIVE_GREEN, "#626E60"),
        (Colors.BG_MUTED_OLIVE, "#918770"),
        (Colors.BG_BEIGE, "#C09F80"),
        (Colors.BG_GREY, "#b0b0b0ff"),
    ],
)
def test_color_values(color, expected_hex):
    assert color == expected_hex


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
