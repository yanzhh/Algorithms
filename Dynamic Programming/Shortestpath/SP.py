# -*- coding: utf-8 -*-
"""
Created on Fri Jul 13 13:24:43 2018

@author: Arc
"""

inf = float('inf')

def neighbour(Adj,node):
    nblist = []
    for i in Adj:
        if node in Adj[i]:
            nblist.append(i)
    return nblist

# Naive Algorithm, recursive
def sp_rec(Adj, s, v):
    if v == s:
        return 0
    elif neighbour(Adj,v) == []:
        return inf
    else:
        d = []
        for node in neighbour(Adj,v):
            d.append(sp_rec(Adj,s,node)+Adj[node][v])
        return min(d)

# Naive algorithm which can return the shortest path
def sp_rec1(Adj, s, v, pre={}):
    """Adj: Adjacent list of a DAG; s: start point; v: target; pre: dictionary, store the predecessor of nodes on the shortest path from s to v"""
    if v == s:
        return 0, pre
    elif neighbour(Adj,v) == []:
        return inf, pre
    else:
        d = {}
        tmp = pre.copy()
        for node in neighbour(Adj,v):
            dist,pre1 = sp_rec1(Adj, s, node, tmp)
            dist = dist + Adj[node][v]
            d[dist] = (node, pre1)
        m = min(d)
        p = d[m]   
        pre = p[1]
        pre[v] = p[0]
        return m, pre


#Describe the graphs by Adjacent list 
# DAG in Ex.1
Adj1 = {'r':{'s':5, 't':3}, 's':{'t':2, 'x':6}, 't':{'x':7, 'y':4, 'z':2}, 'x':{'y':-1, 'z':1}, 'y':{'z':-2}, 'z':{}}
s = 's'; v = 'z'
length = sp_rec(Adj1,s,v)
if length == inf:
    print('No path from', s, 'to', v)
else:
    print('length of shortest path from', s, 'to', v, 'is', length)


length, prelist = sp_rec1(Adj1,s,v)
if length == inf:
    print('No path from', s, 'to', v)
else:
    sp = []
    target = v
    for i in prelist:
        prenode = prelist[target]
        sp.append(prenode)
        target = prenode
    sp.reverse()
    print('The shortest path is', sp )
    print('length of shortest path from', s, 'to', v, 'is', length)
    
################################################################################
    
# DP Algorithm, DAG
def sp_dp_DAG(Adj, s, v):
    mem = {}
    if v in mem:
        return mem[v]
    else:
        if v == s:
            mem[v] = 0
        elif neighbour(Adj,v) == []:
            mem[v] = inf
        else:
            d = []
            for node in neighbour(Adj,v):
                d.append(sp_dp_DAG(Adj,s,node)+Adj[node][v])
            mem[v] = min(d)
        return mem[v]
    

length = sp_rec(Adj1,s,v)
if length == inf:
    print('No path from', s, 'to', v)
else:
    print('length of shortest path from', s, 'to', v, 'is', length)    
    
##############################################################################

#DP algorithm, general case   
def sp_dp(Adj, k, s, v):
    if v == s:
        return 0
    elif k == 0 and v != s:
        return inf
    else:
        d = []
        for node in neighbour(Adj, v):
            d.append(sp_dp(Adj, k-1, s, v) + Adj[node][v])
        return min(d)
    
Adj2 = {'s':{'t':6, 'y':7}, 't':{'y':8, 'x':5, 'z':-4}, 'y':{'x':-3, 'z':9}, 'x':{'t':-2}, 'z':{'s':2, 'x':7}}
s = 's'; v = 't'
print('shortest path from', s, 'to', v, 'is', sp_dp(Adj2,len(Adj2)-1,s,v))    
    
    
    
    
    