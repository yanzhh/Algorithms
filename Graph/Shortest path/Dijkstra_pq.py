# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 16:25:53 2018

@author: Arc
"""

from queue import PriorityQueue as pq

def dijkstra(graph, s):
    """graph: graph presentated by adjacent list. s: start point"""
    q = pq() #用来保存计算了到s路径长度的节点。
    q.put((0,s)) #最短路径从初始点s开始
    seen = set() #最短路径节点集合
    seen.add(s) #加入初始点
    parents = {s:None} #保存最短路径上节点的 predecessor
    distance = {} # 保存最短路径上节点到s的距离
    for node in graph:
        distance[node] = inf
    distance[s] = 0
    
    while len(seen) < len(graph):
        dist_u, u = q.get()
        seen.add(u)
        neighbors = graph[u]
        for node in neighbors:
            if node not in seen:
                dist_node = dist_u + graph[u][node]
                if dist_node < distance[node]:
                    q.put((dist_node,node))
                    distance[node] = dist_node
                    parents[node] = u
    return parents, distance

graph = {
        'a':{'b':10, 'c':3}, 
        'b':{'d':2, 'c':1}, 
        'c':{'b':4, 'd':8, 'e':2}, 
        'd':{'e':7}, 
        'e':{'d':9} 
        }
s = 'a' 


inf = float('infinity')

parents, distance = dijkstra(graph, s)
print(parents)
print(distance)