#!/usr/bin/python2
import numpy as np

import ps12
def main():
    a = np.array([[2,1,-1],[-3,-1,2],[-2,1,2]])
    b = np.array([[8],[-11],[-3]])
    x = ps12.gaussElimin(a,b)
    x = ps12.LUdecomp(a)
    y = ps12.LUsolve(x,b)
    



    
