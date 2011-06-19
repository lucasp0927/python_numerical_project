def dx_dt(data,ans):
    #import numpy as np
    f=open(data,'r')
    s=f.read()
    ori_data=s.split()
    #print ori_data
    x_t=[]
    v_t=[]
    t=[]
    x=[]
    #print len(ori_data)
    for n in range(0,len(ori_data),2):
        #print n
        #print ori_data[2*n]
        #print type(float(ori_data[2*n]))
        t.append(float(ori_data[n]))
    for c in range(1,len(ori_data),2):
        x.append(float(ori_data[c]))
        x_t=x[:-2]
    #print x
    for k in range(len(x)-2):
        #print k
        #print float(x[k+1])
        v=( -x[k+2] + 4*x[k+1] - 3*x[k] ) / (2*( t[k+1] - t[k] ))
        v_t.append(v)
        
    #print 'x_t=',x_t
    #print 't=',t
    #print 'v_t=',v_t

    filename = ans
    f = open(filename, 'w')
    for i in range(len(x_t)):
        f.write('%15.10f\t%15.10f\n' % (x_t[i], v_t[i]))

    f.close()

dx_dt('data1',"ans1")
dx_dt('data2',"ans2")
dx_dt('data3',"ans3")
dx_dt('data4',"ans4")
dx_dt('data5',"ans5")
dx_dt('data6',"ans6")
