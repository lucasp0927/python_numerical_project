#Problem 14
#Name: Chao Jung Lee --b97202070
#Collaborators: Cheng Kai Huang -- b97201047
#group 9
#Time: 1hr





import numpy as np
import matplotlib.pyplot as plt

def rk4( f, x0, t ):
    x=np.zeros(len(t))
    x[0]=x0
    for j in range(1,len(t)):  #suppose t:t0~tn ,len(t)=n+1 , index go from 1 to n
        h=t[j]-t[j-1]
        K1=h*f(t[j-1],x[j-1])
        K2=h*f(t[j-1]+0.5*h,x[j-1]+0.5*K1)
        K3=h*f(t[j-1]+0.5*h,x[j-1]+0.5*K2)
        K4=h*f(t[j-1]+h,x[j-1]+K3)
        x[j]=x[j-1]+(1.0/6.0)*(K1+2*K2+2*K3+K4)
    return(x)
  
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
#testing code

##def F(t,x):
##    z=np.cos(2*t)
##    return z
##t=np.zeros(200)
##for i in range(1,200): #t0~t99
##    t[i]=t[i-1]+0.05
##
##x0=1
##
##X=rk4(F,x0,t)  #numerical solution
####
####print 'X',X
####print't',t
##def H(t): #analytical solution
##    return (0.5*np.sin(2*t)+1)
##
####print'H(t)',H(t)
####print 'X(t)',X
####print 'len of X',len(X)
####print 'len of H',len(H(t))
####print 'len of t',len(t)
####print 'analytical result\n'
##plt.plot(t,H(t),'gd')
##plt.show()
##
####print'numerical result\n'
##plt.plot(t,X,'rx')
##plt.show()
##
####print H(t)-X # difference between numerical and analytical




    
    
