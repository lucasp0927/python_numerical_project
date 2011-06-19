##Problem Set14
##Group 32
##Names: Cheng, Yu-Hsung & Wu, Tsuei-Shin
##Time:

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
    x0 = np.array(x0)
    t = np.array(t)
    x = np.array([x0]*len(t),np.float64)
    x[0] = x0
    for j in range(len(t)-1):
        h = t[j+1]-t[j]
        K1 = h*f(x[j],t[j])
        K2 = h*f(x[j]+0.5*K1,t[j]+0.5*h)
        K3 = h*f(x[j]+0.5*K2,t[j]+0.5*h)
        K4 = h*f(x[j]+K3,t[j+1])
        x[j+1] = x[j]+(1.0/6)*(K1+2*K2+2*K3+K4)
    return x
    
    
