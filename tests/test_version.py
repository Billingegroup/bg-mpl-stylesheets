"""Unit tests for __version__.py
"""

import bg-mpl-stylesheets


def test_package_version():
    """Ensure the package version is defined and not set to the initial placeholder."""
    assert hasattr(bg-mpl-stylesheets, "__version__")
    assert bg-mpl-stylesheets.__version__ != "0.0.0"
