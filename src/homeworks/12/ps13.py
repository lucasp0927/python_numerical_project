## module polyFit
import numpy as np
from ps12 import *
def polyFit(xData,yData,m):
    ''' 
    Returns coefficients of the polynomial
    p(x) = c[0] + c[1]x + c[2]x^2 +...+ c[m]x^m
    that fits the specified data in the least
    squares sense.

    USAGE:
        c = polyFit(xData,yData,m)
    INPUT:
        xData,yData : numpy arrays
            data to be fitted
        m : int
            degree of p(x)
    OUTPUT:
        c : numpy array
    coefficients of p(x)
    '''
    A=np.Zero(m+1,m+1)
    b=np.Zero(m+1)
    n=len(xdata)
    for j in range(m+1):
        for k in range(m+1):
            sum=0
            for i in range(n+1):
                sum=sum+x[i]**(j+k)
            A[k][j]=sum
    for k in range(m+1):
        sum=0
        for i in range(n+1):
            sum=sum+y[i]*(x[i]**(k))
        b[k]=sum
    x = LUdecomp(A)
    return LUsolve(x,b)
    
    
    

def stdDev(c, xData, yData):
    '''
    Computes the std. deviation between p(x)
    and the data.
    USAGE:
        sigma = stdDev(c,xData,yData)
    INPUT:
        xData,yData : numpy arrays
            data to be fitted
        c : numpy array
            coefficients of p(x)
    OUTPUT:
        sigma: float
            std. deviation
        '''
    def p(c,x,n):
        sum=0
        for i in range(len(c)+1):
            sum=sum+c[i]*(x**(i))
        return sum
    n= len(xdata)
    s=0
    for i in range(n+1):
        s=s+(ydata[i]-f(c,xdata(i),n))**2
    return math.sqrt(s/(n-len(c)))
