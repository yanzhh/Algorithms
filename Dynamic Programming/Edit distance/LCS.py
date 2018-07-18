# -*- coding: utf-8 -*-
"""
Created on Tue Jul 17 16:27:04 2018

@author: Arc
"""

import numpy as np

def LCS(x, y):
    m = len(x)
    n = len(y)
    c = np.zeros((m+1,n+1))
    b = np.asarray([[None]*n]*m)
    for i in range(1,m+1):
        for j in range(1, n+1):
            if x[i-1] == y[j-1]:
                c[i][j] = c[i-1][j-1] + 1
                b[i-1][j-1] = 'nw'
            elif c[i-1][j] >= c[i][j-1]:
                c[i][j] = c[i-1][j]
                b[i-1][j-1] = 'u'
            else:
                c[i][j] = c[i][j-1]
                b[i-1][j-1] = 'l'
    return c, b


def print_LCS(b, x, m, n):
    """m,n: Lenght of X and Y"""
    if m == 0 or n == 0:
        return None
    elif b[m-1][n-1] == 'nw':
        print_LCS(b,x, m-1, n-1)
        print(x[m-1])
    elif b[m-1][n-1] == 'u':
        print_LCS(b, x, m-1, n)
    else: #b[m][n] == 'l'
        print_LCS(b, x, m, n-1)
        
x = ['A', 'B', 'C', 'B', 'D', 'A', 'B']
y = ['B', 'D', 'C', 'A', 'B', 'A']
m=len(x); n=len(y)
c, b = LCS(x, y)
print('c=',c)
print_LCS(b,x, m, n)