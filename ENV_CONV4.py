import matplotlib.pyplot as plt
import numpy as np
import random as rd

def dessin_ln(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"black",lw=2)
    
def dessin_lp(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"purple",lw=2)
    
def dessin_n(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"o")
    
def dessin_r(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"ro")
    
def expl (n,rmax,c):
    L=[]
    for k in range (n):
        r=rmax*rd.random()/(1+c*rd.random())
        arg=2*np.pi*rd.random()
        L.append(r*np.exp(arg*1j))
    return L
    
def nuage (n,bx,by):
    L=[]
    for k in range (n):
        L.append(rd.randint(0,bx)+rd.randint(0,by)*1j)
    return L
    
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
        L2.append(L[x])
    return L2
    
def diametre(L):
    x,y,d=L[0],L[1],mod(L[0]-L[1])
    for a in L:
        for b in L:
            if mod(a-b)>d:
                x,y,d=a,b,mod(a-b)
    return [x,y]
    
N=expl(1000,10,3 )
E=env_conv(N)
dessin_n(N)
dessin_lp(E)
plt.show()

