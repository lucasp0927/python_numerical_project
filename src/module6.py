'''Module 6: exact solution
'''
import numpy as np
import scipy as sp
import scipy.integrate as inte
def exactSol(Amp, w, x0,v0,t0,x_int):


    with open('param.in') as fin:
        for line in fin:
            data=line.split()
            a0=float(data[0])
            a1=float(data[1])
            a2=float(data[2])
            a3=float(data[3])
            b=float(data[4])

    
    xinit=[x0,v0]
    print 'a0={0:6.4f} a1={1:6.4f} a2={2:6.4f} a3={3:6.4f}'.format(a0,a1,a2,a3)
    dt=1e-5
    t=np.arange(0,t0+dt,dt)
    y=inte.odeint(f,xinit,t,args=(a0,a1,a2,a3,b,Amp,w))
    with open('exact.dat','w') as fout:
        for i in range(len(y)):
            fout.write('%10.6f %10.6f\n' % (t[i],y[i,0]))
    error=abs(float(y[-1,0])-x_int)/x_int 
    #print 'error: {0:8.2%}'.format( error)
    return t,y[:,0],error
def f(x,t,a0,a1,a2,a3,b,Amp,w):
    x0=x[0]
    x1=x[1]
    return [float(x1),(a0+a1*x0+a2*x0**2+a3*x0**3)-b*x1+Amp*np.cos(w*t)]
