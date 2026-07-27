import math

import matplotlib as mpl
import pytest
from matplotlib import cycler

from bg_mpl_stylesheets.styles import (
    all_styles,
    update_style_with_latex,
    use_style,
)


def values_are_close(expected_value, actual_value, rel_tol=1e-5, abs_tol=1e-8):
    """Recursively compare two values."""
    if isinstance(expected_value, bool) or isinstance(actual_value, bool):
        return expected_value is actual_value
    if isinstance(expected_value, (int, float)) and isinstance(
        actual_value, (int, float)
    ):
        return math.isclose(
            expected_value,
            actual_value,
            rel_tol=rel_tol,
            abs_tol=abs_tol,
        )
    if isinstance(expected_value, (list, tuple)) and isinstance(
        actual_value, (list, tuple)
    ):
        if len(expected_value) != len(actual_value):
            return False
        return all(
            values_are_close(expected_item, actual_item, rel_tol, abs_tol)
            for expected_item, actual_item in zip(expected_value, actual_value)
        )
    return expected_value == actual_value


def rc_params_match(expected, actual, rel_tol=1e-5, abs_tol=1e-8):
    """Return whether all expected rcParams match the actual values."""
    for key, expected_value in expected.items():
        if key not in actual:
            return False
        actual_value = actual[key]
        if not values_are_close(
            expected_value, actual_value, rel_tol, abs_tol
        ):
            return False
    return True


def test_update_style_with_latex():
    actual = update_style_with_latex(all_styles["bg-style"])
    expected = expected_style
    assert expected == actual


@pytest.mark.parametrize(
    "style_args",
    [
        # Case 1: No input (default) is passed to use_style().
        # Expected: "bg-style" is used.
        [None, "bg-style"],
        # Case 2: "bg-style" is passed to use_style().
        # Expected: "bg-style" is used.
        ["bg-style", "bg-style"],
    ],
)
def test_use_style(style_args):
    with mpl.rc_context():
        if style_args[0] is None:
            use_style()
        else:
            use_style(style_args[0])
        actual = mpl.rcParams.copy()
    expected = all_styles[style_args[1]]
    assert rc_params_match(expected, actual)


@pytest.mark.parametrize(
    "style_args",
    [
        # Case 1: An unknown style name is passed to use_style().
        # Expected: ValueError explains the input is unrecognized
        # and lists the valid styles.
        [
            "not-a-style",
            (
                "not-a-style is not a recognized style. "
                f"Please select from {list(all_styles)}."
            ),
        ],
    ],
)
def test_use_style_bad(style_args):
    with pytest.raises(ValueError) as exc_info:
        use_style(style_args[0])
    actual = str(exc_info.value)
    expected = style_args[1]
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
