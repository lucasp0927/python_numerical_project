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
        
