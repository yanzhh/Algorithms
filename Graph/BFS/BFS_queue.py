# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 10:01:06 2018

@author: Arc
"""
from queue import Queue
def BFS_1(graph, s):
    q = Queue()
    parents = {s:None}
    i = 0
    level = {s:i}
    q.put(s)
    while not q.empty():
        u = q.get()
        neighbors = graph[u]
        i += 1
        for node in neighbors:
            if node not in level:
                q.put(node)
                parents[node] = u
                level[node] = i
        
    return parents, level

graph = {
       's':['a','x'], 
       'a':['s','z'],'z':['a'], 
       'x':['s','d','c'], 
       'd':['f','c','x'], 
       'c':['x','d','f','v'], 
       'f':['d','c','v'], 
       'v':['c','f']
      }


parents, level = BFS_1(graph, s)


def print_path(parents,s,v):
    """
    parent: dictionary store the parent nodes information
    s: start point
    v: object point
    """
    if v == s:
        print(s)
    elif parents[v] == None:
        print("No path from",s, "to",v,"exists")
    else: #print the shortest path from s to parent of v before print v.
        print_path(parents,s,parents[v])
        print(v)

s = 's'; v='v'
print('level of nodes are',level)
print('The shortest path from',s,'to',v,'is')
print_path(parents,'s','v')