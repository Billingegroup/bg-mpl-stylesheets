# BillingeGroup mpl-stylesheets

* `matplotlib` can accept a manually defined stylesheet file that is located remotely or
  locally.

* To use the BillingeGroup stylesheet, please install this package first

  1. It is recommended to install using conda: `conda install -c conda-forge bg-mpl-stylesheets`

  2. Else, you can install from source code in this repo by `python setup.py install`.

* By default the package uses LaTeX fonts for mathematical symbols. This feature requires a Latex package on your computer.  It is not required for the use of the styel-sheet but gives better results for things like angstrom symbols.

  * For Ubuntu users, you can try [this suggestion](https://stackoverflow.com/questions/11354149/python-unable-to-render-tex-in-matplotlib/37218925#37218925):

  ```
  apt-get install dvipng texlive-latex-base texlive-latex-extra texlive-latex-recommended texlive-fonts-recommended cm-super
  ```


* Then simply place the following commands at the
   **begining** of you python session whenever you plot.

  ```
  import matplotlib.pyplot as plt
  from bg_mpl_stylesheet.bg_mpl_stylesheet import bg_mpl_style
  plt.style.use(bg_mpl_style)
  ```


* If you wish to use BillingeGroup stylesheet as the default style of
  your plots, please follow these steps.

  1. Use following commands to figure out which matplotlib config directory
    on your system:

      ```
      import matplotlib
      config_dir = matplotlib.get_configdir()
      ```

  1. Copy and paste `bg_mpl_stylesheet` file to the  `config_dir` found at previous
     step.

    * NOTE: If you installed bg-mpl-stylesheets via conda, or do not have the `bg_mpl_stylesheet` file for any other reason, you can (re)download it [here](https://github.com/Billingegroup/bg-mpl-stylesheets/blob/master/bg_mpl_stylesheet/bg_mpl_stylesheet).


* You could also configure any matplotlib rcParameter dynamically in your python session by

    ```
    plt.rcParams['figure.dpi'] = 180
    plt.rcParams['font.size'] = 18
    (... and so on)
    ```
* Now you can start writing the plot codes as normal, such as

    ```
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4])
    plt.ylabel('some numbers')
    plt.show()
    ```

* You can also go to the `example` folder and run `plot.py` for testing. The example plot would be like this:

![example_plot](example/plot.png?raw=true)

* The full group color cycle is shown in the following along with the color codes:

![color_cycle](example/color_cycle.png?raw=true)

* For full reference, please see matplotlib doc:
  https://matplotlib.org/users/dflt_style_changes.html
