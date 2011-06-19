#!/usr/bin/python2
'''Module 1, I/O Module
   Implements a function dataRead
'''
import numpy as np
def dataRead(filename):
    ''' From File filename, read in three-column data and return as a tuple
        of three numpy arrays

        USAGE:
        tdata, xdata, vdata= dataRead(filename)

        INPUT:
        filename    - string, name of the data file

        OUTPUT
        tdata, xdata,vdata - a tuple of three 1D numpy arrays
                        tdata is an array of time data
                        xdata is an array of postition data
                        vdata is an array of velocity data

    '''
    tdata,xdata,vdata = [],[],[]
    filein = open(filename,'r')
    for aline in filein:
        tmp = str.split(aline)
        tdata.append(float(tmp[0]))
        xdata.append(float(tmp[1]))
        vdata.append(float(tmp[2]))                
    return (np.array(tdata),np.array(xdata),np.array(vdata))

if __name__ == '__main__':
    tdata,xdata,vdata = dataRead('sample1.dat')
    print tdata
    print xdata
    print vdata
