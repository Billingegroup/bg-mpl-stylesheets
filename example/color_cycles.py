import matplotlib.pyplot as plt
import numpy as np

from bg_mpl_stylesheets.bg_mpl_stylesheet import bg_mpl_style

# please read the README about how to install the group plot style package
# and how to import it and use
plt.style.use(bg_mpl_style)


x = np.arange(0, 1, 0.01)
y = np.sin(3 * x)

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
offset = -0.5  # the offset to plot difference curve

cycle = plt.rcParams["axes.prop_cycle"].by_key()["color"]

# plot the color cycles and corresponding color codes.
for i, c in enumerate(cycle):
    ax.plot(x, y + offset * i, label="\\{}".format(c), color=c, linestyle="-")


ax.set_xlim(0, 2.0)  # set x-axis lower and upper limits

ax.legend(loc="upper right", frameon=False, prop={"size": 14}, ncol=1)


plt.show()
# fig.savefig('color_cycle.png')
