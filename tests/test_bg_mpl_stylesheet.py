import pytest
from matplotlib import cycler

from bg_mpl_stylesheets import styles


def test_update_style_with_latex():
    actual = styles.update_style_with_latex(styles.all_styles["bg-style"])
    expected = expected_style
    assert expected == actual


def test_use_style_default(monkeypatch):
    # UC1: use_style is called with no arguments.
    # Expected: the default "bg-style" style is passed to Matplotlib.
    actual = []
    monkeypatch.setattr(styles.mpl_style, "use", actual.append)
    styles.use_style()
    expected = [styles.all_styles["bg-style"]]
    assert actual == expected


def test_use_style_valid_style(monkeypatch):
    # UC2: use_style is called with a recognized style name.
    # Expected: the requested style is passed to Matplotlib.
    style_name = "bg-style"
    actual = []
    monkeypatch.setattr(styles.mpl_style, "use", actual.append)
    styles.use_style(style_name)
    expected = [styles.all_styles[style_name]]
    assert actual == expected


@pytest.mark.parametrize("invalid_style", ["not-a-style", None])
def test_use_style_invalid_style(invalid_style):
    # UC3: use_style is called with an unknown name or invalid value.
    # Expected: ValueError explains the problem and lists valid styles.
    expected = (
        f"{invalid_style} is not a recognized style. "
        f"Please select from {list(styles.all_styles)}."
    )
    with pytest.raises(ValueError) as exc_info:
        styles.use_style(invalid_style)
    actual = str(exc_info.value)
    assert actual == expected


expected_style = {
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
