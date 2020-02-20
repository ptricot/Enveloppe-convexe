import matplotlib.pyplot as plt
import random as rd
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

def nuage(n,p):
    Lx=[float(rd.randint(0,p))/p for k in range (n)]
    Ly=[float(rd.randint(0,p))/p for k in range (n)]
    Lz=[float(rd.randint(0,p))/p for k in range (n)]
    return (Lx,Ly,Lz)
    
def tp(b,a):
    plt.plot([b[0],b[0]+a[0]],[b[1],b[1]+a[1]],[b[2],b[2]+a[2]],"purple",lw=2)

    
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

def dessin_b(G):
    Lx,Ly,Lz=G[0],G[1],G[2]
    plt.plot(Lx,Ly,Lz,"bo")
    
def dessin_T(E):
    for L in E:
        (a,b,c)=L
        (xa,ya,za)=a
        (xb,yb,zb)=b
        (xc,yc,zc)=c
        plt.plot([xa,xb,xc],[ya,yb,yc],[za,zb,zc],"ro")
        plt.plot([xa,xb,xc,xa],[ya,yb,yc,ya],[za,zb,zc,za],"black",lw=2)

def pv (v1,v2):
    (a,b,c)=v1
    (d,e,f)=v2
    return (b*f-e*c,c*d-a*f,a*e-d*b)
    
def ps (v1,v2):
    (a,b,c)=v1
    (d,e,f)=v2
    return(a*d+b*e+c*f)
    
def norme_carre(u):
    (a,b,c)=u
    return a**2+b**2+c**2

def normer(u):
    n=(u[0]**2+u[1]**2+u[2]**2)**0.5
    if n==0:
        return (0,0,0)
    else:
        return (u[0]/n,u[1]/n,u[2]/n)
    
def is_in (x,L):
    for k in L:
        if k==x:
            return True
    return False

def env(G):
    Lx,Ly,Lz,E,pile=G[0],G[1],G[2],[],[]
    def un (i,j):
        n=((Lx[i]-Lx[j])**2+(Ly[i]-Ly[j])**2+(Lz[i]-Lz[j])**2)**0.5
        return ((Lx[i]-Lx[j])/n,(Ly[i]-Ly[j])/n,(Lz[i]-Lz[j])/n)
    def non_col(i,j,k):
        ij,ik=un(j,i),un(k,i)
        if norme_carre(pv(ij,ik))>0.00000000001:
            return True
        else:
            return False
    def diff(a,b):
        return ((Lx[b],Ly[b],Lz[b]) != (Lx[a],Ly[a],Lz[a]))
    a=0
    for k in range (1,len(Lx)):
        if Lz[k]<Lz[a]:
            a=k
    pmin,u=1,(0,0,1)
    for k in range (len(Lx)):
        if diff(a,k):
            uk=un(k,a)
            p=ps(u,uk)
            if p<pmin:
                b=k
                pmin=p
    uab=un(a,b)
    up=(uab[0],uab[1],0)
    N=(uab[1],-uab[0],0)
    pmin,c=(ps(N,N)**0.5),0
    for k in range (len(Lx)):
        if diff(a,k) and diff(b,k) and non_col(a,b,k):
            uak=un(a,k)
            p1=ps(uak,uab)
            puak=normer((uak[0]-p1*uab[0],uak[1]-p1*uab[1],uak[2]-p1*uab[2]))
            p=ps(puak,N)
            if p<pmin:
                c=k
                pmin=p
    E.append((a,b,c))
    pile.append((a,b,c))  #Tout jusqu'ici sert à trouver le premier triangle abc de l'enveloppe
    while len(pile) != 0 :
        (a,b,c)=pile.pop()
        l=[(a,b,c),(b,c,a),(c,a,b)]
        for g in l:
            u,v,w=g[0],g[1],g[2]  #chercher les faces avec uv côté commun
            ok=True
            for t in E:
                if is_in(u,t) and is_in(v,t) and not(is_in(w,t)):
                    ok=False
            if ok:  # ok verifie qu'une face n'est pas déjà dans E
                M=((Lx[u]+Lx[v])/2,(Ly[u]+Ly[v])/2,(Lz[u]+Lz[v])/2)
                Mw=normer((M[0]-Lx[w],M[1]-Ly[w],M[2]-Lz[w]))
                n=normer((Lx[v]-Lx[u],Ly[v]-Ly[u],Lz[v]-Lz[u]))
                pmax,i=-1,0
                for k in range (len(Lx)):
                    if diff(u,k) and diff(v,k) and diff(w,k) and non_col(u,v,k):
                        Mk=normer((-M[0]+Lx[k],-M[1]+Ly[k],-M[2]+Lz[k]))
                        p=ps(Mk,n)
                        pMk=normer((Mk[0]-p*n[0],Mk[1]-p*n[1],Mk[2]-p*n[2]))
                        p2=ps(pMk,Mw)
                        if p2>pmax:
                            i,pmax=k,p2
                E.append((u,v,i))
                pile.append((u,v,i))
    E2=[]
    for k in E:
        (a,b,c)=k
        E2.append(((Lx[a],Ly[a],Lz[a]),(Lx[b],Ly[b],Lz[b]),(Lx[c],Ly[c],Lz[c])))
    return E2

import time

G=expl_3d(100,10,2)
dessin_b(G)
t1=time.clock()
E=env(G)
t2=time.clock()
dessin_T(E)
print(t2-t1)
plt.show()
            
        
        
    
            