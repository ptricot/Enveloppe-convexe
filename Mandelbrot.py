import matplotlib.pyplot as plt
import numpy as np

n=10

def mod(z):
    return (z.real**2+z.imag**2)**0.5
    
def dist(a,b):
    return mod(a.real-b.real+(a.imag-b.imag)*1j)

def arg(z):
    d=mod(z)+z.real
    if d==0:
        return np.pi
    else:
        return 2*np.arctan(z.imag/d)
        
def dessin(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"go")
    plt.plot([2,2,-2,-2],[2,-2,2,-2],"bo")
    
def dessin_l(L):
    plt.plot([z.real for z in L],[z.imag for z in L],lw=2)
    plt.plot([2,2,-2,-2],[2,-2,2,-2],"bo")
    
def m(z1,z2):
    return z1.real*z2.real-z1.imag*z2.imag+(z1.real*z2.imag+z1.imag*z2.real)*1j

def mandel_cv(c):
    k=0
    z=0
    for k in range (n):
        z=m(z,z)+c
        if mod(z)>2:
            return False
    return True

def grille (k):
    L=[]
    for x in range (4*k):
        for y in range (4*k):
            c=x/k-2+(y/k-2)*1j
            if mandel_cv(c):
                L.append(c)
    return L

def emballage (e,nmax):
    ex=np.exp(np.pi/4*1j)
    def int():
        c=0
        for x in range (20):
            for y in range (20):
                c_prec=c
                c=x/10-2+(y/10-2)*1j
                if mandel_cv(c):
                    return(c_prec,c)
    a,b=int()
    while dist(a,b)>(e/2):
        c=(a+b)/2
        if mandel_cv(c):
            b=c
        else:
            a=c
    a,b,n=(a+b)/2,(a+b)/2,0
    L=[a]
    while (dist(L[0],b)>e or n<4) and n<nmax:
        n+=1
        c1,c2,k,ok=a+(b-a)*e,a,1,0
        while (not ok) and k<10:
            c2,c1=c1,a+(b-a)*e*(ex**k)
            k+=1   
            if ( not ( mandel_cv(c1) ) and mandel_cv(c2) ) or ( not ( mandel_cv(c2) ) and mandel_cv(c1) ):
                ok=1
        c=(c1+c2)/2
        L.append(c)
        a,b=c,a
    return L
    
G=emballage(0.01,10000)
dessin_l(G)
plt.show()