"""Command-line entry point for bg-mpl-stylesheets."""

import argparse

from bg_mpl_stylesheets.version import __version__  # noqa


def main():
    """Run the bg-mpl-stylesheets command-line interface.

    Supports ``--version`` to print the installed package version. With
    no arguments, prints the help message.
    """
    parser = argparse.ArgumentParser(
        prog="bg-mpl-stylesheets",
        description=(
            "A package for using Billinge group Matplotlib style files.\n\n"
            "For more information, visit: "
            "https://github.com/Billingegroup/bg-mpl-stylesheets/"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )

    parser.add_argument(
        "--version",
        action="store_true",
        help="Show the program's version number and exit",
    )

    args = parser.parse_args()

    if args.version:
        print(f"bg-mpl-stylesheets {__version__}")
    else:
        # Default behavior when no arguments are given
        parser.print_help()


if __name__ == "__main__":
    main()
