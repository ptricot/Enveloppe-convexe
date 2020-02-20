import matplotlib.pyplot as plt
import numpy as np
import random as rd

def dessin_l(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"black",lw=2)
    
def dessin_b(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"bo")

def dessin_n(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"o")

def nuage (n,bx,by):
    L=[]
    for k in range (n):
        L.append(rd.randint(0,bx)+rd.randint(0,by)*1j)
    return L

def f(t):
    return np.cos(t)*np.cos(10*t)

def ech (f,a,b,n):
    return [ a+k*(1/(b-a))+f(a+k*(1/(b-a)))*1j for k in range (n+1)]

def expl (n,rmax,e,p):
    L=[]
    for k in range (n):
        r=rd.randint(0,rmax)/rd.randint(1,p)
        arg=2*np.pi*rd.randint(0,e-1)/e
        L.append(r*np.exp(arg*1j))
    return L

def circle (n,z,r):
    return[z+np.exp(2*np.pi*(k/n)*1j) for k in range (n)]
    
def patate (n,z,r,ratio,rota):
    L=[z+r*np.exp(2*np.pi*(k/n)*1j) for k in range (n)]
    for k in range (len(L)):
        L[k]=(L[k].real+ratio*L[k].imag*1j)*np.exp(2*np.pi*ratio*1j)
    return L
    
def mod(z):
    return (z.real**2+z.imag**2)**0.5

def arg(z):
    d=mod(z)+z.real
    if d==0:
        return np.pi
    else:
        return 2*np.arctan(z.imag/d)
        
def pas_appartient(L,z):
    ok=True
    for z1 in L:
        if z1==z:
            ok=False
    return ok
    
def env_list(L):
    Lso,Lno,Lse,Lne=[],[],[],[]
    for z in L:
        so,se,ne,no=True,True,True,True
        for z2 in L:
            if z2.real<z.real and z2.imag<z.imag:
                so=False
            if z2.real<z.real and z2.imag>z.imag:
                no=False
            if z2.real>z.real and z2.imag<z.imag:
                se=False
            if z2.real>z.real and z2.imag>z.imag:
                ne=False
        if so:
            Lso.append(z)
        elif se:
            Lse.append(z)
        elif ne:
            Lne.append(z)
        elif no:
            Lno.append(z)
    L2=[]
    L2.extend(Lso),L2.extend(Lse),L2.extend(Lne),L2.extend(Lno)
    return L2

def env_conv(L):
    C=[]
    for z1 in L:
        for z2 in L:
            if z1 != z2:
                u12 = (z2-z1)/mod(z2-z1)
                okd,okg=True,True
                for z in L:
                    if z!=z1:
                        u=(z-z1)/mod(z-z1)
                        du=(arg(u)-arg(u12))
                        if 0<du<np.pi or -2*np.pi<du<-np.pi:
                            okd=False
                        elif np.pi<du<2*np.pi or -np.pi<du<0:
                            okg=False
                if okg or okd:
                    if pas_appartient(C,z1):
                        C.append(z1)
                    if pas_appartient(C,z2):
                        C.append(z2)
    return C

def bar(C):
    s=C[0]-C[0]
    for k in C:
        s=s+k
    return s/len(C)
    
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
    
def toile (C):
    L=[]
    while len(C)>0:
        L.extend(