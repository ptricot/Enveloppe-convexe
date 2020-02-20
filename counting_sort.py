# -*- coding: utf-8 -*-
"""
Created on Thu Oct 18 08:42:01 2018

@author: Paul
"""

def Counting_sort(l):
    r=[0,0]    # Range of l's elements
    for i in l:
        if i<r[0]:
            r[0]=i
        elif i>r[1]:
            r[1]=i
    
    c=[0 for i in range (r[0],r[1]+1)]    # Number of occurence of every integer : c[i] is the occurences of i+offset
    offset=r[0]
    for i in l:
        c[i-offset]+=1
        
    s=[]           # Sorted list
    for i in range(len(c)):     # For every potential value in l ( value in the range r), value is i+offset
        for k in range (c[i]):     # Repeat k times where k is the number of occurences of i+offset
            s.append(i+offset)
    return s