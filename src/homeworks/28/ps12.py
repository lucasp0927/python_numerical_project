import numpy as np
def gaussElimin(a,b):
    a = 1.0*a
    b = 1.0*b
    x = np.zeros([len(b),1])
    for i in range(len(a)-1):
        for j in range(i + 1,len(a)):
            b[j] = b[j] - (a[j][i] / a[i][i])*b[i]
            a[j] = a[j] - (a[j][i] / a[i][i])*a[i]
            
    for i in range(len(a)-1,-1,-1):
        if i == len(a)-1:
            x[i][0] = b[i][0]/a[i][i]
        else:
            z = [a[i][j]*x[j][0] for j in range(len(a)-1,-1,-1)]
            x[i][0] = (b[i][0]-sum(z))/a[i][i]
    return x
