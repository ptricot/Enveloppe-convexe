import matplotlib.pyplot as plt
import numpy as np
import random as rd

def dessin_l(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"black",lw=2)
    
def dessin_p(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"bo")

def tri(L,c):
    if c==1:
        for k in range (len(L)):
            for l in range (len(L)-k-1):
                if L[l].real>L[l+1].real:
                    L[l],L[l+1]=L[l+1],L[l]
                elif L[l].real==L[l+1].real:
                    if L[l].imag>L[l+1].imag:
                        L[l],L[l+1]=L[l+1],L[l]
    if c==2:
        for k in range (len(L)):
            for l in range (len(L)-k-1):
                if L[l].real>L[l+1].real:
                    L[l],L[l+1]=L[l+1],L[l]
                elif L[l].real==L[l+1].real:
                    if L[l].imag<L[l+1].imag:
                        L[l],L[l+1]=L[l+1],L[l]
    if c==3:
        for k in range (len(L)):
            for l in range (len(L)-k-1):
                if L[l].real<L[l+1].real:
                    L[l],L[l+1]=L[l+1],L[l]
                elif L[l].real==L[l+1].real:
                    if L[l].imag>L[l+1].imag:
                        L[l],L[l+1]=L[l+1],L[l]
    if c==4:
        for k in range (len(L)):
            for l in range (len(L)-k-1):
                if L[l].real<L[l+1].real:
                    L[l],L[l+1]=L[l+1],L[l]
                elif L[l].real==L[l+1].real:
                    if L[l].imag<L[l+1].imag:
                        L[l],L[l+1]=L[l+1],L[l]

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
    tri(Lso,2)
    tri(Lse,1)
    tri(Lne,3)
    tri(Lno,4)
    L2=[]
    L2.extend(Lso)
    L2.extend(Lse)
    L2.extend(Lne)
    L2.extend(Lno)
    L2.append(L2[0])
    return L2

def nuage (n,bx,by):
    L=[]
    for k in range (n):
        L.append(rd.randint(0,bx)+rd.randint(0,by)*1j)
    return L

N=nuage(20,10,10)
dessin_p(N)
dessin_l(env_list(N))

plt.show()