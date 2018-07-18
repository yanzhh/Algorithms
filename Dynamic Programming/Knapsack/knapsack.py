# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 22:33:29 2018

@author: Arc
"""

import numpy as np

#from bottom to top
def knapsack(p, S):
    m = len(p) + 1
    n = S + 1
    c = np.zeros((m,n))
    b = np.zeros((m,n))
    
    for i in range(1, m):
        for x in range(1,n):
            if p[i-1][0] > x:
                #b[i-1] = 0
                c[i][x] = c[i-1][x]
            else:
                if c[i-1][x] > c[i-1][x-p[i-1][0]] + p[i-1][1]:
                    c[i][x] = c[i-1][x]
                else:
                    b[i][x] = 1 
                    c[i][x] = c[i-1][x-p[i-1][0]] + p[i-1][1]
    return c, b
                    
    
p = [(1,1), (2, 6), (5, 18), (6, 22), (7, 28)] # p[i] = (s, v), s为item p[i] 的size, v为item p[i] 的value. 
S = 11
c, b = knapsack(p, S)
print('c=\n',c,'\n','b=\n',b)


# from top to bottom
inf = float('inf')
def knapsack_1(p, i, x):
    
    #mem = np.zeros((m,n))

    if mem[i][x] != inf:
        return mem[i][x]
    elif i == 0:
        mem[i][x] = 0
    elif p[i-1][0] > x:
        mem[i][x] = knapsack_1(p, i-1, x)
    else:
        mem[i][x] = max(knapsack_1(p, i-1, x), knapsack_1(p, i-1, x-p[i-1][0])+ p[i-1][1])
    return mem[i][x]
p = [(1,1), (2, 6), (5, 18), (6, 22), (7, 28)] # p[i] = (s, v), s为item p[i] 的size, v为item p[i] 的value.    
S = 11
m = len(p) + 1
n = S + 1
mem = np.asarray([[inf]*n]*m)
c = knapsack_1(p, len(p), S)
print('c=\n',c)