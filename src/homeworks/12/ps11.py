#!/usr/bin/python2
#Problem 11
#Name: Lucas Peng B97901120
#Collaborators: Hank Lee B97202037
#Time: 1:00

import numpy as np
def forward_difference_h2(f,x,h):
    """ Given a function f, return the derivative df at points x
        using the O(h**2) forward difference formula
    USAGE:
        df = forward_difference_h2(f,x,h)
    INPUT:
        f       - function to find derivative of
        x       - list of values x to find derivative at
        h       - step size
    OUTPUT:
        df      - list of f' at values x
    """
    x = np.array(x)
    return list((-3*f(x)+4*f(x+h)-f(x+2*h))/(2*h))
    
def backward_difference_h2(f,x,h):
    """ Given a function f, find the derivative df at x
        using the O(h**2) backward difference formula
    USAGE:
        df = backward_difference_h2(f,x,h)
    INPUT:
        f       - function to find derivative of
        x       - list of values x to find derivative at
        h       - step size
    OUTPUT:
        df      - list of f' at values x
    """
    x=np.array(x)
    return list((3*f(x)-4*f(x-h)+f(x-2*h))/(2*h))

def central_difference_h2(f,x,h):
    """ Given a function f, find the derivative df at x
        using the O(h**2) central difference formula
    USAGE:
        df = central_difference_h2(f,x,h)
    INPUT:
        f       - function to find derivative of
        x       - list of values x to find derivative at
        h       - step size
    OUTPUT:
        df      - list of f' at values x
    """
    x=np.array(x)
    return list((-f(x-h)+f(x+h))/(2*h))

def richardson( f, x, n, h ):
    """Richardson's Extrapolation to approximate  f'(x) at a particular x.

    USAGE:
        d = richardson( f, x, n, h )

    INPUT:
        f       - function to find derivative of
        x       - value of x to find derivative at
        n       - number of levels of extrapolation
        h       - initial stepsize

    OUTPUT:
        numpy float array -  two-dimensional array of extrapolation values.
                             The [n,n] value of this array should be the
                             most accurate estimate of f'(x).
    """
    m = np.zeros([n,n])
    for i in range(n):m[i][0] = (f(x+(h/2**i))-f(x))/(h/2**i)

    for i in range(1,n):
        for j in range(i,n):            
            m[j][i]=m[j][i-1]+(m[j][i-1]-m[j-1][i-1])/(2**i-1)
    return m

if __name__ == "__main__":
    f = np.cos
    x=np.arange(10)
    print forward_difference_h2(f,x,0.001)
    print backward_difference_h2(f,x,0.001)
    print central_difference_h2(f,x,0.001)
    print richardson(f,9,4,0.001)
    print -1*np.sin(x)
