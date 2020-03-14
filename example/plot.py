import matplotlib.pyplot as plt
from diffpy.utils.parsers.loaddata import loadData
#if use stylesheet remotely
path = 'https://raw.githubusercontent.com/Billingegroup/mpl-stylesheets/master/bg_style'
#if use stylesheet locally
# path = '../bg_style'
plt.style.use(path)

#load PDF data
r, gcalc, dr, dg, gdiff = loadData('./CdSe.fgr').T

fig = plt.figure()
ax = fig.add_subplot(1,1,1)
offset = -0.5 # the offset to plot difference curve

ax.plot(r, gcalc+gdiff) # Experimental
ax.plot(r, gcalc) # Calculated
ax.plot(r, gdiff + offset) # Difference
ax.axhline(y = offset, color = 'k', linestyle = '--')

ax.set_xlim(2.0, 20.0) # set x-axis lower and upper limits
ax.set_xlabel('r ($\mathrm{\AA}$)')
ax.set_ylabel('G ($\mathrm{\AA}$$^{-2}$)')

plt.show()
# fig.savefig('plot.png')