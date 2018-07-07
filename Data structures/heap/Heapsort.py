# -*- coding: utf-8 -*-
"""
Created on Fri Jul  6 23:30:12 2018

@author: Arc
"""

from Heap import heap

def heapsort(alist):
    h = heap()
    h.buildmaxheap(alist)
    for i in range(h.size, 1, -1):
        h.exchange(1, i)
        h.size -= 1
        h.maxheapify(1)
    return h.heaplist[1:]        
#
if __name__ == '__main__':
    import random
    alist = []
    for i in range(10):
        alist += [random.randint(1,30)]
    print('original list', alist)
    blist = heapsort(alist)
    print('sorted list', blist)