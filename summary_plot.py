
import matplotlib.pyplot as plt
import numpy as np





ymin = [0.841, 0.572, 0.517, 0.522, 0.515, 0.521, 0.525, 0.539]
ymax = [0.971, 0.634, 0.553, 0.528, 0.523, 0.525, 0.529, 0.549]
mean = [0.906, 0.603, 0.535, 0.525, 0.519, 0.523, 0.527, 0.544]
x = [3, 4, 5, 6, 7, 8, 9, 10]



plt.ylim((0.5,1.0))

for i in range(8):
    plt.ylim((0.5,0.6))
    plt.vlines(x[i], ymax[i], ymin[i])

plt.plot(x, mean, 'r.')

####plt.axvline(x=.5, ymin=0.522, ymax=0.528)
plt.show()
