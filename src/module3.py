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
    x=np.zeros([n,1])
    for k in range(n-1):
        for i in range(k+1,n):
            l=a[i,k]/a[k,k]
            a[i,k]=0
            for j in range(k+1,n):
                a[i,j]=a[i,j]-l*a[k,j]
            b[i,0]=b[i,0]-l*b[k,0]
    x[(n-1),0]=b[(n-1),0]/a[n-1,n-1]
    for i in range(n-2,-1,-1):
        v=b[i,0]
        for j in range(i+1,n):
            v=v-a[i,j]*x[j,0]
        x[i,0]=v/a[i,i]
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
    x=np.zeros([n,1])
    y=np.zeros([n,1])
    y[0,0]=b[0,0]
    for i in range(1,n):
        v=b[i,0]
        for j in range(i):
            v=v-a[i,j]*y[j,0]
        y[i,0]=v

    x[(n-1),0]=y[(n-1),0]/a[n-1,n-1]
    for i in range(n-2,-1,-1):
        v=y[i,0]
        for j in range(i+1,n):
            v=v-a[i,j]*x[j,0]
        x[i,0]=v/a[i,i]
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
