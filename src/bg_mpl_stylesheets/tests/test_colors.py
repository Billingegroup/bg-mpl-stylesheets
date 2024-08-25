import pytest

from bg_mpl_stylesheets.colors import Colors


@pytest.mark.parametrize(
    "hex, expected_hex",
    [
        (Colors.bg_blue, "#0B3C5D"),
        (Colors.bg_red, "#B82601"),
        (Colors.bg_green, "#1C6B0A"),
        (Colors.bg_light_blue, "#328CC1"),
        (Colors.bg_light_grey, "#A8B6C1"),
        (Colors.bg_yellow, "#D9B310"),
        (Colors.bg_brown, "#6C5050"),
        (Colors.bg_burgundy, "#76323F"),
        (Colors.bg_olive_green, "#626E60"),
        (Colors.bg_muted_olive, "#918770"),
        (Colors.bg_beige, "#C09F80"),
        (Colors.bg_grey, "#B0B0B0FF"),
    ],
)
def test_color_values(hex, expected_hex):
    # Test the hex values of the colors
    assert hex == expected_hex


def test_bg_colors():
    # Test the get_bg_colors function
    bg_colors = Colors.get_bg_colors()
    expected_colors = [
        Colors.bg_blue,
        Colors.bg_red,
        Colors.bg_green,
        Colors.bg_light_blue,
        Colors.bg_light_grey,
        Colors.bg_yellow,
        Colors.bg_brown,
        Colors.bg_burgundy,
        Colors.bg_olive_green,
        Colors.bg_muted_olive,
        Colors.bg_beige,
        Colors.bg_grey,
    ]
    assert bg_colors == expected_colors
