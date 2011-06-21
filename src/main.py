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
b=1.0
Amp=1.0
w=1.0
x0=1.0
v0=1.0
x_int=2.5
l=1.0
c=1.0
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
fit=np.zeros(4)
#for test n=1,when in use, n should be change to n=20
n=20
for index in range(n):
    filename = filepath + str(index+1) + '.dat'
    #filename="test.dat"
    tdata,xdata,vdata = dataRead(filename)
    adata=df(tdata,vdata)[1]
    P2=adata+b*vdata[1:-1]
    tdata=tdata[1:-1]
    fit3=polyFit(tdata,P2,3)
    #print fit3
    #plt.plot(tdata,P2,tdata,fit3[0]+fit3[1]*tdata+fit3[2]*tdata**2+fit3[3]*tdata**3)
    fit+=fit3
    #if stdDev(fit2,tdata,P2)>stdDev(fit3,tdata,P2):
    #   fit+=fit3
    #   print "111111111111111111111"
    #else:
    #   fit+=fit2
fit/=float(n)
#plt.plot(tdata,P2,tdata,fit[0]+fit[1]*tdata+fit[2]*tdata**2+fit[3]*tdata**3)
def spring(x,t):
   x0=x[0]
   x1=x[1]
   return np.array([x1,fit[0]+fit[1]*x0+fit[2]*x0**2+fit[3]*x0**3-b*x1+Amp*np.cos(w*t)])
#the time range is tdata[1:-1] ,x[:,0]:position,x[:,1]velocity
x=odeSolve(spring,[x0,v0],tdata)
#the answer:firing time
t=firing(tdata,x[:,0],x_int,l,c)

##############  verify #######################
print "firing time",t
#plt.plot(tdata,x[:,0])
#plt.show()    
print 'Total time:', (time.time()-tstart)
###########################################
