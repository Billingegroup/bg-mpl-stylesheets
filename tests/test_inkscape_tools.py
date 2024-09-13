from pathlib import Path

from bg_mpl_stylesheets.inkscape_tools import get_all_layer_ids


def test_get_all_layer_ids(user_filesystem):
    input_svg = Path(user_filesystem) / "test.svg"
    expected = ["layer1", "layer2"]
    actual = get_all_layer_ids(input_svg)
    assert expected == actual
