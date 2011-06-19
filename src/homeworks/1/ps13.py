## module polyFit

from numpy import *

##xData=array([18,30,15,12])
##yData=array([15,30,32,21])


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
    n=len(a)
    x=zeros(n)
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
    x[n-1]=b[n-1,0]/a[n-1,n-1]
    for i in range(n-2,-1,-1):
        v=b[i,0]
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
    M=zeros([m+1,m+1])
    Y=zeros([m+1,1])
    for i in range(m+1):
        s=sum(power(xData,i))
        for j in range(i+1):
            M[i-j,j]=s
    for i in range(m):
        s=sum(power(xData,2*m-i))
        for j in range(i+1):
            M[m-(i-j),m-j]=s

    for i in range(m+1):
        Y[i,0]=sum(power(xData,i)*yData)
    
    return gaussElimin(M,Y)

    

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
    z=zeros(len(xData))
    for i in range(len(xData)):
        for j in range(len(c)):
            z[i]+=c[j]*power(xData[i],j)
    return sum(power(yData-z,2))


        
##print polyFit(xData,yData,3)
##ans=polyFit(xData,yData,2)
##print stdDev(ans, xData, yData)
##for i in range(len(ans)):
##    ans[i]+=0.0001
##    print stdDev(ans, xData, yData)
##    ans[i]-=0.0002
##    print stdDev(ans, xData, yData)
##    ans[i]+=0.0001

