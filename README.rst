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
# BillingeGroup mpl-stylesheets

## Installation and usage
* `matplotlib` can accept a manually defined stylesheet file that is located remotely or
  locally.

* To use the BillingeGroup stylesheet, please install this package first

  1. It is recommended to install using conda: `conda install -c conda-forge bg-mpl-stylesheets`

  2. To get cutting edge updates you can install in develop mode from the source code in this repo by typing `python setup.py develop`.

* By default the package uses LaTeX fonts for mathematical symbols. This feature requires a Latex package on your computer.  It is not required for the use of the styel-sheet but gives better results for things like angstrom symbols.  Matplotlib will look for your installed latex package, for example TeXLive or MikTex.  If it can't find a latex package it will look for non-latex font replacements.

* To use the stylesheet, near the beginning your python script type the.

  ```[python]
  from bg_mpl_stylesheet.bg_mpl_stylesheet import <style-sheet-name>
  plt.style.use(<style-sheet-name>)
  ```
  
  for example
  
  ```
  from bg_mpl_stylesheet.bg_mpl_stylesheet import bg_mpl_style
  plt.style.use(bg_mpl_style)
  ```

* If you wish to use BillingeGroup stylesheet as the default style for all
  your plots, please follow these steps.

  1. Use following commands to figure out which matplotlib config directory
    on your system:

      ```
      import matplotlib
      config_dir = matplotlib.get_configdir()
      ```

  1. Copy and paste the `bg_mpl_stylesheet` file to the  `config_dir` found in the previous
     step.

## Overriding the default styles
* You can configure any matplotlib style parameter by updating its value in the `rcParams` dictionary dynamically in your python session, For example,  by typing

    ```
    plt.rcParams['figure.dpi'] = 180
    plt.rcParams['font.size'] = 18
    (... and so on)
    ```
    
    Not that the `rcParams` are global.  It can get very confusing if these are updated everywhere in the code.  It is much better to make local updates to their values by defining functions for your plots and using the @matplotlib.style.context() decorator, e.g., 
    
    ```
    import matplotlib.pyplot as plt

    @mpl.rc_context({'lines.linewidth': 1, 'axes.linewidth': 0.7, 'xtick.major.size': 0.7,
                 'xtick.major.width': 0.7,  'xtick.labelsize': 5, 'legend.frameon': False,
                 'legend.loc': 'best', 'font.size': 5, 'axes.labelsize': 5,
                 'ytick.left': False, 'ytick.labelleft': False, 'ytick.right': False
                 })
    def all_plot(x-array, yarray):
        plt.plot(x-array, y-array)
        plt.ylabel('some numbers')
        plt.show()
        return
    ```
    This will confine the style updates to just apply in the function namespace.  
    
* You can also update style parameters locally by using the matplotlib style context manager, for example

    ```
    with plot.style.context(<new_stylesheet>):
        plt.plot(x-array, y-array)
        plt.ylabel('some numbers')
    plt.show()
    ```
### Here are a snapshot of values in bg-mpl-style sheet which you may override with rc.parms to fine tune things:

    'lines.linewidth':       2.50,
    'lines.markeredgewidth': 0.25,
    'lines.markersize':      6.00,
    'lines.solid_capstyle': 'round',
    'font.size': 15.0,
    'font.family': ['sans-serif'],
    ###################
    # axes properties #
    ###################
    'axes.titlesize': 14.0,
    'axes.labelsize': 16.0,
    'axes.labelcolor': 'k',
    'axes.linewidth':  2.5,
    'axes.edgecolor':  'k',
    'axes.prop_cycle': cycler('color',
                              ['#0B3C5D', '#B82601', '#1c6b0a', '#328CC1',
                               '#a8b6c1', '#D9B310', '#984B43', '#76323F',
                               '#626E60', '#AB987A', '#C09F80', '#b0b0b0ff']),
    ####################
    # xtick properties #
    ####################
    'xtick.top': True,
    'xtick.direction': 'in',
    'xtick.color': 'k',
    'xtick.labelsize':   15.0,
    'xtick.minor.width':  0.5,
    'xtick.major.width':  1.7,
    'xtick.major.pad':    5.0,
    ####################
    # ytick properties #
    ####################
    'ytick.right': True,
    'ytick.direction': 'in',
    'ytick.color': 'k',
    'ytick.labelsize':   15.0,
    'ytick.minor.width':  0.5,
    'ytick.major.width':  1.7,
    'ytick.major.pad':    5.0,
    ###################
    # grid properties #
    ###################
    'grid.color': '#b2b2b2',
    'grid.linestyle': '--',
    'grid.linewidth': 1.0,
    #####################
    # figure properties #
    #####################
    'figure.facecolor': 'w',
    'savefig.bbox': 'tight'

# Example code

* You can also go to the `example` folder and run `plot.py` for testing. The example plot would be like this:

![example_plot](example/plot.png?raw=true)

## Colors

* The full group color cycle is shown in the following along with the color codes:

![color_cycle](example/color_cycle.png?raw=true)

* For full reference, please see matplotlib doc:
  https://matplotlib.org/users/dflt_style_changes.html

## Contributing
    
    Please feel encouraged to contribute your own style-sheets to the package and make your beautiful styles more widely available.  To do so, fork the repo, create a branch and make a Pull Request.
