#-*-coding:utf-8-*-
#Problem 11
#Name:Yu-Yi Kuo, Cheung Hei Ya
#Collaborators:
#Time:3:00

import numpy as np

def gaussElimin(a,b):
    """Solves [a]{x} = {b} by Gauss elimination.
    USAGE:
        x = gaussElimin(a,b)
    INPUT:
        a       -numpy array (n*n)
        b       -numpy array (n*1)
    OUTPUT:
        x       -numpy array (n*1)
    """
    n=b.size
    a=np.float64(a.copy())
    b=np.float64(b.copy())
    for k in range(0,n-1):
        for i in range(k+1,n):
            c=a[i,k]/a[k,k]
            for j in range(k+1,n):
                a[i,j]=a[i,j]-c*a[k,j]
            b[i,0]=b[i,0]-c*b[k,0]
    x=np.zeros((n,1))
    x[n-1,0]=b[n-1,0]/a[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum=b[i,0]
        for j in range(i,n):
            sum=sum-a[i,j]*x[j,0]
        x[i,0]=sum/a[i,i]
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
    n=int(np.sqrt(a.size))
    a=np.float64(a.copy())
    for k in range(0,n-1):
        for i in range(k+1,n):
            c=a[i,k]/a[k,k]
            a[i,k]=c
            for j in range(k+1,n):
                a[i,j]=a[i,j]-c*a[k,j]
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
    a=np.float64(a.copy())
    b=np.float64(b.copy())
    LU=LUdecomp(a)
    n=b.size
    y=np.zeros((n,1))
    x=np.zeros((n,1))
    y[0,0]=b[0,0]
    for i in range(1,n):
        sum = b[i,0]
        for j in range(0,i):
            sum=sum-LU[i,j]*y[j,0]
        y[i,0]=sum
    x[n-1,0]=y[n-1,0]/LU[n-1,n-1]
    for i in range(n-2,-1,-1):
        sum=y[i,0]
        for j in range(i,n):
            sum=sum-LU[i,j]*x[j,0]
        x[i,0]=sum/LU[i,i]
    return x
