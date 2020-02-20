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

def mod(z):
    return (z.real**2+z.imag**2)**0.5

def arg(z):
    d=mod(z)+z.real
    if d==0:
        return np.pi
    else:
        return 2*np.arctan(z.imag/d)
        
def env_bary(L):
    n=len(L)
    bar=(1/n)*(sum(L))
    C=[]
    for k in range (n):
        C.append((L[k],arg(L[k]-bar)))
        
    def tri_arg (l) :
        def merge (l1,l2):
            l=[]
            while len(l1)>0 and len(l2)>0:
                if l1[0][1]<l2[0][1]:
                    l.append(l1.pop(0))
                else:
                    l.append(l2.pop(0))
            l.extend(l1)
            l.extend(l2)
            return l
        if len(l)==1:
            return l
        elif len(l)==2:
            if l[0][1]>l[1][1]:
                l[0],l[1]=l[1],l[0]
            return l
        else:
            l1,l2=l[:(len(l)//2)],l[(len(l)//2):]
            return merge(tri_arg(l1),tri_arg(l2))
            
    def clear (l):
        l2=[]
        for k in range (len(l)):
            l2.append(l[k][0])
        l2.append(l2[0])
        return l2
        
    def lower_last (l):
        i,min=0,0
        for k in range (len(l)):
            m=l[k].imag
            if m<min:
                i,min=k,m
        return ( l[(i+1):]+l[:(i+1)] )
        
    def left(a,b,c):
            ab,ac=arg(b-a),arg(c-a)
            if (0 <= ab-ac <= np.pi) or ( -2*np.pi <= ab-ac <= -np.pi):
                return True
            else:
                return False
                
    def prune (l):
        k=0
        while k<(len(l)-1):
            if left(l[k-1],l[k],l[k+1]):
                l.pop(k)
                if k>0:
                    k-=1
            else:
                k+=1
        return l
        
    def boucle(l):
        l.append(l[0])
        return l
        
    l=boucle(prune(lower_last(clear(tri_arg(C)))))
    return l,bar
    
G=expl(2000,1,0.1)
dessin_n(G)
E=env_bary(G)
dessin_r([E[1]])
dessin_ln(E[0])
plt.show()
