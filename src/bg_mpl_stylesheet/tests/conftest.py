import pytest


def create_svg_with_layers():
    # Define the SVG content as a string
    svg_content = """<?xml version="1.0" encoding="UTF-8"?>
<svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    <g id="layer1">
        <rect x="10" y="10" width="100" height="100" fill="red"/>
    </g>
    <g id="layer2">
        <circle cx="60" cy="60" r="50" fill="blue"/>
    </g>
</svg>"""
    return svg_content


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = tmp_path
    svg = base_dir / "test.svg"

    with open(svg, "w") as f:
        f.write(create_svg_with_layers())

    yield base_dir
