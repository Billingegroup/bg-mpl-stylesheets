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

    @classmethod
    def get_color_name_from_hex(cls, hex_value: str) -> str:
        for color in cls:
            if color.value.lower() == hex_value.lower():
                return color.name
        raise ValueError("Unknown color name. Please check Colors enum for available colors.")

    @classmethod
    def get_bg_colors(cls) -> list[str]:
        return [color.value for color in cls if color.name.startswith("BG")]
