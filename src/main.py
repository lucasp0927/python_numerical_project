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


def noise_level():
    '''
    use stdDev to calculate the noise level.
    '''
    noise_level = 0
    for i in range(20):
        filename = 'data' + str(i+1) + '.dat'
        tdata,xdata,vdata = dataRead(filename)
        #calculate xdata's noise level
        fit=polyFit(tdata,xdata,5)
        noise =  stdDev(fit,tdata,xdata)
        noise_level+=noise
        #calculate vdata's noise level
        fit=polyFit(tdata,vdata,5)
        noise =  stdDev(fit,tdata,vdata)
        noise_level+=noise
    # impirical formula
    noise_level=noise_level*100/20
    print 'noise level is: '+str(noise_level)
    return noise_level


def poly(n,x,fit):
    ans=0.0
    for i in range(n+1):
        ans += fit[i]*x**i
    return ans

def main():
    tstart=time.time()
    Amp, w, b, x0,v0,x_int,l,c=paraRead()
#    print paraRead()
    # Amp : amplitude in A cos (w t)
    # w   : angular frequency
    # x0, v0: initial conditions
    # x_int : interception point
    # l : distance from the motion
    # c : velocity of the bullet
    fit_n = 3
    filepath = 'data'
    fit=np.zeros(fit_n+1)
    
    nl=noise_level()                    # calculate noise level
#    nl=0
    
    n=20 #sample file number
    for index in range(n):
        filename = filepath + str(index+1) + '.dat'
        tdata,xdata,vdata = dataRead(filename)
#        plt.plot(tdata,xdata)

        # if noise level bigger than 3 start smoothing
        if nl>3.0:
            xdata=smooth(xdata,window_len=int((nl-2)*4),window='gaussian')
            vdata=smooth(vdata,window_len=int(nl-2)*4,window='gaussian')
            
 #       xdata = poly(8,tdata,polyFit(tdata,xdata,8)) #to use this method uncomment nl=0
#        vdata = poly(8,tdata,polyFit(tdata,vdata,8))
#        plt.plot(tdata,xdata)        
        adata=df(tdata,vdata)[1]

        if nl>3.0:
            adata=smooth(adata,window_len=int((nl-2)*6.9),window='hamming') #hamming window is really good here 104 best for dataset2

        P2=adata+b*vdata[1:-1]
        tdata=tdata[1:-1]
        xdata=xdata[1:-1]
        fit3=polyFit(xdata,P2,fit_n)
#        plt.plot(xdata,P2,xdata,poly(fit_n,xdata,fit3))
        fit+=fit3
#    plt.show()
    fit/=float(n)
#    print fit

    def spring(x,t):
       x0=x[0]
       x1=x[1]
       return np.array([x1,poly(fit_n,x0,fit)-b*x1+Amp*np.cos(w*t)])
    #the time range is tdata[1:-1] ,x[:,0]:position,x[:,1]velocity

    #################################
    #Here are three DE solver in module4
    ################################
    tdata = np.mgrid[tdata[0]:tdata[-1]:0.0005]

    #x_de=odeSolve(spring,[x0,v0],tdata)
    #x_de=pc4(spring,[x0,v0],tdata)
    x_de=rk452(spring,[x0,v0],tdata)
    #x_de,tdata=rk45(spring,[x0,v0],tdata[0],tdata[-1])

    #the answer:firing time
    t0=firing(tdata,x_de[:,0],x_int,l,c)

    ##############  verify #######################
    #print "firing time",t0
    #Eplt.plot(xdata,poly(fit_n,xdata,fit))
#    plt.plot(tdata,x_de[:,0])
#    plt.show()

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
#    return error

def test():
    n=10
    err=0.0
    # err_m = []
    # w_m = np.linspace(70,130,20)
    # for w in w_m:
    #     err=0.0
    #     for i in range(int(n)):
    #         err+=main(w)
    #     err_m.append(err/n*100)
    # print zip(w_m,err_m)
    for i in range(n):
        err += main()
    print err/float(n)
    
if __name__ == '__main__':
    main()
#     test()
