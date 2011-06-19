## module polyFit
#-*-coding:utf-8-*-
#Problem 11
#Name:Yu-Yi Kuo, Cheung Hei Ya
#Collaborators:
#Time:3:00
import numpy as np
import math

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
    from ps12 import*
    A=np.zeros((m,m))
    b=np.zeros((m,1))
    for i in range(0,m):
        for j in range(i,m):
            for x in xData:
                A[i,j]+=float(x)**(i+j)
            A[j,i]=A[i,j]
    for i in range(0,m):
        for k in range(0,m):
            b[i,0]+=float(yData[k])*(float(xData[k])**i)
    a=np.zeros((m,1))
    a=gaussElimin(A,b)
    return a

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
    s=0
    L=[]
    n=len(xData)
    m=c.size
    for i in range(0,n):
        f=0
        for j in range(0,m):
            f+=c[j,0]*float(xData[i])**j
        L.append((y[i]-f)**2)
    s=sum(L)
    sigma=math.sqrt(s/(n-m))
    return sigma


        
             

