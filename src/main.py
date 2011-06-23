#!/usr/bin/python2
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

def main():
    #old_settings = np.seterr(all='raise')
    #np.geterr()
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
    # Amp : amplitude in A cos (w t)
    # w   : angular frequency
    # x0, v0: initial conditions
    # x_int : interception point
    # l : distance from the motion
    # c : velocity of the bullet


    ###########################################
    #Our codes start here
    ##########################################

    def poly(n,x,fit):

        ans=0.0
        for i in range(n+1):
    #        print x,fit[i],i
            ans += fit[i]*x**i
        return ans

    fit_n = 3
    filepath = 'data'
    fit=np.zeros(fit_n+1)
    #for test n=1,when in use, n should be change to n=20
    n=20
    for index in range(n):
        filename = filepath + str(index+1) + '.dat'
        tdata,xdata,vdata = dataRead(filename)

    #    xdata[10:-10]=smooth(xdata)[10:-10]
    #    vdata[10:-10]=smooth(vdata)[10:-10]
        xdata=smooth(xdata,window_len=50,window='flat')
        vdata=smooth(vdata,window_len=50,window='flat')

        adata=df(tdata,vdata)[1]
#        plt.plot(tdata[1:-1],adata)
        adata=smooth(adata,window_len=50,window='hamming') #hamming window is really good here
#        plt.plot(tdata[1:-1],adata)

        #TODO add a sorter to sort x
        P2=adata+b*vdata[1:-1]
    #    P2[10:-10]=smooth(P2)[10:-10]
    #    P2 = smooth(P2,window_len=10)
        tdata=tdata[1:-1]
        xdata=xdata[1:-1]
        fit3=polyFit(xdata,P2,fit_n)
        #print fit3
    #    plt.plot(xdata,P2,xdata,poly(fit_n,xdata,fit3))
        fit+=fit3
    #plt.plot(tdata,vdata[1:-1])
    #plt.plot(tdata,adata)
#    plt.show()
    fit/=float(n)
    print fit

    def spring(x,t):
       x0=x[0]
       x1=x[1]
       return np.array([x1,poly(fit_n,x0,fit)-b*x1+Amp*np.cos(w*t)])
    #   return np.array([float(x1),fit[0]+fit[1]*x0+fit[2]*x0**2+fit[3]*x0**3-b*x1+Amp*np.cos(w*t)])
    #the time range is tdata[1:-1] ,x[:,0]:position,x[:,1]velocity

    #################################
    #Here are three DE solver in module4
    ################################
    #tdata = np.mgrid[tdata[0]:tdata[-1]:0.001]

    #x_de=odeSolve(spring,[x0,v0],tdata)
    #x_de=pc4(spring,[x0,v0],tdata)
    x_de=rk452(spring,[x0,v0],tdata)
    #x_de,tdata=rk45(spring,[x0,v0],tdata[0],tdata[-1])

    #the answer:firing time
    t0=firing(tdata,x_de[:,0],x_int,l,c)

    ##############  verify #######################
    #print "firing time",t0
    #Eplt.plot(xdata,poly(fit_n,xdata,fit))
    #plt.plot(tdata,x_de[:,0])
    #plt.show()
    ###########################################
    #Our codes end here
    ##########################################

    #######################################
    #Below are code from professor's testkit
    ######################################
    tsol=time.time()
#    print 'solution phase elasped time:',tsol-tstart

    # exact solution
    # t_exact: time series of the exact solution
    # x_exact: exact solution of x at t_exact
    t_exact, x_exact, error=exactSol(Amp, w, x0,v0,t0+l/c,x_int)
    print 'error: {0:8.2%}'.format( error)
#    print 'exact phase elapsed time:',time.time()-tsol
#    print 'total time:',time.time()-tstart
    return error

if __name__ == '__main__':
    n=50.0
    err=0.0
    for i in range(int(n)):
        err+=main()
    print err/n*100
