import pytest


def create_svg_with_layers():
    # Define the SVG content as a string
    svg_content = """<?xml version="1.0" encoding="UTF-8" standalone="no"?>
<!-- Created with Inkscape (http://www.inkscape.org/) -->

<svg
   width="200.40558mm"
   height="100.04597mm"
   viewBox="0 0 200.40558 100.04597"
   version="1.1"
   id="svg1"
   inkscape:version="1.3.2 (091e20e, 2023-11-25, custom)"
   sodipodi:docname="minimal2layer.svg"
   xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
   xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
   xmlns="http://www.w3.org/2000/svg"
   xmlns:svg="http://www.w3.org/2000/svg"
   xmlns:rdf="http://www.w3.org/1999/02/22-rdf-syntax-ns#"
   xmlns:cc="http://creativecommons.org/ns#">
  <sodipodi:namedview
     id="namedview1"
     pagecolor="#ffffff"
     bordercolor="#000000"
     borderopacity="0.25"
     inkscape:showpageshadow="2"
     inkscape:pageopacity="0.0"
     inkscape:pagecheckerboard="0"
     inkscape:deskcolor="#d1d1d1"
     inkscape:document-units="mm"
     inkscape:zoom="1.26875"
     inkscape:cx="843.34975"
     inkscape:cy="261.67488"
     inkscape:window-width="1920"
     inkscape:window-height="1094"
     inkscape:window-x="-11"
     inkscape:window-y="-11"
     inkscape:window-maximized="1"
     inkscape:current-layer="layer2" />
  <defs
     id="defs1" />
  <g
     inkscape:label="Layer 1"
     inkscape:groupmode="layer"
     id="layer1">
    <rect
       style="fill:#000000;stroke-width:0.264583"
       id="rect1"
       width="9.1756973"
       height="5.2134647"
       x="107.81445"
       y="20.228243" />
  </g>
  <g
     inkscape:groupmode="layer"
     id="layer2"
     inkscape:label="Layer 2">
    <rect
       style="fill:#000000;stroke-width:0.264583"
       id="rect2"
       width="8.3415432"
       height="5.0049262"
       x="117.19868"
       y="35.660095" />
  </g>
  <metadata
     id="metadata1">
    <rdf:RDF>
      <cc:License
         rdf:about="http://creativecommons.org/licenses/by-sa/4.0/">
        <cc:permits
           rdf:resource="http://creativecommons.org/ns#Reproduction" />
        <cc:permits
           rdf:resource="http://creativecommons.org/ns#Distribution" />
        <cc:requires
           rdf:resource="http://creativecommons.org/ns#Notice" />
        <cc:requires
           rdf:resource="http://creativecommons.org/ns#Attribution" />
        <cc:permits
           rdf:resource="http://creativecommons.org/ns#DerivativeWorks" />
        <cc:requires
           rdf:resource="http://creativecommons.org/ns#ShareAlike" />
      </cc:License>
      <cc:Work
         rdf:about="">
        <cc:license
           rdf:resource="http://creativecommons.org/licenses/by-sa/4.0/" />
      </cc:Work>
    </rdf:RDF>
  </metadata>
</svg>
"""
    return svg_content


@pytest.fixture
def user_filesystem(tmp_path):
    base_dir = tmp_path
    svg = base_dir / "test.svg"

    with open(svg, "w") as f:
        f.write(create_svg_with_layers())

    yield base_dir
