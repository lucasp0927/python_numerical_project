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
    x0=np.float64(x0)
    t=np.float64(t)
    x=np.zeros((len(t),np.size(x0)))
    x[0]=x0
    h=t[1]-t[0]
    tj=t[0]
    xj=x0
    for j in range(1,len(t)):
       K1=h*f(tj,xj)
       K2=h*f(tj+0.5*h,xj+0.5*K1)
       K3=h*f(tj+0.5*h,xj+0.5*K2)
       K4=h*f(tj+h,xj+K3)
       xj+=(K1+2*K2+2*K3+K4)/6.0
       tj+=h
       x[j]=xj
    return x
def h(x,t):
   x0=x[0]
   x1=x[1]
   return [x1,0.25*x1-x0+np.sin(0.8*t)]
x0=np.array((0,0.2))
t=np.arange(0,10,0.01)
x=rk4(h,x0,t)
plt.plot(t,x)
plt.show()
#def f(t,x):
#   return x

#t=np.arange(100)/10.0
#print rk4(f,[1,2,3],t)
