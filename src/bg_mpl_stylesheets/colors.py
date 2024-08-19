from enum import Enum


class Colors(str, Enum):
    BG_BLUE = "#0B3C5D"
    BG_RED = "#B82601"
    BG_GREEN = "#1c6b0a"
    BG_LIGHT_BLUE = "#328CC1"
    BG_LIGHT_GREY = "#a8b6c1"
    BG_YELLOW = "#D9B310"
    BG_BROWN = "#6C5050"
    BG_BURGUNDY = "#76323F"
    BG_OLIVE_GREEN = "#626E60"
    BG_MUTED_OLIVE = "#918770"
    BG_BEIGE = "#C09F80"
    BG_GREY = "#b0b0b0ff"
    # Add more colors as needed


def get_bg_colors() -> list[str]:
    bg_colors = [
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
    return bg_colors
