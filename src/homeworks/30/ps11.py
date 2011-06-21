#-*-coding:utf-8-*-
#Problem 11
#Name:Yu-Yi Kuo, Cheung Hei Ya
#Collaborators:
#Time:2:00



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
    
    return (-f(x+2*h)+4*f(x+h)-3*f(x))/(2*h)
    
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
    df=(f(x-2*h)-4*f(x-h)+3*f(x))/(2*h)
    return df

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
    df=(f(x+h)-f(x-h))/(2*h)
    return df

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
                             most accurate estimate of f'(x).
    """
    N=[[]]
    def N1(h):
        N1=(f(float(x+h))-f(float(x-h)))/(float(2*h))
        return N1
    for j in range(n):
        N[0].append(N1(float(h/2**j)))
        
    for i in range(1,n):
        N.append([])
        for j in range(n-i):
            N[i].append(N[i-1][j+1]+(N[i-1][j+1]-N[i-1][j])/(float(2**(i)-1)))
    A=[]
    for i in range(n):
        j=i
        while j>=0:
            A.append(N[i-j][j])
            j-=1
 
    return A

