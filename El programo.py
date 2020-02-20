import numpy as np

def mod(z):
    return (z.real**2+z.imag**2)**0.5

def arg(z):
    d=mod(z)+z.real
    if d==0:
        return np.pi
    else:
        return 2*np.arctan(z.imag/d)
    
def env_conv(L):
    x=0
    for k in range (len(L)):
        if L[k].imag>L[x].imag:
            x=k
    L2=[L[x]]
    while (L2[0]!=L2[-1] or (len(L2)<2)):
        if len(L2)==1:
            u=-np.pi
        else:
            u=arg(L2[-1]-L2[-2])
        x,u1=0,np.pi
        for k in range (len(L)):
            u2=arg(L[k]-L2[-1])
            if u<=u2<=u1:
                x,u1=k,u2
        L2.append(L.pop(x))
    return L2