from distutils.spawn import find_executable

from matplotlib import cycler

bg_style = {
    ####################
    # lines properties #
    ####################
    "lines.linewidth": 2.50,
    "lines.markeredgewidth": 0.25,
    "lines.markersize": 6.00,
    "lines.solid_capstyle": "round",
    ###################
    # font properties #
    ###################
    "font.size": 15.0,
    "font.family": ["sans-serif"],
    "font.sans-serif": [
        "DejaVu Sans",
        "Bitstream Vera Sans",
        "Computer Modern Sans Serif",
        "Lucida Grande",
        "Verdana",
        "Geneva",
        "Lucid",
        "Arial",
        "Helvetica",
        "Avant Garde",
        "sans-serif",
        "cm",
    ],
    ###################
    # axes properties #
    ###################
    "axes.titlesize": 14.0,
    "axes.labelsize": 16.0,
    "axes.labelcolor": "k",
    "axes.linewidth": 2.5,
    "axes.edgecolor": "k",
    "axes.prop_cycle": cycler(
        "color",
        [
            "#0B3C5D",
            "#B82601",
            "#1C6B0A",
            "#328CC1",
            "#A8B6C1",
            "#D9B310",
            "#6C5050",
            "#76323F",
            "#626E60",
            "#918770",
            "#C09F80",
            "#B0B0B0FF",
        ],
    ),
    ####################
    # xtick properties #
    ####################
    "xtick.top": True,
    "xtick.direction": "in",
    "xtick.color": "k",
    "xtick.labelsize": 15.0,
    "xtick.minor.width": 0.5,
    "xtick.major.width": 1.7,
    "xtick.major.pad": 5.0,
    ####################
    # ytick properties #
    ####################
    "ytick.right": True,
    "ytick.direction": "in",
    "ytick.color": "k",
    "ytick.labelsize": 15.0,
    "ytick.minor.width": 0.5,
    "ytick.major.width": 1.7,
    "ytick.major.pad": 5.0,
    ###################
    # grid properties #
    ###################
    "grid.color": "#b2b2b2",
    "grid.linestyle": "--",
    "grid.linewidth": 1.0,
    #####################
    # figure properties #
    #####################
    "figure.facecolor": "w",
    "savefig.bbox": "tight",
}


def update_style_with_latex(style):
    if find_executable("latex"):
        tex = {
            ###################
            # text properties #
            ###################
            "text.usetex": True,
            "text.latex.preamble": r"\usepackage[cm]{sfmath}",
            "mathtext.fontset": "stixsans",
        }
        style.update(tex)
    return style


all_styles = {"bg-style": bg_style}

for key, style in all_styles.items():
    all_styles.update({key: update_style_with_latex(style)})
