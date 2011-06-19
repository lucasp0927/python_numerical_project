#-*-coding:utf-8-*-
#Problem 12
#Name: Cheng, Yu-Hsung & Wu, Tsuei-Shin
#Collaborators: WCW
#Time: 4h

import numpy as np

def gaussElimin(a_,b_):
    """Solves [a]{b} = {x} by Gauss elimination.
    USAGE:
        x = gaussElimin(a,b)
    INPUT:
        a       -numpy array (n*n)
        b       -numpy array (n*1)
    OUTPUT:
        x       -numpy array (n*1)
    """
    a = np.array(a_, dtype=np.float64)[:len(a_)]
    b = np.array(b_, dtype=np.float64)[:len(b_)]
    for k in range(len(b)-1):
        for i in range(k+1,len(b)):
            lamda=a[i][k]/a[k][k]
            a[i][k]=0
            for j in range(k+1,len(b)):
                a[i][j]=a[i][j]-lamda*a[k][j]
            b[i]=b[i]-lamda*b[k]
    x=np.zeros((len(b),1))
    x[len(b)-1]=b[len(b)-1]/a[len(b)-1][len(b)-1]
    for i in range(len(b)-2,-1,-1):
        sum=b[i]
        for j in range(i+1,len(b)):
            sum=sum-a[i][j]*x[j]
        x[i]=sum/a[i][i]
    return x
   
def LUdecomp(a_):
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
    a = np.array(a_, dtype=np.float64)[:len(a_)]
    n = len(a)
    for k in range(n-1):
        for i in range(k+1,n):
            lumda = a[i][k]/a[k][k]
            a[i][k] = lumda
            for j in range(k+1,n):
                a[i][j] -= lumda*a[k][j]
    return a

    
def LUsolve(a_,b_):
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
    a = np.array(a_, dtype=np.float64)[:len(a_)]
    b = np.array(b_, dtype=np.float64)[:len(b_)]
    n= len(b)
##    L = np.zeros((n,n))
##    U = np.zeros((n,n))
##    for i in range(n):
##        L[i][i]=1
##        for j in range(n):
##            if j<i: L[i][j]=a[i][j]
##            else: U[i][j]=a[i][j]
##    y=gaussElimin(L,b)
##    x=gaussElimin(U,y)
    x = np.zeros((n,1))
    y = np.zeros((n,1))
    y[0] = b[0]
    for i in range(1,n):
        Sum = b[i]
        for j in range(i):#change 'i-1' to 'i'
            Sum -= (a[i][j])*y[j]
        y[i] = Sum
    x[n-1] = y[n-1]/(a[n-1][n-1])
    for i in range(n-2,-1,-1):
        Sum = y[i]#!! Here is y[i] instead of b[i] to compute x[i]
        for j in range(i+1,n):# I change 'i' to 'i+1'
            Sum -= (a[i][j])*x[j]
        x[i] = Sum/a[i][i]
    return x
