# BillingeGroup mpl-stylesheets

* `matplotlib` can accept stylesheet file that is located remotely or
  locally.

* To use BillingeGroup stylesheet, simply type following commands at the
   *begining* of you python session

  ```
  >>> import matplotlib as mpl
  >>> path = 'https://raw.githubusercontent.com/Billingegroup/mpl-stylesheets/master/bg_style'
  >>> mpl.style.use(path)
  ```

  The variable `path` can also be the filepath to the stylesheet file on your local system.

* If you wish to use BillingeGroup stylesheet as the default style of
  your plots, please follow these steps.

  1. Clone the repo to your local computer

  1. Use following commands to figure out which matplotlib config directory
    on your system:

      ```
      >>> import matplotlib
      >>> config_dir = matplotlib.get_configdir()

      ```

  1. Copy and paste `bg_style` file to `config_dir` found at previous
     step.


* You could also configure any matplotlib rcParameter dynamically in your python session by

    ```
    matplotlib.rcParams['figure.dpi'] = 180
    matplotlib.rcParams['font.size'] = 18
    (... and so on)
    ```

* For full reference, please see matplotlib doc:
  https://matplotlib.org/users/dflt_style_changes.html
