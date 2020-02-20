import matplotlib.pyplot as plt
import random as rd
import numpy as np

def dessin_l(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"black",lw=2)
    
def dessin_n(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"o")

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
        elif L[k].imag==L[x].imag:
            if L[k].real<L[x].real:
                x=k
    L2=[L[x]]
    while (L2[0]!=L2[-1] or (len(L2)<2)) and len(L)>0:
        if len(L2)==1:
            u=-np.pi
        else:
            u=arg(L2[-1]-L2[-2])
        x,u1=0,np.pi
        for k in range (len(L)):
            u2=arg(L[k]-L2[-1])
            if u2>=u and u2<=u1:
                x,u1=k,u2
        L2.append(L.pop(x))
    return L2
        
def expl (n,rmax,e,p):
    L=[]
    for k in range (n):
        r=rd.randint(0,rmax)/rd.randint(1,p)
        arg=2*np.pi*rd.randint(0,e-1)/e
        L.append(r*np.exp(arg*1j))
    return L

def etoile(L,a):