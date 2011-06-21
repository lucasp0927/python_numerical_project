'''Module 4: ODE solver
   Implement function odeSolve
'''
import numpy as np
def odeSolve( f, x0, t ):
    """ODE solver to x' = f(x,t) with x(t[0]) = x0.

    USAGE:
        x = odeSolve(f, x0, t)

    INPUT:
        f     - function of x and t equal to dx/dt.  x may be multivalued,
                in which case it should a list or a NumPy array.  In this
                case f must return a Np array with the same dimension
                as x.
        x0    - the initial condition(s).  Specifies the value of x when
                t = t[0].  Can be either a scalar or a list or Np array
                if a system of equations is being solved.
        t     - list or Np array of t values to compute solution at.
                t[0] is the the initial condition point, and the difference
                h=t[i+1]-t[i] determines the step size h.

    OUTPUT:
        x     - Np array containing solution values corresponding to each
                entry in t array.  If a system is being solved, x will be
                an array of arrays.
    """

    # n = len( t )
    # x = np.array( [ x0 ] * n )
    # for i in xrange( n - 1 ):
    #     h = t[i+1] - t[i]
    #     k1 = h * f( x[i], t[i] )
    #     k2 = h * f( x[i] + 0.5 * k1, t[i] + 0.5 * h )
    #     k3 = h * f( x[i] + 0.5 * k2, t[i] + 0.5 * h )
    #     k4 = h * f( x[i] + k3, t[i+1] )
    #     x[i+1] = x[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
    # return x        
    x=[x0]
    for i,t_i in enumerate(t[:-1]):
        h = t[i+1] - t_i
        k1 = h*f(x[i],t_i)
        k2 = h*f(x[i]+0.5*k1,t_i+0.5*h)
        k3 = h*f(x[i]+0.5*k2,t_i+0.5*h)
        k4 = h*f(x[i]+k3,t_i+h)
        x.append(x[i]+1.0/6.0*(k1+2*k2+2*k3+k4))
    return np.array(x)



def pc4( f, x0, t ):
    """Adams-Bashforth-Moulton 4th order predictor-corrector method

    USAGE:
        x = pc4(f, x0, t)

    INPUT:
        f     - function of x and t equal to dx/dt.  x may be multivalued,
                in which case it should a list or a Np array.  In this
                case f must return a Np array with the same dimension
                as x.
        x0    - the initial condition(s).  Specifies the value of x when
                t = t[0].  Can be either a scalar or a list or Np array
                if a system of equations is being solved.
        t     - list or Np array of t values to compute solution at.
                t[0] is the the initial condition point, and the difference
                h=t[i+1]-t[i] determines the step size h.

    OUTPUT:
        x     - Np array containing solution values corresponding to each
                entry in t array.  If a system is being solved, x will be
                an array of arrays.

    NOTES:
        This function used the Adams-Bashforth-Moulton predictor-corrector
        method to solve the initial value problem

            dx
            -- = f(x,t),     x(t(1)) = x0
            dt

        at the t values stored in the t array (so the interval of solution is
        [t[0], t[N-1]].  The 4th-order Runge-Kutta method is used to generate
        the first three values of the solution.  Notice that it works equally
        well for scalar functions f(x,t) (in the case of a single 1st order
        ODE) or for vector functions f(x,t) (in the case of multiple 1st order
        ODEs).

    """

    n = len( t )
    x = np.array( [ x0 ] * n )

    # Start up with 4th order Runge-Kutta (single-step method).  The extra
    # code involving f0, f1, f2, and f3 helps us get ready for the multi-step
    # method to follow in order to minimize the number of function evaluations
    # needed.

    f1 = f2 = f3 = 0
    for i in xrange( min( 3, n - 1 ) ):
        h = t[i+1] - t[i]
        f0 = f( x[i], t[i] )
        k1 = h * f0
        k2 = h * f( x[i] + 0.5 * k1, t[i] + 0.5 * h )
        k3 = h * f( x[i] + 0.5 * k2, t[i] + 0.5 * h )
        k4 = h * f( x[i] + k3, t[i+1] )
        x[i+1] = x[i] + ( k1 + 2.0 * ( k2 + k3 ) + k4 ) / 6.0
        f1, f2, f3 = ( f0, f1, f2 )

    # Begin Adams-Bashforth-Moulton steps

    for i in xrange( 3, n - 1 ):
        h = t[i+1] - t[i]
        f0 = f( x[i], t[i] )
        w = x[i] + h * ( 55.0 * f0 - 59.0 * f1 + 37.0 * f2 - 9.0 * f3 ) / 24.0
        fw = f( w, t[i+1] )
        x[i+1] = x[i] + h * ( 9.0 * fw + 19.0 * f0 - 5.0 * f1 + f2 ) / 24.0
        f1, f2, f3 = ( f0, f1, f2 )

    return x

def rk45( f, x0, t ):
    """Fourth-order Runge-Kutta method with error estimate.

    USAGE:
        x, err = rk45(f, x0, t)

    INPUT:
        f     - function of x and t equal to dx/dt.  x may be multivalued,
                in which case it should a list or a Np array.  In this
                case f must return a Np array with the same dimension
                as x.
        x0    - the initial condition(s).  Specifies the value of x when
                t = t[0].  Can be either a scalar or a list or Np array
                if a system of equations is being solved.
        t     - list or Np array of t values to compute solution at.
                t[0] is the the initial condition point, and the difference
                h=t[i+1]-t[i] determines the step size h.

    OUTPUT:
        x     - Np array containing solution values corresponding to each
                entry in t array.  If a system is being solved, x will be
                an array of arrays.
        err   - Np array containing estimate of errors at each step.  If
                a system is being solved, err will be an array of arrays.

    NOTES:
        This version is based on the algorithm presented in "Numerical
        Mathematics and Computing" 6th Edition, by Cheney and Kincaid,
        Brooks-Cole, 2008.
    """

    # Coefficients used to compute the independent variable argument of f

    c20  =   2.500000000000000e-01  #  1/4
    c30  =   3.750000000000000e-01  #  3/8
    c40  =   9.230769230769231e-01  #  12/13
    c50  =   1.000000000000000e+00  #  1
    c60  =   5.000000000000000e-01  #  1/2

    # Coefficients used to compute the dependent variable argument of f

    c21 =   2.500000000000000e-01  #  1/4
    c31 =   9.375000000000000e-02  #  3/32
    c32 =   2.812500000000000e-01  #  9/32
    c41 =   8.793809740555303e-01  #  1932/2197
    c42 =  -3.277196176604461e+00  # -7200/2197
    c43 =   3.320892125625853e+00  #  7296/2197
    c51 =   2.032407407407407e+00  #  439/216
    c52 =  -8.000000000000000e+00  # -8
    c53 =   7.173489278752436e+00  #  3680/513
    c54 =  -2.058966861598441e-01  # -845/4104
    c61 =  -2.962962962962963e-01  # -8/27
    c62 =   2.000000000000000e+00  #  2
    c63 =  -1.381676413255361e+00  # -3544/2565
    c64 =   4.529727095516569e-01  #  1859/4104
    c65 =  -2.750000000000000e-01  # -11/40

    # Coefficients used to compute 4th order RK estimate

    a1  =   1.157407407407407e-01  #  25/216
    a2  =   0.000000000000000e-00  #  0
    a3  =   5.489278752436647e-01  #  1408/2565
    a4  =   5.353313840155945e-01  #  2197/4104
    a5  =  -2.000000000000000e-01  # -1/5

    b1  =   1.185185185185185e-01  #  16.0/135.0
    b2  =   0.000000000000000e-00  #  0
    b3  =   5.189863547758284e-01  #  6656.0/12825.0
    b4  =   5.061314903420167e-01  #  28561.0/56430.0
    b5  =  -1.800000000000000e-01  # -9.0/50.0
    b6  =   3.636363636363636e-02  #  2.0/55.0

    n = len( t )
    x = np.array( [ x0 ] * n )
    for i in xrange( n - 1 ):
        h = t[i+1] - t[i]
        k1 = h * f( x[i], t[i] )
        k2 = h * f( x[i] + c21 * k1, t[i] + c20 * h )
        k3 = h * f( x[i] + c31 * k1 + c32 * k2, t[i] + c30 * h )
        k4 = h * f( x[i] + c41 * k1 + c42 * k2 + c43 * k3, t[i] + c40 * h )
        k5 = h * f( x[i] + c51 * k1 + c52 * k2 + c53 * k3 + c54 * k4, \
                        t[i] + h )
        k6 = h * f( \
            x[i] + c61 * k1 + c62 * k2 + c63 * k3 + c64 * k4 + c65 * k5, \
            t[i] + c60 * h )

        x[i+1] = x[i] + a1 * k1 + a3 * k3 + a4 * k4 + a5 * k5
        x5 = x[i] + b1 * k1 + b3 * k3 + b4 * k4 + b5 * k5 + b6 * k6


    return x
