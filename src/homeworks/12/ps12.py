#!/usr/bin/python2
from __future__ import division
import numpy as np
from copy import copy

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
    #convert to float
    a,b = a.astype(np.float) , b.astype(np.float)
    n = b.shape[0]
    aug = np.hstack([a,b])
    #move largest number to pivot position, avoid round off error
    #forward
    for i in range(n):
        maxi = np.abs(aug[i:,i]).argmax()+i
        aug[i],aug[maxi] = copy(aug[maxi]),copy(aug[i])
        for j in range(i+1,n)[::-1]:
            aug[j,:] -= aug[i,:]*aug[j,i]/aug[i,i]
        aug[i,:] /= aug[i,i]
    #backward
    for i in range(n)[::-1]:
        for j in range(i):
            aug[j,:] -= aug[i,:]*aug[j,i]
    x = np.array([aug[:,-1]]).transpose()
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
        #convert to float
    a = a.astype(np.float)
    n = a.shape[0]
    L = np.zeros([n,n])
    aug = a
    for i in range(n):
        for j in range(i+1,n)[::-1]:
            t = aug[j,i]/aug[i,i]
            aug[j,:] -= aug[i,:]*aug[j,i]/aug[i,i]
            L[j,i] = t
    aug = L+aug
    return aug

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
    n = a.shape[0]
    U = np.triu(a)
    L = np.tril(a)
    for i in range(n):
        L[i,i] = 1

    tmp = np.hstack([L,b])
    for i in range(n):
        for j in range(i+1,n):
            tmp[j,:] -= tmp[i,:]*tmp[j,i]
    y = np.array([tmp[:,-1]]).transpose()
    tmp = np.hstack([U,y])
    for i in range(n):
        tmp[i] /= tmp[i,i]
    for i in range(n)[::-1]:
        for j in range(i):
            tmp[j,:] -= tmp[i,:]*tmp[j,i]
    x = np.array([tmp[:,-1]]).transpose()
    return x

if __name__ == '__main__':
    a = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]])
    b = np.array([[8],[-11],[-3]])
    x = gaussElimin(a,b)
    print x
    x = LUdecomp(a)
    print LUsolve(x,b)
    pass


