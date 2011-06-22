'''Module 2, Differentiation Module
    Implments two functions df to carry out the first 
    derivatives of a list of data on equally spaced interval
'''
import numpy as np
def df(x,y):
    ''' Compute the first derivate of y(x) numerically, using the three-point
    central difference formula and assuming x is equally-spaced.
    USAGE:
    xout, out= df(x,y)
    INPUT 
        x: 1D numpy array of equally-spaced points
        y: 1D numpy array of function y(x_i)
    OUTPUT
        xout: 1D numpy array
            x points where the numerically derivative is valid
        out:  1D numpy array
            first derivative of y at points xout
    '''    
    #http://www.holoborodko.com/pavel/numerical-methods/numerical-derivative/central-differences/
    #from here 3N central differential formula is (f(x+h)-f(x-h))/2h
    h = x[1]-x[0]
    xout,out = [],[]
    l = len(x)
    for i,x_i in enumerate(x[1:-1]): #first and last point dont have difference
        #########
        #five point
        ########
        if (i==0 or i==l-3):
            xout.append(x_i)
            out.append((y[i+2]-y[i])/2*h)#since i start frmo 0,so i need to plus 1
        elif (i==1 or i==l-4):
            xout.append(x_i)
            out.append((y[i-1]-8*y[i]+8*y[i+2]-y[i+3])/12*h)
        else:
            xout.append(x_i)
            out.append((-1*y[i-2]+9*y[i-1]-45*y[i]+45*y[i+2]-9*y[i+3]+y[i+4])/60*h)
        ##########
        #Three point
        ##########
        # xout.append(x_i)
        # out.append((y[i+2]-y[i])/2*h)#since i start frmo 0,so i need to plus 1

    return (np.array(xout),np.array(out))


if __name__ == '__main__':
    x=[1,2,3,4,5]
    y=[10,20,30,40,50]
    xout,out = df(x,y)
    print xout
    print out
