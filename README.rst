|Icon| |title|_
===============

.. |title| replace:: bg-mpl-stylesheets
.. _title: https://Billingegroup.github.io/bg-mpl-stylesheets

.. |Icon| image:: https://avatars.githubusercontent.com/Billingegroup
        :target: https://Billingegroup.github.io/bg-mpl-stylesheets
        :height: 100px

|PyPi| |Forge| |PythonVersion| |PR|

|CI| |Codecov| |Black| |Tracking|

.. |Black| image:: https://img.shields.io/badge/code_style-black-black
        :target: https://github.com/psf/black

.. |CI| image:: https://github.com/Billingegroup/bg-mpl-stylesheets/actions/workflows/main.yml/badge.svg
        :target: https://github.com/Billingegroup/bg-mpl-stylesheets/actions/workflows/main.yml

.. |Codecov| image:: https://codecov.io/gh/Billingegroup/bg-mpl-stylesheets/branch/main/graph/badge.svg
        :target: https://codecov.io/gh/Billingegroup/bg-mpl-stylesheets

.. |Forge| image:: https://img.shields.io/conda/vn/conda-forge/bg-mpl-stylesheets
        :target: https://anaconda.org/conda-forge/bg-mpl-stylesheets

.. |PR| image:: https://img.shields.io/badge/PR-Welcome-29ab47ff

.. |PyPi| image:: https://img.shields.io/pypi/v/bg-mpl-stylesheets
        :target: https://pypi.org/project/bg-mpl-stylesheets/

.. |PythonVersion| image:: https://img.shields.io/pypi/pyversions/bg-mpl-stylesheets
        :target: https://pypi.org/project/bg-mpl-stylesheets/

.. |Tracking| image:: https://img.shields.io/badge/issue_tracking-github-blue
        :target: https://github.com/Billingegroup/bg-mpl-stylesheets/issues

A package for using Billinge group style files

* LONGER DESCRIPTION HERE

For more information about the bg-mpl-stylesheets library, please consult our `online documentation <https://Billingegroup.github.io/bg-mpl-stylesheets>`_.

Citation
--------

If you use bg-mpl-stylesheets in a scientific publication, we would like you to cite this package as

        bg-mpl-stylesheets Package, https://github.com/Billingegroup/bg-mpl-stylesheets

Installation
------------

The preferred method is to use `Miniconda Python
<https://docs.conda.io/projects/miniconda/en/latest/miniconda-install.html>`_
and install from the "conda-forge" channel of Conda packages.

To add "conda-forge" to the conda channels, run the following in a terminal. ::

        conda config --add channels conda-forge

We want to install our packages in a suitable conda environment.
The following creates and activates a new environment named ``bg-mpl-stylesheets_env`` ::

        conda create -n bg-mpl-stylesheets_env python=3
        conda activate bg-mpl-stylesheets_env

Then, to fully install ``bg-mpl-stylesheets`` in our active environment, run ::

        conda install bg-mpl-stylesheets

Another option is to use ``pip`` to download and install the latest release from
`Python Package Index <https://pypi.python.org>`_.
To install using ``pip`` into your ``bg-mpl-stylesheets_env`` environment, we will also have to install dependencies ::

        pip install -r https://raw.githubusercontent.com/Billingegroup/bg-mpl-stylesheets/main/requirements/run.txt

and then install the package ::

        pip install bg-mpl-stylesheets

If you prefer to install from sources, after installing the dependencies, obtain the source archive from
`GitHub <https://github.com/Billingegroup/bg-mpl-stylesheets/>`_. Once installed, ``cd`` into your ``bg-mpl-stylesheets`` directory
and run the following ::

        pip install .

Support and Contribute
----------------------

`Diffpy user group <https://groups.google.com/g/diffpy-users>`_ is the discussion forum for general questions and discussions about the use of bg-mpl-stylesheets. Please join the bg-mpl-stylesheets users community by joining the Google group. The bg-mpl-stylesheets project welcomes your expertise and enthusiasm!

If you see a bug or want to request a feature, please `report it as an issue <https://github.com/Billingegroup/bg-mpl-stylesheets/issues>`_ and/or `submit a fix as a PR <https://github.com/Billingegroup/bg-mpl-stylesheets/pulls>`_. You can also post it to the `Diffpy user group <https://groups.google.com/g/diffpy-users>`_. 

Feel free to fork the project and contribute. To install bg-mpl-stylesheets
in a development mode, with its sources being directly used by Python
rather than copied to a package directory, use the following in the root
directory ::

        pip install -e .

To ensure code quality and to prevent accidental commits into the default branch, please set up the use of our pre-commit
hooks.

1. Install pre-commit in your working environment by running ``conda install pre-commit``.

2. Initialize pre-commit (one time only) ``pre-commit install``.

Thereafter your code will be linted by black and isort and checked against flake8 before you can commit.
If it fails by black or isort, just rerun and it should pass (black and isort will modify the files so should
pass after they are modified). If the flake8 test fails please see the error messages and fix them manually before
trying to commit again.

Improvements and fixes are always appreciated.

Before contribuing, please read our `Code of Conduct <https://github.com/Billingegroup/bg-mpl-stylesheets/blob/main/CODE_OF_CONDUCT.rst>`_.

Contact
-------

For more information on bg-mpl-stylesheets please visit the project `web-page <https://Billingegroup.github.io/>`_ or email Prof. Simon Billinge at sb2896@columbia.edu.
