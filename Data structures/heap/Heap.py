# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 16:24:32 2018

@author: Arc
"""

class maxheap(object):
    def __init__(self):
        self.heaplist = [0]
        self.size = 0        
    
    def left(self, i):
        l = (i<<1)  #left/right index of node i's children
        if l <= self.size:
            return l
        else:
            return None
        
    def right(self, i):
        r = (i<<1) + 1 #left/right index of node i's children
        if r <= self.size:
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
        idx = self.size
        while self.heaplist[idx//2] < x:
            self.exchange(self, idx, idx//2)
            idx = idx // 2
            
            
    def maxheapify(self,i): #A[i], A[left[i]], A[right[i]]中最大的index记为j, 如果j!= i, 则，交换A[i]与A[j], 运行 maxheapify(self,j)
        assert i <= self.size, 'index is out of range'
        largest = i
        maxchild = self.maxchild(i)
        if maxchild != None and self.heaplist[maxchild] > self.heaplist[i]:
            largest = maxchild
        if largest != i:
            self.exchange(i,largest)
            self.maxheapify(largest)

    # define: buildmaxheap(A,array), produce a max heap from an unordered array.
    # do maxheapify on indexes of parents in [1, n//2]    
    def buildmaxheap(self, alist):
        self.heaplist += alist
        self.size += len(alist)
        i = self.size//2
        while i > 0:
            self.maxheapify(i)
            i -= 1
    

class minheap(object):
    def __init__(self):
        self.heaplist = [0]
        self.size = 0        
    
    def left(self, i):
        l = 2*i  #left/right index of node i's children
        if l <= self.size:
            return l
        else:
            return None
        
    def right(self, i):
        r = 2*i + 1 #left/right index of node i's children
        if r <= self.size:
            return r
        else:
            return None
        
    def exchange(self, i, j): #exchange A[i] and A[j]
        tmp = self.heaplist[i]
        self.heaplist[i] = self.heaplist[j]
        self.heaplist[j] = tmp
        
    def minchild(self, i):
        l = self.left(i); r = self.right(i)
        if l == None:    #这里包含了 r = None 的情况
            return  r
        elif r == None:
            return l
        elif self.heaplist[l] < self.heaplist[r]:
            return l
        else:
            return r
        
    #define insert method: 将新元素x放到heaplist最后，即成为heap的一个leaf, 然后比较x与其parent的值的大小，决定是否交换x与其parent，即提升x。递归这个过程。
    def insert(self,x):
        self.heaplist.append(x)
        self.size += 1
        idx = self.size
        while self.heaplist[idx//2] > x:
            self.exchange(self, idx, idx//2)
            idx = idx // 2
    
    def get_min(self):
        if self.size < 1:
            assert self.size >= 1, 'heap underflow'
        min = self.heaplist[1]
        self.heaplist[1] = self.heaplist[self.size] #交换根节点和最后一个节点，由于root的child节点没有改变，因此root的child子树仍然是最小堆。
        self.size -= 1
        self.minheapify(self,1)
        return min
        
        
    #define: minheapify(A,i), assume the tree rooted at left(i) and right(i) are min heaps, then minheapify(A,i) will exchange A[i] and one of its children if A[i] is smaller than it.
    def minheapify(self,i): #A[i], A[left[i]], A[right[i]]中最小的index记为j, 如果j!= i, 则，交换A[i]与A[j], 运行 minheapify(self,j)
        assert i <= self.size, 'index is out of range'
        least= i
        minchild = self.minchild(i)
        if minchild != None and self.heaplist[minchild] < self.heaplist[i]:
            least = minchild
        if least != i:
            self.exchange(i,least)
            self.minheapify(least)
            
    # define: buildminheap(A,array), produce a min heap from an unordered array.
    # do minheapify on indexes of parents in [1, n//2]    
    def buildminheap(self, alist):
        self.heaplist += alist
        self.size += len(alist)
        i = self.size//2
        while i > 0:
            self.minheapify(i)
            i -= 1
            
