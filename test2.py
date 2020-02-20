import random as rd
import numpy as np
import matplotlib.pyplot as plt

def dessin_n(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"o")
    
def dessin_ln(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"black",lw=2)
    
def dessin_r(L):
    plt.plot([z.real for z in L],[z.imag for z in L],"ro")

def expl (n,rmax,c):
    L=[]
    for k in range (n):
        r=rmax*rd.random()/(1+c*rd.random())
        arg=2*np.pi*rd.random()
        L.append(r*np.exp(arg*1j))
    return L
