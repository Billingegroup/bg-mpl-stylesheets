def get_colors():
    return {
        "bg_blue": "#0B3C5D",
        "bg_red": "#B82601",
        "bg_green": "#1c6b0a",
        "bg_light_blue": "#328CC1",
        "bg_light_grey": "#a8b6c1",
        "bg_yellow": "#D9B310",
        "bg_brown": "#6C5050",
        "bg_burgundy": "#76323F",
        "bg_olive_green": "#626E60",
        "bg_muted_olive": "#918770",
        "bg_beige": "#C09F80",
        "bg_grey": "#b0b0b0ff",
    }
    
def get_bg_colors() -> list[str]:
    colors = get_colors()
    bg_colors = [
        colors["bg_blue"],
        colors["bg_red"],
        colors["bg_green"],
        colors["bg_light_blue"],
        colors["bg_light_grey"],
        colors["bg_yellow"],
        colors["bg_brown"],
        colors["bg_burgundy"],
        colors["bg_olive_green"],
        colors["bg_muted_olive"],
        colors["bg_beige"],
        colors["bg_grey"],
    ]
    return bg_colors


