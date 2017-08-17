# including density function, cumulative density function
# and inverse cumulative distribution function


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
        return r/t**b

#  cumulative distribution function of g(t)
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

# inverse cumulative distribution function
def ICDF(x):
    a1 = 0.43
    a2 = 0.98
    b = 0.86
    r = (1-b) / (a2**(1-b) - a1**(1-b))
    return (a1**(1-b) + (x*(1-b))/r)**(1/(1-b))
