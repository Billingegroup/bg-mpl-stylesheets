"""Unit tests for __version__.py
"""

import bg_mpl_stylesheets


def test_package_version():
    """Ensure the package version is defined and not set to the initial placeholder."""
    assert hasattr(bg_mpl_stylesheets, "__version__")
    assert bg_mpl_stylesheets.__version__ != "0.0.0"
