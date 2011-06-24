'''Module 3: Polynomial Fit Module
   Implments  functions polyFit, and stdDev
'''
#polyFit and stddev using module from group12, not test yet
#Others are from 1st group, tested.
import numpy as np

def gaussElimin(a,b):
    """Solves [a]{b} = {x} by Gauss elimination.
    USAGE:
        x = gaussElimin(a,b)
    INPUT:
        a       -numpy array (n*n)
        b       -numpy array (n*1)
    OUTPUT:
        x       -numpy array (n*1)
    """
    a=a*1.0
    b=b*1.0
    n=len(a)
    x=np.zeros(n)
    for k in range(n-1):
        i=1
        while a[k,k]==0:
            for j in range(k,n):
                c=a[k,j]
                a[k,j]=a[k+i,j]
                a[k+i,j]=c
            c=b[k,0]
            a[k,0]=a[k+i,0]
            a[k+i,0]=c
            i+=1
        for i in range(k+1,n):
            l=a[i,k]/a[k,k]
            a[i,k]=0
            for j in range(k+1,n):
                a[i,j]=a[i,j]-l*a[k,j]
            b[i,0]=b[i,0]-l*b[k,0]
    x[(n-1)]=b[(n-1),0]/a[n-1,n-1]
    for i in range(n-2,-1,-1):
        v=b[i,0]
        for j in range(i+1,n):
            v=v-a[i,j]*x[j]
        x[i]=v/a[i,i]
    return x

def LUdecomp(a):
    """ LU decomposition: [L][U] = [a].
    USAGE:
        a = LUdecomp(a)
    INPUT
        a       -numpy array (n*n)
    OUTPUT
        a       -numpy array (n*n)
    The returned matrix [a]=[L\U] contains [U] in the upper triangle
    and the nondiagonal terms of [L] in the lower triangle.
    """
    a=a*1.0
    n=len(a)
    for k in range(n-1):
        for i in range(k+1,n):
            l=a[i,k]/a[k,k]
            a[i,k]=l
            for j in range(k+1,n):
                a[i,j]=a[i,j]-l*a[k,j]
    return a

def LUsolve(a,b):
    """Solves [L][U]{x} = b, where [a] = [L\U] is the matrix
    returned from LUdecomp.
    USAGE:
        x = LUsolve(a,b)
    INPUT:
        a       -numpy array (n*n)
        b       -numpy array (n*1)
    OUTPUT
        x       -numpy array (n*1)
    """
    a=a*1.0
    b=b*1.0
    n=len(a)
    x=np.zeros(n)
    y=np.zeros([n,1])
    y[0,0]=b[0,0]
    for i in range(1,n):
        v=b[i,0]
        for j in range(i):
            v=v-a[i,j]*y[j,0]
        y[i,0]=v

    x[n-1]=y[(n-1),0]/a[n-1,n-1]
    for i in range(n-2,-1,-1):
        v=y[i,0]
        for j in range(i+1,n):
            v=v-a[i,j]*x[j]
        x[i]=v/a[i,i]
    return x

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
    M=np.zeros([m+1,m+1])
    Y=np.zeros([m+1,1])
    for i in range(m+1):
        s=sum(np.power(xData,i))
        for j in range(i+1):
            M[i-j,j]=s
    for i in range(m):
        s=sum(np.power(xData,2*m-i))
        for j in range(i+1):
            M[m-(i-j),m-j]=s

    for i in range(m+1):
        Y[i,0]=sum(np.power(xData,i)*yData)
    
#    return gaussElimin(M,Y)
    return LUsolve(LUdecomp(M),Y)

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
    z=np.zeros(len(xData))
    for i in range(len(xData)):
        for j in range(len(c)):
            z[i]+=c[j]*np.power(xData[i],j)
#    return np.power(sum(np.power(yData-z,2))/len(xData),0.5)
    return sum(np.abs(yData-z)/z)/len(yData)

