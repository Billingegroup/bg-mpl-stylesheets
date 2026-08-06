=============
Release notes
=============

.. current developments

0.6.1
=====

**Fixed:**

* Fixed incorrect script entry point in `pyproject.toml` that caused `bg-mpl-stylesheets -h`
and `bg-mpl-stylesheets --version` to print the raw launcher script instead of running.


0.6.0
=====

**Added:**

* Added support for Python 3.14
* Added ``use_style()`` as a convenience helper for applying Billinge group Matplotlib styles.

**Changed:**

*  <news item>

**Deprecated:**

*  <news item>

**Fixed:**

* Fixed `plot.py` example script to resolve the data file path relative to
the script location instead of the current working directory, so it
works regardless of where it's run from.
* Fixed latex preamble syntax error due to matplotlib update.
*  Updated project to the latest scikit-package template
* Added missing API doc entries for bg_mpl_stylesheets_app and version submodules.

**Removed:**

* Removed support for Python 3.11


0.5.1
=====

**Added:**

* Spelling check via Codespell in pre-commit
* Coverage report in each PR


0.5.0
=====

**Added:**

* Support for python 3.13

**Removed:**

* Support for python 3.10
* distutils module, as deprecated in Python 3.13


0.4.2
=====

**Fixed:**

* Another recut to include issue templates
* tests folder at the root of the repo
* re-cookiecut repo to group's package standard
* dependency installation in pyproject.toml for pip install
* add matplotlib to pip.txt, maintain matplotlib-base in conda.txt


0.3.2
=====

**Changed:**

* key name in the style dictionary from all_styles["bg_style"] to all_styles["bg-style"]

**Fixed:**

* URLs referring to the organization in README.md

0.3.1
=====

**Added:**

* inskape_tools.py module with python helper functions for scripting inkscape tasks
* function in inkscape_tools.py to export a list of layers from an svg file.  Can help with beamer animations.

**Fixed:**

* package structure to new group template


v0.1.0
=======

**Added:**

* CHANGELOG
* Rever tags for conda-forge release
* Config files for conda-forge release

**Changed:**

* Changelog filename

**Deprecated:** None

**Removed:** None

**Fixed:**

* Rever integration
* Rever version bump patterns

0.4.0
=====

**Added:**

* `Colors` enum for choosing  a bg color by name

**Removed:**

* duplicate pre-commit GitHub workflow

**Fixed:**

* Capitalized the hex color codes

0.4.0
=====

0.4.1
=====

**Added:**

* Columbia blue (#B9D9EB) as columbia_blue in Colors
