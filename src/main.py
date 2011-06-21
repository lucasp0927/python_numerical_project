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

##############
b=1
############

tstart=time.time()
#Amp, w, b, x0,v0,x_int,l,c=paraRead('input.in')
# Amp : amplitude in A cos (w t)
# w   : angular frequency
# x0, v0: initial conditions
# x_int : interception point
# l : distance from the motion
# c : velocity of the bullet
filepath = 'data/sample'
for index in range(1):
    #filename = filepath + str(index+1) + '.dat'
    filename="test.dat"
    tdata,xdata,vdata = dataRead(filename)
    adata=df(tdata,vdata)[1]
    P2=adata+b*vdata[1:-1]
    tdata=tdata[1:-1]
    fit2=polyFit(tdata,P2,2)
    fit3=polyFit(tdata,P2,3)
    if stdDev(fit2,tdata,P2)>stdDev(fit3,tdata,P2):
       fit=fit3
    fit=fit2
    plt.plot(tdata,P2)
plt.show()    
print 'Total time:', (time.time()-tstart)
