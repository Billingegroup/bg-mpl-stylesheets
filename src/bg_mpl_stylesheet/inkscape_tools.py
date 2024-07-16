import subprocess


def export_layers_to_pdf(svg_file, output_pdf, layers_to_include):
    """
    Export a subset of layers from an svg file to a PDF output

    Parameters
    ----------
    svg_file string
      The path to the svg
    output_pdf string
      The path to the output pdf file
    layers_to_include list of strings
      The layers_to_include

    Returns
    -------
    None

    """

    # Define the command to run Inkscape
    command = [
        "inkscape",
        svg_file,
        "--export-type=pdf",
        f"--export-filename={output_pdf}",
    ]

    # Add commands to hide all layers initially
    layers_hide = [f"--select-by-id={layer_id} --verb=LayerHide" for layer_id in get_all_layer_ids(svg_file)]
    command.extend(layers_hide)

    # Add commands to show specific layers
    layers_show = [f"--select-by-id={layer_id} --verb=LayerShow" for layer_id in layers_to_include]
    command.extend(layers_show)

    # Add command to export
    command.append("--verb=FileSave")
    command.append("--verb=FileClose")

    # Execute the command
    subprocess.run(command, check=True)


def get_all_layer_ids(svg_file):
    """
    The layer IDs are the names of the layers, but this python script will return them all

    Parameters
    ----------
    svg_file string
      The path to the svg

    Returns
    -------
    The layer IDs as a list of strings

    """
    from xml.etree import ElementTree as ET

    tree = ET.parse(svg_file)
    root = tree.getroot()

    # Inkscape-specific namespace for layer elements
    namespace = {"svg": "http://www.w3.org/2000/svg"}

    layer_ids = []
    for layer in root.findall(".//svg:g", namespace):
        print(layer.attrib)
        if "{http://www.inkscape.org/namespaces/inkscape}label" in layer.attrib:
            layer_ids.append(layer.attrib["id"])

    return layer_ids


# Example usage
# svg_file = "example.svg"
# output_pdf = "output.pdf"
# layers_to_include = ["layer1", "layer2"]  # Replace with your layer IDs

# export_layers_to_pdf(svg_file, output_pdf, layers_to_include)
