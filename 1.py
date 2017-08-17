
import matplotlib.pyplot as plt
import numpy as np



ymax = [5.268,5.223,5.187,6.252,7.13,5.17,6.635,6.546,11.329,13.658,14.451,15.286,16.814,22.92]
ymin = [0.251,0.351,0.075,0.126,0.151,1.031,0.201,0.226,0.226,0.302,3.699,5.384,0.201,0.151]
x = [10, 20, 25, 40, 50, 75, 80, 100, 200, 400, 600, 800, 1000, 1200]



##plt.ylim((0,1.0))

for i in range(len(ymin)):
    plt.vlines(x[i], ymax[i], ymin[i])
    
plt.xlabel('number of users')
plt.ylabel('tomcat container usage')
##plt.plot(x, mean, 'r.')

####plt.axvline(x=.5, ymin=0.522, ymax=0.528)
plt.show()
