# -*- coding: utf-8 -*-
"""
Created on Mon Jul 16 16:19:09 2018

@author: Arc
"""

import numpy as np

inf = float('inf')
def MCOP(p):
    n = len(p) - 1
    m = np.asarray([[inf]*n]*n)
    s = np.asarray([[inf]*n]*n)
    
    for i in range(n):  # case: j=i
        m[i][i] = 0 
    for l in range(2, n+1): # case: j!= i; then length l>=2
        for i in range(n-l+1): #要保证矩阵链的长度为l，则对应的i可以的取值范围为 0~n-l
            j = i + l -1 # [i,j]长度为l，则j = i+l-1
            for k in range(i, j):
                q = m[i][k] + m[k+1][j] + p[i]*p[k+1]*p[j+1]
                if q < m[i][j]:
                    m[i][j] = q
                    s[i][j] = k
    return m,s

p = [30,35,15,5,10,20,25]

m, s = MCOP(p)
print('m =', m, '\n','s =\n', s)


inf = float('inf')
def Memorized_MC(p):
    n = len(p) - 1
    m = [[inf]*n]*n
    s = [[inf]*n]*n
    return lookup_chain(m,p,0,n-1, s)

def lookup_chain(m,p,i,j,s):
    if m[i][j] < inf:
        return m[i][j], s
    if i == j:
        m[i][j] = 0
    else:
        for k in range(i,j):
            q = lookup_chain(m,p,i,k,s)[0] + lookup_chain(m,p,k+1,j,s)[0] + p[i]*p[k+1]*p[j+1]
            s1 = k
            if q < m[i][j]:
                m[i][j] = q
                s[i][j] = s1
    return m[i][j], s

p = [30,35,15,5,10,20,25]

m, s = Memorized_MC(p)
print('m =', m, '\n','s =\n', s)