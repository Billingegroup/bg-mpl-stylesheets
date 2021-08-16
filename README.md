# BillingeGroup mpl-stylesheets

* `matplotlib` can accept a manually defined stylesheet file that is located remotely or
  locally.

* To use BillingeGroup stylesheet, please install this package first

  1. You can install from source code in this repo by `python setup.py install`.
  
  2. Or you can conda install the package from conda-forge.

* Then simply run following commands at the
   **begining** of you python session whenever you plot.

  ```
  >>> import matplotlib.pyplot as plt
  >>> from bg_mpl_stylesheet.bg_mpl_stylesheet import bg_mpl_style
  >>> plt.style.use(bg_mpl_style)
  ```


* If you wish to use BillingeGroup stylesheet as the default style of
  your plots, please follow these steps.

  1. Use following commands to figure out which matplotlib config directory
    on your system:

      ```
      >>> import matplotlib
      >>> config_dir = matplotlib.get_configdir()
      ```

  1. Copy and paste `bg_mpl_stylesheet` file to `config_dir` found at previous
     step.


* You could also configure any matplotlib rcParameter dynamically in your python session by

    ```
    plt.rcParams['figure.dpi'] = 180
    plt.rcParams['font.size'] = 18
    (... and so on)
    ```
* Now you can start writing the plot codes as normal, such as

    ```
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x, y)
    fig.savefig('test.pdf')
    ```

* You can also go to the `example` folder and run `plot.py` for the testing. The example plot would be like this:

![example_plot](example/plot.png?raw=true)

* The full group color cycle is shown in the following along with the color codes:

![color_cycle](example/color_cycle.png?raw=true)

* For full reference, please see matplotlib doc:
  https://matplotlib.org/users/dflt_style_changes.html
