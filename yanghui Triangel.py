# -*- coding: utf-8 -*-
"""
Created on Thu Mar  8 11:37:58 2018

@author: Administrator
"""

def triangel(n):
    L=[1]
    
    while True:
        yield L
        
        L = [L[x] + L[x+1] for x in range(len(L) - 1)]
        print(L)
        L.insert(0,1)
        L.append(1)
        if len(L) > n:
            break

a = triangel(10)
i = []
for i in a:
    print(i)