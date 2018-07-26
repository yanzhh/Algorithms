# -*- coding: utf-8 -*-
"""
Created on Tue Jul 10 15:51:34 2018

@author: Arc
"""
import sys
sys.path.append('/Users/Arc/Documents/GitHub/Algorithms/Data structures/priority queue')
# from priorityqueue import minpriqueue as pq

from queue import PriorityQueue as pq

inf = float('inf')

class node(object):
    def __init__(self, name, source):
        self.name = name
        self.d = inf
        self.pi = None
        self.source = source
    
    def __lt__(n1,n2):
        return n1.d < n2.d


def weight(Adj, u, v):
    """u, v: node.name"""
    return Adj[u].get(v,inf) #return weight if weight of (u,v) exists, or else return infinite.
    
        
def initial(Adj, s):
    """G: the graph representation; s: the initial node; return a priority queue which store nodes and the key value of each nodes is the node.d attributes."""
    Q = pq()
    for i in Adj.keys():
        u = node(i, s)
        if u.name == s:
            u.d = 0
        Q.put((u.d,u)) #use Q to preserve the collection of nodes.
    return Q

def relax(Adj, u, v):
    """u,v: class node"""
    w = weight(Adj, u.name,v.name)
    if v.d > u.d + w:
        v.d = u.d + w
        v.pi = u
        
Adj = {'a':{'b':10, 'c':3}, 'b':{'d':2, 'c':1}, 'c':{'b':4, 'd':8, 'e':2}, 'd':{'e':7}, 'e':{'d':9} }
s = 'a' 

def Dijkstra(Adj, s): 
    Q = initial(Adj, s)
    S = []
    print('Q', Q.queue)
    print('S', S)
    while Q.qsize() > 0:
        u = Q.get() #return the node with the least distance to source node.
        S.append(u)
        print('Q', Q.queue)
        print('S', S)
        for v in Adj[u].keys():
            relax(Adj, u, v)
            
#Dijkstra(Adj, s)
#Q = initial(Adj, s)
Q = pq()
#for i in Adj.keys():
#    for j in Adj[i].keys():
#        
for i in Adj:
   u = node(i, s)
   if u.name == s:
       u.d = 0
   Q.put((u.d,u)) 
S = []
print('Q', Q.queue)
print('S', S)
while Q.qsize() > 0:
    u = Q.get() #return the node with the least distance to source node.
    S.append(u)
    print('Q', Q.queue)
    print('S', S)
    for v in Adj[u[1].name].keys():
        relax(Adj, u, v)         
