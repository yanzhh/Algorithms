# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:24:32 2018

@author: Arc
"""

class heap(object):
    def __init__(self):
        self.heaplist = [0]
        self.size = 0        
    
    def left(self, i):
        l = (i<<1)  #left/right index of node i's children
        if l <= len(self.heaplist) -1:
            return l
        else:
            return None
        
    def right(self, i):
        r = (i<<1) + 1 #left/right index of node i's children
        if r <= len(self.heaplist) -1:
            return r
        else:
            return None
        
    def maxchild(self, i):
        l = self.left(i); r = self.right(i)
        if l == None:    #这里包含了 r = None 的情况
            return  r
        elif r == None:
            return l
        elif self.heaplist[l] > self.heaplist[r]:
            return l
        else:
            return r
        
    def exchange(self, i, j): #exchange A[i] and A[j]
        tmp = self.heaplist[i]
        self.heaplist[i] = self.heaplist[j]
        self.heaplist[j] = tmp
        
    def insert(self,x):
        self.heaplist.append(x)
        self.size += 1
        idx = len(self.heaplist)-1
        while self.heaplist[idx//2] < x:
            self.exchange(self, idx, idx//2)
            idx = idx // 2
            
#    def maxheapify(self,i): #A[i], A[left[i]], A[right[i]]中最大的index记为j, 如果j!= i, 则，交换A[i]与A[j], 运行 maxheapify(self,j)
#        assert i <= len(self.heaplist)-1, 'index is out of range'
#        l = self.left(i); r = self.right(i)
#        largest = i
#        if l!= None and self.heaplist[l] > self.heaplist[largest]:
#            largest = l
#        if r!= None and self.heaplist[r] > self.heaplist[largest]:
#            largest = r
#        if largest != i:
#            self.exchange(i,largest)
#            self.maxheapify(largest)
            
    def maxheapify(self,i): #A[i], A[left[i]], A[right[i]]中最大的index记为j, 如果j!= i, 则，交换A[i]与A[j], 运行 maxheapify(self,j)
        assert i <= len(self.heaplist)-1, 'index is out of range'
        largest = i
        maxchild = self.maxchild(i)
        if maxchild != None and self.heaplist[maxchild] > self.heaplist[i]:
            largest = maxchild
        print('largest', largest)
        if largest != i:
            self.exchange(i,largest)
            self.maxheapify(largest)
            print('maxheapify', largest)

            