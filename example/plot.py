import matplotlib.pyplot as plt
from diffpy.utils.parsers.loaddata import loadData

from bg_mpl_stylesheets.styles import all_styles

# please read the README about how to install the group plot style package
# and how to import it and use
plt.style.use(all_styles["bg-style"])

# load PDF data
r, gcalc, dr, dg, gdiff = loadData("example/CdSe_data.fgr").T

fig = plt.figure()
ax = fig.add_subplot(1, 1, 1)
offset = -0.5  # the offset to plot difference curve

ax.plot(r, gcalc + gdiff)  # Experimental
ax.plot(r, gcalc)  # Calculated
ax.plot(r, gdiff + offset)  # Difference
ax.axhline(y=offset, color="k", linestyle="--")

ax.set_xlim(2.0, 20.0)  # set x-axis lower and upper limits
ax.set_xlabel("r (Å)")
ax.set_ylabel("G (Å$^{-2}$)")

plt.tight_layout()
plt.show()
# fig.savefig('plot.pdf')
