import PsServer
import matplotlib.pyplot as plt
import numpy as np



##    plot out the result
##
##def P(x):
##    s = 500 # we choose 10, 100, 500 for s 
##    ps = PsServer.PS_server(7, x, s)
##    ps.status_update()
##    mean_response_time = ps.calculator()
##    return mean_response_time
##x = np.arange(1, 5000, 1)
##ax = plt.subplot(111)
##ax.plot(x, list(map(P, x)), 'r')
##plt.ylim((0.4, 0.6))
##plt.show()
##



# we cut the first 500 points
def Mean(n, s):
    sum_value = 0
    for r in range(500, 3001):
        ps = PsServer.PS_server(n, r, s)
        ps.status_update()
        sum_value += ps.calculator()
    return sum_value/2500

indp_est = [] #independent estimate

s = 100
for _ in range(15):
    s += 100
    indp_est.append(Mean(7, s))

    
x = [1] * len(indp_est)
y = indp_est
plt.plot( x, y, 'o')
plt.show()
