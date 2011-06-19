#-*-coding:utf-8-*-
#Problem 14
#Name: 江衍德
#Collaborators: 楊燿綸
#Time: 0.5

import numpy as np

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
    for i in range(len(t)-1):
        h=t[i+1]-t[i]
        k1=h*f(x[-1],t[i])
        k2=h*f(x[-1]+0.5*k1,t[i]+0.5*h)
        k3=h*f(x[-1]+0.5*k2,t[i]+0.5*h)
        k4=h*f(x[-1]+k3,t[i]+h)
        x.append(x[-1]+(k1+2*k2+2*k3+k4)/6.0)
    return np.array(x)


