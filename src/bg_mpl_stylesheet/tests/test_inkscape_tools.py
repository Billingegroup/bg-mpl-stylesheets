from pathlib import Path

from bg_mpl_stylesheet import inkscape_tools


def test_get_all_layer_ids(tmp_path):
    input_svg = Path(tmp_path) / "test.svg"
    expected = ["layer1", "layer2"]
    actual = inkscape_tools.get_all_layer_ids(input_svg)
    assert expected == actual
