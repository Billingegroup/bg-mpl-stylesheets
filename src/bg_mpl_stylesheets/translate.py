from pathlib import Path

from matplotlib import rc_params_from_file

# this script is for printing the bg_mpl_stylesheets as a python dictionary.


def main():
    style_file = Path(__file__).parent / "bg_mpl_stylesheet"
    bg_mpl_style = rc_params_from_file(
        str(style_file), use_default_template=False
    )
    print(dict(bg_mpl_style))


if __name__ == "__main__":
    main()
