#!/usr/bin/env python
from module0 import *
from module1 import *
from module2 import *
from module3 import *
from module4 import *
from module5 import *
from module6 import *
import numpy as np
import time 

tstart=time.time()

# x"(t)=f(x)-b*v+Amp*cos(w*t)
# x_int: interception x
# l: distance from the motion direction
# c: bullet velocity

Amp, w, b, x0,v0,x_int,l,c=paraRead()

###### 


# Your Code Gose Here


#############

tsol=time.time()
print 'solution phase elasped time:',tsol-tstart

# exact solution
# t_exact: time series of the exact solution
# x_exact: exact solution of x at t_exact
t_exact, x_exact, error=exactSol(Amp, w, x0,v0,t0+l/c,x_int)
print 'error: {0:8.2%}'.format( error)

print 'exact phase elapsed time:',time.time()-tsol
print 'total time:',time.time()-tstart
