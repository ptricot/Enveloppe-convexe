import matplotlib.pyplot as plt
import numpy as np
import random as rd

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
        

def nuage (n,bx,by):
    L=[]
    for k in range (n):
        L.append(rd.randint(0,bx)+rd.randint(0,by)*1j)
    return L

def expl (n,rmax,e,p):
    L=[]
    for k in range (n):
        r=rd.randint(0,rmax)/rd.randint(1,p)
        arg=2*np.pi*rd.randint(0,e-1)/e
        L.append(r*np.exp(arg*1j))
    return L

def circle (n,z,r):
    return[z+r*np.exp(2*np.pi*(k/n)*1j) for k in range (n)]

def patate (n,z,r,ratio,rota):
    L=[z+r*np.exp(2*np.pi*(k/n)*1j) for k in range (n)]
    for k in range (len(L)):
        L[k]=(L[k].real+ratio*L[k].imag*1j)*np.exp(2*np.pi*ratio*1j)
    return L

def ellipse (n,r,e):
    L=[]
    for k in range (n):
        teta=2*np.pi*(k/n)
        L.append(r/(1+e*np.cos(teta))*np.exp(teta*1j))
    return L
    
def expl_3d (n,rmax,c):
    Lx,Ly,Lz=[],[],[]
    for k in range (n):
        r=rmax*rd.random()/(1+c*rd.random())
        ang1=2*np.pi*rd.random()
        ang2=2*np.pi*rd.random()
        x,y,z=r*np.sin(ang2)*np.sin(ang1),r*np.sin(ang2)*np.cos(ang1),r*np.cos(ang2)
        Lx.append(x)
        Ly.append(y)
        Lz.append(z)
    return (Lx,Ly,Lz)

dessin_n(expl(100,1,10,3))
plt.show()