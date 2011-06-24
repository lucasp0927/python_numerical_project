'''Module 5: Solution Module
   Implement function firing
'''

import numpy as np

def firing(t,x,x0,l,c):
    ''' Using trajectory x=x(t), find the t0 such that x(t0)=x0
        USAGE
        t0=firing(t,x,x0)
        INPUT
            t,x: numpy arrays
                contain t and x data
            x0: float
                point of interception
            l : float
                distance from the motion of the particle
            c : float
                bullet velocity
        OUTPUT
            t0: float
                firing time
    '''

    for i,x_i in enumerate(x[:-1]):
        if (x_i-x0)*(x0-x[i+1]) >= 0:#find faster way. multiplying may be slow?
#            inter_t = t[i]
            j=i
            break
    else:
        # guess an answer if for loop doesn't find one
        j=int(np.random.rand()*len(x[:-1]))
    # x intercept between t[i] and t[i+1]
    # t is the time such that x(t0)=x0
    t=t[j]+(t[j+1]-t[j])/(x[j+1]-x[j])*(x0-x[j])
    #return the firing time
    return t-l/c
