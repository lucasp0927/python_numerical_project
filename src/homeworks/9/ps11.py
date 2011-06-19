#-*-coding:utf-8-*-
#Problem 11
#Name:Cheng Kai Huang
#Collaborators:Chao Jung Lee
#Time:one hours
import math
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
    for i in range(len(x)):
        df.append(float((-f(x[i]+2*h)+4*f(x[i]+h)-3*f(x[i]))/(2*h)))
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
    for i in range(len(x)):
        df.append(float((f(x[i]-2*h)-4*f(x[i]-h)+3*f(x[i]))/(2*h)))
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
    for i in range(len(x)):
        df.append(float((f(x[i]+h)-f(x[i]-h))/(2*h)))
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
    def N(j,h):
        if j==1:
            return float((f(x+h)-f(x))/(h))
        else:
            return N(j-1,h/2.0)+(N(j-1,h/2.0)-N(j-1,h))/(2**(j-1)-1)
    arr=np.zeros((n,n))
    for i in range(n):
        for j in range(i+1):
            arr[i][j]=N(j+1,h*2**(-i+j))
    return arr
            
    
##x=1
##hk=0.01
##print richardson( math.sin, x, 5, hk )
    
