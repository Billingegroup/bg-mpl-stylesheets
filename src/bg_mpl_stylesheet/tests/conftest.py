from pathlib import Path

import pytest
from lxml import etree


def create_svg_with_layers():
    # Create the root <svg> element
    svg = etree.Element("svg", xmlns="http://www.w3.org/2000/svg", version="1.1")

    # Define the layers
    layers = [
        {
            "id": "layer1",
            "elements": [
                {
                    "tag": "rect",
                    "attributes": {"x": "10", "y": "10", "width": "100", "height": "100", "fill": "red"},
                }
            ],
        },
        {
            "id": "layer2",
            "elements": [{"tag": "circle", "attributes": {"cx": "60", "cy": "60", "r": "50", "fill": "blue"}}],
        },
    ]

    # Create layers and add elements to them
    for layer in layers:
        g = etree.SubElement(svg, "g", id=layer["id"])
        for element in layer["elements"]:
            etree.SubElement(g, element["tag"], **element["attributes"])

    # Convert the XML tree to a string
    svg_data = etree.tostring(svg, pretty_print=True, xml_declaration=True, encoding="UTF-8")

    return svg_data


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = Path(tmp_path)
    svg = base_dir / "test.svg"

    with open(svg, "w") as f:
        f.write(create_svg_with_layers())

    yield tmp_path
