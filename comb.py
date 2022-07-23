#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  3 18:17:23 2020

@author: sk
"""
from itertools import combinations 

def kk(l):
    return [list(i) for k in range(len(l)+1) for i in combinations(l,k) ]

def denix(l,k):
    return [{li} for li in l] if k == 1 else [ r|{li}   for r in denix(l,k-1) for li in l if li not in r]

def caras(l):
    res = []
    [res.append(d) for d in denix(l,len(l)) if d not in res]
    return res
    
    
def ye(l,k,res):
    return [r for r in res if r not in res-r] if k==0  else []

def denixx(l,k,res):
    [ res.add(li) for li in l] if k == 1 else [ res.add(r|{li})   for r in denixx(l,k-1,res) for li in l if li not in r]  
    return [r for r in res if r not in res-{r}]

######################################################################
def damelemes(lists):
    res = []
    [res.append(elem)  for lis in lists for elem in lis if elem not in res]
    return res

def compis(elem,lists):
    res = []
    [res.append(elems) for lis in lists for elems in lis if elem in lis if elems not in res]
    return res

def reachh(elem,lists):
    res = compis(elem,lists)
    [res.append(elm)  for ell in res for elm in compis(ell,lists) for _ in range(len(lists)) if elm not in res]
    return res

def metodo(lists):
    res = []
    [res.append(set(reachh(elem,lists))) for elem in damelemes(lists) if set(reachh(elem,lists)) not in res]
    return len(res)
    
####################################################################

from numpy.random import random
import matplotlib.pyplot as plt




def pinta(points, sema):
    for p in sema:
        if len(p)==1:
            plt.plot([points[p[0]][0]], [points[p[0]][1]], marker='o', markersize=5, color="red")
        elif len(p)==2: #[1,2]
            x = [points[pi][0] for pi in p] 
            y = [points[pi][1] for pi in p] 
            plt.plot(x,y,color="b")
        elif len(p) == 3:
            x = [points[pi][0] for pi in p] 
            y = [points[pi][1] for pi in p] 
            plt.fill(x,y,alpha=1,color="g")
    return plt.show()