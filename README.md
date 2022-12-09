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
    
# Example code

* You can also go to the `example` folder and run `plot.py` for testing. The example plot would be like this:

![example_plot](example/plot.png?raw=true)

## Colors

* The full group color cycle is shown in the following along with the color codes:

![color_cycle](example/color_cycle.png?raw=true)

* For full reference, please see matplotlib doc:
  https://matplotlib.org/users/dflt_style_changes.html
