'''Module 2, Differentiation Module
    Implments two functions df to carry out the first 
    derivatives of a list of data on equally spaced interval
'''
import numpy as np
def df(x,y):
    ''' Compute the first derivate of y(x) numerically, using the three-point
    central difference formula and assuming x is equally-spaced.
    USAGE:
    xout, out= df(x,y)
    INPUT 
        x: 1D numpy array of equally-spaced points
        y: 1D numpy array of function y(x_i)
    OUTPUT
        xout: 1D numpy array
            x points where the numerically derivative is valid
        out:  1D numpy array
            first derivative of y at points xout
    '''    
