# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:24:43 2018

@author: Arc
"""

# Naive Algorithm, recursive
def sp_rec(Adj, s, v):
    if v == s:
        return 0
    else:
        d = []
        for node in neighbour(Adj,v):
            d.append(sp_rec(Adj,s,node)+Adj[node][v])
            print(node,'in neighbour(',v,')',neighbour(Adj,v))
            print('d',d)
        return min(d)
    
def neighbour(Adj,node):
    nblist = []
    for i in Adj:
        if node in Adj[i]:
#            print('Adj[i]=',Adj[i])
            nblist.append(i)
    return nblist

#Define a graph by Adjacent list 
Adj = {'s':{'t':6, 'y':7}, 't':{'y':8, 'x':5, 'z':-4}, 'y':{'x':-3, 'z':9}, 'x':{'t':-2}, 'z':{'s':2, 'x':7}}
s = 's'; v = 'z'
print('shortest path from', s, 'to', v, 'is', sp_rec(Adj,s,v))