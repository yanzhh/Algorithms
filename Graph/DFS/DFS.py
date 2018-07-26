# -*- coding: utf-8 -*-
"""
Created on Sat Jun 30 02:22:29 2018

@author: Arc
"""

#Define a graph by Adjacent list 
Adj = {'a':['b','d'], 'b':['e'],'d':['b'], 'e':['d'], 'c':['e','f'], 'f':['f']}




def DFS_visit(Adj,parent,s):
    for v in Adj[s]:
        if v not in parent.keys():
            print('now at',v)
            parent[v] = s
            parent = DFS_visit(Adj,parent,v)
    return parent

def DFS(Adj):
    parent = {}
    for s in Adj:
        if s not in parent.keys():
            parent[s] = None                      #s没有被iterate过，那么s的parent为None
            parent = DFS_visit(Adj,parent,s)      #然后对s进行DFS
    return parent
    
parent = DFS(Adj)

