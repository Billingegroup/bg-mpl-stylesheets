# BillingeGroup mpl-stylesheets

* `matplotlib` can accept stylesheet file that is located remotely or
  locally.

* To use BillingeGroup stylesheet remotely, simply run following commands at the
   **begining** of you python session.

  ```
  >>> import matplotlib.pyplot as plt
  >>> path = 'https://raw.githubusercontent.com/Billingegroup/mpl-stylesheets/master/bg_style'
  >>> plt.style.use(path)
  ```

* If you prefer to use BillingeGroup stylesheet locally, please follow these steps.

  1. Fork and clone the repo to your local computer

  1. replace the variable `path` into the stylesheet file on your local system and run the commands as above.

* If you wish to use BillingeGroup stylesheet as the default style of
  your plots, please follow these steps.

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
    plt.rcParams['figure.dpi'] = 180
    plt.rcParams['font.size'] = 18
    (... and so on)
    ```
* Now you can start writing the plot codes as normal, for example

    ```
    fig = plt.figure()
    ax = fig.add_subplot(1,1,1)
    ax.plot(x, y)
    fig.savefig('test.pdf')
    ```

* For full reference, please see matplotlib doc:
  https://matplotlib.org/users/dflt_style_changes.html
