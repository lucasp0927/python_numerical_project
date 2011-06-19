
#Problem 13
#Name: Chao Jung Lee --b97202070
#Collaborators: Cheng Kai Huang -- b97201047
#group 9
#Time: 2hr


## module polyFit




import numpy
import numpy as np
import math

def polyFit(xData,yData,m):


    def gaussElimin(a,b):
        A=a.copy()# This command is to prevent a be changed
        n=len(A) 
        A = np.float64(A)    
        x=np.zeros(n)
        x=np.float64(x)
        B=b.copy()
        B=np.float64(B)
        for k in range(0,n):
            for i in range(k+1,n):
                lamda=A[i][k]/A[k][k]
                A[i][k]=0
                for j in range(k+1,n):
                    A[i][j]=A[i][j]-lamda*A[k][j]
                B[i]=B[i]-lamda*B[k]


        x[n-1]=B[n-1]/A[n-1][n-1]
        for i in range(n-2,-1,-1):
            t=0   
            for j in range(i+1,n):
                t=t+A[i][j]*x[j]
            x[i]=(B[i]-t)/(A[i][i])
        return x

            
    
    
    

    def basis(x,j):
        return x**j

    

    A=np.zeros((m+1,m+1))
    A = np.float64(A)
    b=np.zeros(m+1)
    b=np.float64(b)
    n=len(x)-1 #since length of x is n+1
    
    for k in range(m+1):
        for j in range(m+1):
            for i in range(n+1):
                A[k][j]=A[k][j]+basis(x[i],j+k) # to this step ,I've constructed  the A matrix

        
    for k in range(m+1):
        for i in range(n+1):
            b[k]=b[k]+basis(x[i],k)*y[i]  # construct b vector



    c=gaussElimin(A,b)

    return(c)


    ''' 
    Returns coefficients of the polynomial
    p(x) = c[0] + c[1]x + c[2]x^2 +...+ c[m]x^m
    that fits the specified data in the least
    squares sense.

    USAGE:
        c = polyFit(xData,yData,m)
    INPUT:
        xData,yData : numpy arrays
            data to be fitted
        m : int
            degree of p(x)
    OUTPUT:
        c : numpy array
            coefficients of p(x)
    '''

def stdDev(c, xData, yData):


    def basis(x,j):
        return x**j

    S=0
    S=float(S)
    sigma=0
    sigma=float(sigma)


    def fit_func(c,x):
        sum=0
        sum=float(sum)
        
        for i in range(len(c)):
            sum=sum+c[i]*(x**i)
        return(sum) 

            
  
 
    for i in range(len(c)):
              
        S=S+(y[i]-fit_func(c,x[i]))**2
        
    sigma=math.sqrt(S/(len(x)-len(c)))

    return sigma



    
        
    
    '''
    Computes the std. deviation between p(x)
    and the data.
    USAGE:
        sigma = stdDev(c,xData,yData)
    INPUT:
        xData,yData : numpy arrays
            data to be fitted
        c : numpy array
            coefficients of p(x)
    OUTPUT:
        sigma: float
            std. deviation
        '''

#testing code

##x=np.zeros(6)
##x=np.float64(x)
##y=np.zeros(6)
##y=np.float64(y)
##
##x[0]=2
##x[1]=3
##x[2]=7
##x[3]=13
##x[4]=18
##x[5]=25
##y[0]=1
##y[1]=5
##y[2]=7
##y[3]=16
##y[4]=35
##y[5]=42
##
##print 'coefficients\n',polyFit(x,y,4)
##c=polyFit(x,y,4)
##print'\n'
##print 'standarf deviation\n',stdDev(c,x,y)




        
             

