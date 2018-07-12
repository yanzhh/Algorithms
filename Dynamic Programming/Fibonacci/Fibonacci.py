# -*- coding: utf-8 -*-
"""
Created on Thu Jul 12 20:04:03 2018

@author: Arc
"""

def Fib(n):
    mem = {}
    if n == 1 or n == 2:
        mem[n] = 1
    elif mem.get(n,None) == None:
        mem[n] = Fib(n-1) + Fib(n-2)
    return mem[n], mem

n = 10
(f, mem) = Fib(n)
print('Fib(%d), %d'%(n,f))
print('mem', mem)