#!/usr/bin/python2.6
from module0 import *
from module1 import *
from module2 import *
from module3 import *
from module4 import *
from module5 import *
from module6 import *
import matplotlib.pyplot as plt
import numpy as np
import time

##############
# b=2.0
# Amp=1.0
# w=1.0
# x0=1.0
# v0=1.0
# x_int=0.5
# l=1.0
# c=1.0
############

tstart=time.time()

Amp, w, b, x0,v0,x_int,l,c=paraRead()
#print paraRead()
# Amp : amplitude in A cos (w t)
# w   : angular frequency
# x0, v0: initial conditions
# x_int : interception point
# l : distance from the motion
# c : velocity of the bullet


###########################################
#Our codes start here
##########################################
filepath = 'data'
fit=np.zeros(4)
#for test n=1,when in use, n should be change to n=20
n=20
for index in range(n):
    filename = filepath + str(index+1) + '.dat'
    tdata,xdata,vdata = dataRead(filename)
    adata=df(tdata,vdata)[1]
    P2=adata+b*vdata[1:-1]
    tdata=tdata[1:-1]
    xdata=xdata[1:-1]
    fit3=polyFit(xdata,P2,3)
    #print fit3
#    plt.plot(xdata,P2,xdata,fit3[0]+fit3[1]*xdata+fit3[2]*xdata**2+fit3[3]*xdata**3)
#    plt.plot(tdata,adata)
    print fit3
    fit+=fit3
#plt.show()
fit/=float(n)
def spring(x,t):
   x0=x[0]
   x1=x[1]
   return np.array([x1,fit[0]+fit[1]*x0+fit[2]*x0**2+fit[3]*x0**3-b*x1+Amp*np.cos(w*t)])
#the time range is tdata[1:-1] ,x[:,0]:position,x[:,1]velocity

#x=odeSolve(spring,[x0,v0],tdata)
x=pc4(spring,[x0,v0],tdata)
#x=rk45(spring,[x0,v0],tdata)

#the answer:firing time
t0=firing(tdata,x[:,0],x_int,l,c)

##############  verify #######################
print "firing time",t0
#plt.plot(tdata,x[:,0])
#plt.show()
###########################################
#Our codes end here
##########################################

#######################################
#Below are code from professor's testkit
######################################
tsol=time.time()
print 'solution phase elasped time:',tsol-tstart

# exact solution
# t_exact: time series of the exact solution
# x_exact: exact solution of x at t_exact
t_exact, x_exact, error=exactSol(Amp, w, x0,v0,t0+l/c,x_int)
print 'error: {0:8.2%}'.format( error)

print 'exact phase elapsed time:',time.time()-tsol
print 'total time:',time.time()-tstart
