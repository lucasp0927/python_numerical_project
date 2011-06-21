#!/usr/bin/python2
#from module0 import *
from module1 import *
from module2 import *
from module3 import *
from module4 import *
from module5 import *
#from module6 import *
import matplotlib.pyplot as plt
import numpy as np
import time

tstart=time.time()
#Amp, w, b, x0,v0,x_int,l,c=paraRead('input.in')
# Amp : amplitude in A cos (w t)
# w   : angular frequency
# x0, v0: initial conditions
# x_int : interception point
# l : distance from the motion
# c : velocity of the bullet
filepath = 'data/sample'
for index in range(20):
    filename = filepath + str(index+1) + '.dat'
    tdata,xdata,vdata = dataRead(filename)
    print tdata
print 'Total time:', (time.time()-tstart)
