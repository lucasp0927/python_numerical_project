'''Module 0: Read in simulation parameters
'''
import numpy as np
import random 
def paraRead():
    with open('maxmin.dat') as fin:
        for line in fin:
            data=line.split()
            xmin=float(data[0])
            xmax=float(data[1])
    print 'xmin=',xmin,' xmax=', xmax
    try:
        with open('input.in') as fin:
            for line in fin:
                data=line.split()
                A=float(data[0])
                w=float(data[1])
                x0=float(data[2])
                v0=float(data[3])
#        with open('xin.in') as fin:
#            for line in fin:
#                data=line.split()    
#                x_in=float(data[0])
#            x_shift=[0.1,]
#            x_shift=[ i*0.05+0.05 for i in range(1,8)]
#            x_in=x0+random.choice(x_shift)
            x_in=x0+0.1+(xmax-xmin-0.1)*0.5*int(np.random.uniform()*10000)/10000.
            print 'x_int=%6.4f\n' % (x_in)
            c=6.
            l=(x_in-x0)*0.8
        with open('param.in') as fin:
            for line in fin:
                data=line.split()
                b=float(data[-1])    
        return A,w,b,x0,v0,x_in,l,c
    except TypeError:
        print 'Invalid filename!'
    except IOError:
        print 'File does not exists!!'
