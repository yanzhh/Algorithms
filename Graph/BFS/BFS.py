# -*- coding: utf-8 -*-
"""
Created on Fri Jun 29 23:38:55 2018

@author: Arc
"""

#Define a graph by Adjacent list 
Adj = {'s':['a','x'], 'a':['s','z'],'z':['a'], 'x':['s','d','c'], 'd':['f','c','x'], 'c':['x','d','f','v'], 'f':['d','c','v'], 'v':['c','f']}

def BFS(Adj,s):
    """
    Adj: Adjacent list, represent a graph.
    s: start point, here we assume it is a string
    """
    level = {s:0}   #start point is in current level: level 0
    parent = {s:None}
    i = 1 # next level is i
    frontier = [s]  #points in previous level: level i-1
    while len(frontier)!= 0: #当上一个level不为空，则循环
        next = []   # points in next level
        for u in frontier:  #在上一个level的points中循环
            for v in Adj[u]:    #遍历u的所有neighbours.
                if v not in level.keys():    #如果v没有level，即没有被遍历过
                    next.append(v)  #则在next中加入v
                    level[v] = i    #v的level设置为i
                    parent[v] = u   #v的parent设置为u
        frontier = next
        print('level',i,'frontier = ',frontier)
        i += 1
    return level, parent              
    
    
level, parent = BFS(Adj,'s')