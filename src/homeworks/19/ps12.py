#-*-coding:utf-8-*-
#Problem 12
#Name: 江衍德
#Collaborators: 楊燿綸
#Time: 1.5 hr

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
    for x in range(len(a)-1):
        for i in range(x+1,len(a)):
            while a[(x,x)]==0:
                y=x+1
                a[x]=[a[(x,z)]+a[(y,z)] for z in range(len(a))]
                b[x]=b[x]+b[y]
                y+=1
            b[i]-=b[x]*a[(i,x)]/a[(x,x)]
            for j in range(len(a)-1,-1,-1):
                a[(i,j)]-=a[(x,j)]*a[(i,x)]/a[(x,x)]
    x=np.zeros((len(b),1))
    x[-1]=b[-1]/a[(-1,-1)]
    for i in range(len(x)-2,-1,-1):
        for j in range(i+1,len(a)):
            b[i]-=a[(i,j)]*x[j]
        x[i]=b[i]/a[(i,i)]
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
    for x in range(len(a)-1):
        for i in range(x+1,len(a)):
            for j in range(len(a)-1,x,-1):
                a[(i,j)]-=a[(x,j)]*a[(i,x)]/a[(x,x)]
            a[(i,x)]=a[(i,x)]/a[(x,x)]
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
    for i in range(1,len(a)):
        for j in range(i):
            b[i]-=a[(i,j)]*b[j]
    x=np.zeros((len(b),1))    
    x[-1]=b[-1]/a[(-1,-1)]
    for i in range(len(x)-2,-1,-1):
        for j in range(i+1,len(a)):
            b[i]-=a[(i,j)]*x[j]
        x[i]=b[i]/a[(i,i)]
    return x
