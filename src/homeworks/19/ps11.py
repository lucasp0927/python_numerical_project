#problem set 11
#Name:·¨ïúºú

#Collaborators: none
#Time:1:00
#
def f(x):
    return x**3+x

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
    return [(-f(xi+2*h) +4*f(xi+h) - 3*f(xi))/(2*h) for xi in x]
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
    return [(f(xi-2*h) -4*f(xi-h) + 3*f(xi))/(2*h) for xi in x]
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
    return [(f(xi+h)-f(xi-h))/(2*h) for xi in x]
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
                             most accurate estimate of f'(x).
    """
    import numpy as np
    R=np.zeros([n,n])
    for j in range (0, n):
        H = h/(2**j)
        R[j,0]= (f(x+H)-f(x-H))/(2*H)
    for i in range (1,n):
        for j in range (i,n):
            R[j,i]= R[j,i-1] + (R[j,i-1]-R[j-1,i-1])/(2**i-1)
    return R
        
