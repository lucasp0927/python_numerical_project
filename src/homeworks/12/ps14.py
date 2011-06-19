#!/usr/bin/python2
import numpy as np
import matplotlib.pyplot as plt
def rk4( f, x0, t ):
    """Fourth-order Runge-Kutta method to solve x' = f(x,t) with x(t[0]) = x0.

    USAGE:
        x = rk4(f, x0, t)

    INPUT:
        f     - function of x and t equal to dx/dt.  x may be multivalued,
                in which case it should a list or a NumPy array.  In this
                case f must return a NumPy array with the same dimension
                as x.
        x0    - the initial condition(s).  Specifies the value of x when
                t = t[0].  Can be either a scalar or a list or NumPy array
                if a system of equations is being solved.
        t     - list or NumPy array of t values to compute solution at.
                t[0] is the the initial condition point, and the difference
                h=t[i+1]-t[i] determines the step size h.

    OUTPUT:
        x     - NumPy array containing solution values corresponding to each
                entry in t array.  If a system is being solved, x will be
                an array of arrays.
    """
    x=[x0]
    for i,t_i in enumerate(t[:-1]):
        h = t[i+1] - t_i
        k1 = h*f(x[i],t_i)
        k2 = h*f(x[i]+0.5*k1,t_i+0.5*h)
        k3 = h*f(x[i]+0.5*k2,t_i+0.5*h)
        k4 = h*f(x[i]+k3,t_i+h)
        x.append(x[i]+1.0/6.0*(k1+2*k2+2*k3+k4))
    return np.array(x)

def main():
    def f(x,t):
        return np.array([x[1],-x[0]])
    t = np.linspace(0,10,100)
    x= rk4(f,np.array([0,0.1]),t)
#    print x
    # plt.plot(t,x[:,0])
    # plt.plot(t,x[:,1])    
    # plt.show()
