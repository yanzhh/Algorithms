# -*- coding: utf-8 -*-
"""
Created on Thu Jul 26 15:22:32 2018

@author: Arc
"""
           
            
def DFS(graph, s):
    q = []  #python的list类似于stack，用 list.append 实现stack.push, list.pop 实现stack.pop
    q.append(s)
    seen = set()
    seen.add(s)
    result = []
    while len(q) > 0:
        u = q.pop()
        neighbors = graph[u]
        for node in neighbors:
            if node not in seen:
                q.append(node)
                seen.add(node)
        result.append(u)
    return result

graph = {
       's':['a','x'], 
       'a':['s','z'],'z':['a'], 
       'x':['s','d','c'], 
       'd':['f','c','x'], 
       'c':['x','d','f','v'], 
       'f':['d','c','v'], 
       'v':['c','f']
      }

result = DFS(graph, 's')

print(result)