#-*-coding:utf-8-*-
#Problem 11
#Name:Wu Po-Kuan
#Collaborators:
#Time:0:40




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
    df=[(-f(xi+2*h)+4*f(xi+h)-3*f(xi))/2/h for xi in x]
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
    df=[(f(xi-2*h)-4*f(xi-h)+3*f(xi))/2/h for xi in x]
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
    df=[(f(xi+h)-f(xi-h))/2/h for xi in x]
    return df

def richardson( f, x, n, h ):
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
                             most accurate estimate of f'(x)."""
    N=np.zeros((n,n))
    for i in range(n):
        N[i,0]=(f(x+h/np.power(2,i))-f(x-h/np.power(2,i)))/(2*h/np.power(2,i))
    for i in range(1,n):
        for j in range(i,n):
            N[j,i]=N[j,i-1]+(N[j,i-1]-N[j-1,i-1])/(np.power(2,i)-1)
    return N
