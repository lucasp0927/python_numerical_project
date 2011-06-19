from numpy import*

def gaussElimin(a,b):
    """Solves [a]{b} = {x} by Gauss elimination.
    USAGE:
        x = gaussElimin(a,b)
    INPUT:
        a       -numpy array (n*n)
        b       -numpy array (n*1)
    OUTPUT:
        x       -numpy array (n*1)
    """
    a=float64(a)
    b=float64(b)
    n=len(b)
    x=zeros((n,1),dtype=float)
    for k in range(n-1):
       for i in range(k+1,n):
          l=float(a[i][k])/a[k][k]
	  a[i][k]=0
	  for j in range(k+1,n):
	     a[i][j]=a[i][j]-l*a[k][j]
	  b[i]=b[i]-l*b[k]
    x[n-1]=float(b[n-1])/a[n-1][n-1]
    for i in range(n-2,-1,-1):
       sum=b[i]
       for j in range(i+1,n):
          sum=sum-a[i][j]*x[j]
       x[i]=float(sum)/a[i][i]
    return x    
    
    
def LUdecomp(a):
    """ LU decomposition: [L][U] = [a].
    USAGE:
        a = LUdecomp(a)
    INPUT
        a       -numpy array (n*n)
    OUTPUT
        a       -numpy array (n*n)
    The returned matrix [a]=[L\U] contains [U] in the upper triangle
    and the nondiagonal terms of [L] in the lower triangle.
    """
    a=float64(a)
    n=len(a)
    for k in range(n-1):
       for i in range(k+1,n):
          l=float(a[i][k])/a[k][k]
	  a[i][k]=l
	  for j in range(k+1,n):
	     a[i][j]=a[i][j]-l*a[k][j]
    return a 
    
def LUsolve(a,b):
    """Solves [L][U]{x} = b, where [a] = [L\U] is the matrix
    returned from LUdecomp.
    USAGE:
        x = LUsolve(a,b)
    INPUT:
        a       -numpy array (n*n)
        b       -numpy array (n*1)
    OUTPUT
        x       -numpy array (n*1)   
    """
    b=float64(b)
    n=len(b)
    LU=LUdecomp(a)
    y=zeros((n,1))
    x=zeros((n,1))
    y[0]=b[0]
    for i in range(1,n):
       sum=b[i]
       for j in range(i):
          sum=sum-LU[i][j]*y[j]
       y[i]=sum
    x[n-1]=float(y[n-1])/LU[n-1][n-1]
    for i in range(n-2,-1,-1):
       sum=y[i]
       for j in range(i+1,n):
          sum=sum-LU[i][j]*x[j]
       x[i]=float(sum)/LU[i][i]
    return x

