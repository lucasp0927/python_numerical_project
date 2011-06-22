#!/usr/bin/env python
import numpy as np
import scipy as sp
from math import cos
from scipy.integrate import odeint
import matplotlib.pyplot as plt

# Parameters
a0=float( raw_input('a0='))
a1=float( raw_input('a1='))
a2=float( raw_input('a2='))
a3=float( raw_input('a3='))
b= float( raw_input('b ='))
# Output to param.in
with open('param.in','w') as fout:
    fout.write('%10.6f %10.6f %10.6f %10.6f %10.6f\n' % (a0,a1,a2,a3,b))

# Input values for solving the final ODE

Amp=float( raw_input('Amp='))
w =float( raw_input('w='))
x0=float( raw_input('x0='))
v0=float( raw_input('v0='))

# Noise level for randomizing data

noise=float(raw_input('noise level='))

# Output to input.in
with open('input.in','w') as fout:
    fout.write('%10.6f %10.6f %10.6f %10.6f\n' % (Amp, w, x0, v0))

# x"(t)=f(x)-b*v+A cos(wt)
def fp(x,t):
    x0=x[0]
    x1=x[1]
    return [float(x1),(a0+a1*x0+a2*x0**2+a3*x0**3)-b*x1+Amp*np.cos(w*t)]
# x"(t)=f(x)-b*v
def f(x,t):
    x0=x[0]
    x1=x[1]
    return [float(x1),(a0+a1*x0+a2*x0**2+a3*x0**3)-b*x1]
# Jacobian of f(x)-b*v
def jac(x,t):
    x0=x[0]
    x1=x[1]
    return [[0,1],[a1+2.*a2*x0+3.*a3*x0**2,-b]]
def df(x,y):
    n=len(y)
    h=(x[-1]-x[0])/n
    out=[]
    for i in range(1,n-1):
        out.append(float((y[i+1]-y[i-1])/2./h))
    xout=x[1:n-1]
    return (np.array(xout), np.array(out))
t=np.arange(0,5.0,0.01)
xinit=[x0,v0]
y=odeint(fp,xinit,t)
with open('exactsol.dat','w') as fout:
    for i in range(len(y)):
        fout.write('{0:10.6f} {1:10.6f}\n'.format(float(t[i]),float(y[i,0])))
with open('maxmin.dat','w') as fout:
   fout.write('%10.6f %10.6f\n' %( y[:,0].min(),y[:,0].max()))
for i in range(1,21):
    xinit=[i*0.01,i*.01]

    y=odeint(f,xinit,t,Dfun=jac,printmessg = False)
    yn=y[:,0]+noise*y[:,0]*np.random.normal(size=len(t))
    vn=y[:,1]+noise*y[:,1]*np.random.normal(size=len(t))

    filname='data'+str(i)+'.dat'
    fout=open(filname,'w')
    for k in range(len(t)):
        fout.write('%10.8f  %10.8f %10.8f\n' % (t[k],yn[k],vn[k]))
    fout.close()
