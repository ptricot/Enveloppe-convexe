import matplotlib.pyplot as plt
import numpy as np
import random as rd

def dessin_l(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"black",lw=2)
    
def dessin_b(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"bo")
    
def dessin_r(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"ro")
    
def dessin_m(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"mo")
    
def nuage (n,bx,by):
    L=[]
    for k in range (n):
        L.append(rd.randint(0,bx)+rd.randint(0,by)*1j)
    return L
    
def expl (n,rmax,c):
    L=[]
    for k in range (n):
        r=rmax*rd.random()/(1+c*rd.random())
        arg=2*np.pi*rd.random()
        L.append(r*np.exp(arg*1j))
    return L
   
def mod(z):
    return (z.real**2+z.imag**2)**0.5

def arg(z):
    d=mod(z)+z.real
    if d==0:
        return np.pi
    else:
        return 2*np.arctan(z.imag/d)
        
def not_in(L,z):
    ok=True
    for z1 in L:
        if z1==z:
            ok=False
    return ok

def env_conv(L):
    C=[]
    for a in L:
        for b in L:
            if a != b:
                ab=b-a
                okd,okg=True,True
                for c in L:
                    if c!=a:
                        ac=c-a
                        du=(arg(ac)-arg(ab))
                        if 0<du<np.pi or -2*np.pi<du<-np.pi:
                            okd=False
                        elif np.pi<du<2*np.pi or -np.pi<du<0:
                            okg=False
                if okg or okd:
                    if not_in(C,a):
                        C.append(a)
                    if not_in(C,b):
                        C.append(b)
    return C

def bar(C):
    return sum(C)/len(C)
    
def tri_env(C):
    b=bar(C)
    U=[]
    for z in C:
        U.append(arg(z-b))
    for k in range(len(C)):
        for l in range (len(C)-k-1):
            if U[l]<U[l+1]:
                U[l],U[l+1],C[l],C[l+1]=U[l+1],U[l],C[l+1],C[l]
    C.append(C[0])
    return C

def enveloppe(L):
    return tri_env(env_conv(L))

G=expl(30,1,1)
E=tri_env(env_conv(G))
dessin_b(G)
dessin_l(E)
plt.show()

import time

G=expl(100,1,1)
t1=time.clock()
E=enveloppe(G)
t2=time.clock()

print(t2-t1)
