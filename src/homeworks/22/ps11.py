from numpy import*

def forward_difference_h2(f,x,h):
    """ Given a function f, return the derivative df at points x
        using the O(h**2) forward difference formula
    USAGE:
        df = forward_difference_h2(f,x,h)
    INPUT:
        f       - function to find derivative of
        x       - list of values x to find derivative at
        h       - step size
    OUTPUT:
        df      - list of f' at values x
    """
    return (-1*f(x+2*h)+4*f(x+h)-3*f(x))/float(2*h)
    
def backward_difference_h2(f,x,h):
    """ Given a function f, find the derivative df at x
        using the O(h**2) backward difference formula
    USAGE:
        df = backward_difference_h2(f,x,h)
    INPUT:
        f       - function to find derivative of
        x       - list of values x to find derivative at
        h       - step size
    OUTPUT:
        df      - list of f' at values x
    """
    return (3*f(x)-4*f(x-h)+f(x-2*h))/float(2*h)

def central_difference_h2(f,x,h):
    """ Given a function f, find the derivative df at x
        using the O(h**2) central difference formula
    USAGE:
        df = central_difference_h2(f,x,h)
    INPUT:
        f       - function to find derivative of
        x       - list of values x to find derivative at
        h       - step size
    OUTPUT:
        df      - list of f' at values x
    """
    return (f(x+h)-f(x-h))/float(2*h)

def richardson( f, x, n, h ):
    """Richardson's Extrapolation to approximate  f'(x) at a particular x.

    USAGE:
	d = richardson( f, x, n, h )

    INPUT:
	f	- function to find derivative of
	x	- value of x to find derivative at
	n	- number of levels of extrapolation
	h	- initial stepsize

    OUTPUT:
        numpy float array -  two-dimensional array of extrapolation values.
                             The [n,n] value of this array should be the
                             most accurate estimate of f'(x)
    """
    arr=zeros((n,n))
    for i in range(n):
       arr[i,0]=central_difference_h2(f,x,h/float(2**i))
       for j in range(1,i+1):
          arr[i,j]=arr[i,j-1]+(arr[i,j-1]-arr[i-1,j-1])/float(2**j-1)
    return arr

#def f(x):
 #  return sin(x)

#for i in range(20):
 #  x=i/float(10)
 #  print richardson(f,x,3,0.001)-cos(x)
