from enum import Enum


class Colors(str, Enum):
    bg_blue = "#0B3C5D"
    bg_red = "#B82601"
    bg_green = "#1C6B0A"
    bg_light_blue = "#328CC1"
    bg_light_grey = "#A8B6C1"
    bg_yellow = "#D9B310"
    bg_brown = "#6C5050"
    bg_burgundy = "#76323F"
    bg_olive_green = "#626E60"
    bg_muted_olive = "#918770"
    bg_beige = "#C09F80"
    bg_grey = "#B0B0B0FF"
    # Add more colors as needed

    @classmethod
    def get_bg_colors(cls) -> list[str]:
        return [color.value for color in cls if color.name.startswith("bg")]
