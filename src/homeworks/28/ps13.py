import numpy as np
from ps12 import *
def polyFit(xData,yData,m):
    A=np.zeros([m+1,m+1])
    b=np.zeros([m+1,1])
    
    for k in range(m+1):
        for j in range(m+1):
            for i in range(len(xData)):
                A[k,j]+=xData[i]**(j+k)
        for i in range(len(xData)):
            b[k]+=xData[i]**k*yData[i]
            
    return gaussElimin(A,b)

