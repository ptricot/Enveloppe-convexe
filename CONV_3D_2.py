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
    
def expl_3d (n,rmax,e,p):
    Lx,Ly,Lz=[],[],[]
    for k in range (n):
        r=rd.randint(0,rmax)/rd.randint(1,p)
        ang1=2*np.pi*rd.randint(0,e-1)/e
        ang2=2*np.pi*rd.randint(0,e-1)/e
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
    
def dessin_r(G):
    Lx,Ly,Lz=G[0],G[1],G[2]
    plt.plot(Lx,Ly,Lz,"ro")

def pv (v1,v2):
    (a,b,c)=v1
    (d,e,f)=v2
    return (b*f-e*c,c*d-a*f,a*e-d*b)
    
def ps (v1,v2):
    (a,b,c)=v1
    (d,e,f)=v2
    return(a*d+b*e+c*f)

def tri_prel(G):
    Lx,Ly,Lz=G[0],G[1],G[2]
    Ex,Ey,Ez=[],[],[]
    for a in range (len(Lx)):
        ok1,ok2,ok3,ok4,ok5,ok6,ok7,ok8=True,True,True,True,True,True,True,True
        for b in range (len(Lx)):
            if Lx[a]<Lx[b] and Ly[a]<Ly[b] and Lz[a]<Lz[b]:
                ok1=False
            if Lx[a]<Lx[b] and Ly[a]<Ly[b] and Lz[a]>Lz[b]:
                ok2=False
            if Lx[a]<Lx[b] and Ly[a]>Ly[b] and Lz[a]<Lz[b]:
                ok3=False
            if Lx[a]<Lx[b] and Ly[a]>Ly[b] and Lz[a]>Lz[b]:
                ok4=False
            if Lx[a]>Lx[b] and Ly[a]<Ly[b] and Lz[a]<Lz[b]:
                ok5=False
            if Lx[a]>Lx[b] and Ly[a]<Ly[b] and Lz[a]>Lz[b]:
                ok6=False
            if Lx[a]>Lx[b] and Ly[a]>Ly[b] and Lz[a]<Lz[b]:
                ok7=False
            if Lx[a]>Lx[b] and Ly[a]>Ly[b] and Lz[a]>Lz[b]:
                ok8=False
        if ok1 or ok2 or ok3 or ok4 or ok5 or ok6 or ok7 or ok8:
            Ex.append(Lx[a])
            Ey.append(Ly[a])
            Ez.append(Lz[a])
    return (Ex,Ey,Ez)

def env2 (G):
    Lx,Ly,Lz=G[0],G[1],G[2]
    E=[]
    for a in range (len(Lx)):
        for b in range (len(Lx)):
            if b != a:
                for c in range (len(Lx)):
                    if c != a and c != b:
                        oka,okb=True,True
                        u1=(Lx[a]-Lx[b],Ly[a]-Ly[b],Lz[a]-Lz[b])
                        u2=(Lx[a]-Lx[c],Ly[a]-Ly[c],Lz[a]-Lz[c])
                        n=pv(u1,u2)
                        for d in range (len(Lx)):
                            if d != a and d != b and d != c:
                                u3=(Lx[a]-Lx[d],Ly[a]-Ly[d],Lz[a]-Lz[d])
                                if ps(n,u3)<0:
                                    oka=False
                                elif ps(n,u3)>0:
                                    okb=False
                        if (oka or okb) and n != (0,0,0):
                            E.append([(Lx[a],Ly[a],Lz[a]),(Lx[b],Ly[b],Lz[b]),(Lx[c],Ly[c],Lz[c])])
    return E
    
G=expl_3d(50,10,20,2)
dessin_b(G)
dessin_T(env2(tri_prel(G)))

plt.show()