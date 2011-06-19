import numpy as np
from ps12 import*
from math import*

## module polyFit
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
    n=len(xData)
    A=np.zeros((m+1,m+1))
    b=np.zeros((m+1,1))
    tmp=np.zeros((2*m+1,1))
    for i in range(len(tmp)):
       s=0
       for j in range(n):
          s+=xData[j]**i
       tmp[i][0]=s
    
    for i in range(m+1):
       for j in range(m+1):
          A[i][j]=tmp[i+j]
    
    for i in range(m+1):
       for j in range(n):
          b[i]+=(xData[j]**i)*(yData[j])
    c=LUsolve(A,b)
    return c

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
    m=len(c)
    n=len(xData)
    S=0
    for i in range(n):
       tmp=0
       for j in range(m):
          tmp+=c[j]*(xData[i]**j)
       S+=(yData[i]-tmp)**2
    return sqrt(float(S)/(n-m+1))

