import numpy as np
def rk4( f, x0, t ):
    x=x0
    sol=np.zeros(len(t))
    sol[0]=x
    for i in range(len(t)-1):
        K1=(t[i+1]-t[i])*f(t[i],x)
        K2=(t[i+1]-t[i])*f(t[i]+(t[i+1]-t[i])/2,x+K1/2)
        K3=(t[i+1]-t[i])*f(t[i]+(t[i+1]-t[i])/2,x+K2/2)
        K4=(t[i+1]-t[i])*f(t[i]+(t[i+1]-t[i]),x+K3)
        x+=(K1+2*K2+2*K3+K4)/6
        sol[i+1]=x
    return sol
