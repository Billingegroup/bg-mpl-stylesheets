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


@pytest.mark.parametrize(
    "hex, expected_name",
    [
        (Colors.bg_blue, "bg_blue"),
        (Colors.bg_red, "bg_red"),
        (Colors.bg_green, "bg_green"),
        (Colors.bg_light_blue, "bg_light_blue"),
        (Colors.bg_light_grey, "bg_light_grey"),
        (Colors.bg_yellow, "bg_yellow"),
        (Colors.bg_brown, "bg_brown"),
        (Colors.bg_burgundy, "bg_burgundy"),
        (Colors.bg_olive_green, "bg_olive_green"),
        (Colors.bg_muted_olive, "bg_muted_olive"),
        (Colors.bg_beige, "bg_beige"),
        (Colors.bg_grey, "bg_grey"),
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
