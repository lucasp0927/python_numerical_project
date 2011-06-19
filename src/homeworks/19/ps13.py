#-*-coding:utf-8-*-
#Problem 13
#Name: 楊燿綸
#Collaborators: 江衍德
#Time: 2 hr

import numpy as np
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
    import numpy as np
    from ps12 import gaussElimin
    def SUM1(j,k,x):
        s = 0
        for i in range (len(x)):
            s = x[i]**(j+k) + s
        return s
    def SUM2(k,x,y):
        s = 0
        for i in range (len(y)):
            s = x[i]**k * y[i] + s
        return s
    a = np.zeros([m+1,m+1])
    for j in range (m+1):
        for k in range (m+1):
            a[k,j] = SUM1(j,k,xData)
    b = np.zeros([m+1,1])
    for k in range (m+1):
        b[k,0] = SUM2(k,xData,yData)
    x = gaussElimin(a,b)
    return x
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
    def f(i,c):
        f = np.float(0)
        for j in range (len(c)):
            f = f + c[j]*xData[i]**j
        return f
    S = np.float(0)
    for i in range (len(xData)):
        S = S + float((yData[i]-f(i,c))**2)
    sigma = (S/(len(xData)-len(c)+1))**(1/2.)
    return sigma
             

