# Problem Set 11
# Name: Cheng, Yu-Hsung
# Collaborators: Wang, Jyh Wei
# Time: 4 hours

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
    df=[]
    for i in x: df.append((4*f(i+h)-3*f(i)-f(i+2*h))/(2*h))
    return df
    
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
    df=[]
    for i in x: df.append((3*f(i)+f(i-2*h)-4*f(i-h)) / (2*h))
    return df

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
    df=[]
    for i in x: df.append((f(i+h)-f(i-h))/(2*h))
    return df

def richardson( f, x, m, h ):
    """Richardson's Extrapolation to approximate  f'(x) at a particular x.

    USAGE:
	d = richardson( f, x, n, h )

    INPUT:
	f	- function to find derivative of
	x	- value of x to find derivative at
	n	- number of levels of extrapolation
	h	- initial stepsize

    OUTPUT:
        numpy float array -  two-dimensional array of extrapolation values.
                             The [n,n] value of this array should be the
                             most accurate estimate of f'(x).
    """
    def richardson1(f,x,n,h):return (f(x+h)-f(x-h))/(2*h) if n==1 else richardson1(f,x,n-1,h/2)+(richardson1(f,x,n-1,h/2)-richardson1(f,x,n-1,h))/(2**(n-1)-1)
    arrayout=np.zeros((m+1,m+1))
    for i in range(m+1):
        for n in range(i+1):
            arrayout[i][n]=richardson1(f,x,n+1,h)
    return arrayout
