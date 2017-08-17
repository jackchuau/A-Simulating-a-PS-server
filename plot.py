import matplotlib.pyplot as plt
import numpy as np

'''
 the probability density function g(t) of the service time t
'''

def g(t):
    a1 = 0.43
    a2 = 0.98
    b = 0.86
    if t< a1:
        return 0
    elif t > a2:
        return 0
    else:
        r = (1-b) / (a2**(1-b) - a1**(1-b))
        return r/(t**b)

def G(t):
    a1 = 0.43
    a2 = 0.98
    b = 0.86
    r = (1-b) / (a2**(1-b) - a1**(1-b))
    if t < a1:
        return 0
    elif t > a2:
        return 1
    else:
        return (r*(t**(1-b) - a1**(1-b)))/(1-b)

plt.xlabel('service time t')
##plt.ylabel('density function g(t)')
plt.ylabel('cumulative density function G(t)')
t = np.arange(0., 1., 0.001)
ax = plt.subplot(111)
##ax.plot(t, list(map(g, t)), 'r.')
ax.plot(t, list(map(G, t)), 'r.')

##plt.ylim((0,3))
plt.ylim((0,1))


ax.spines['right'].set_visible(False)
ax.spines['top'].set_visible(False)
ax.yaxis.set_ticks_position('left')
ax.xaxis.set_ticks_position('bottom')

# when t = a1 = 0.6, g(t) gets its highest value(0.5338034811809763)
max_prob = g(0.6)
print(max_prob)

plt.show()



