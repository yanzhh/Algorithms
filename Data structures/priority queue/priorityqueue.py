# -*- coding: utf-8 -*-
"""
Created on Sat Jul  7 00:35:17 2018

@author: Arc
"""

import sys
sys.path.append('/Users/Arc/Documents/GitHub/Algorithms/Data structures/heap')
from Heap import maxheap

class maxpriqueue(object):
    def __init__(self, item=[]):
        self.queue = maxheap()
        self.queue.buildmaxheap(item)
            
    def put(self, priority, item):
        self.queue.insert((priority, item))    
            
    def get(self):
        self.queue.get_max()

from Heap import minheap

class minpriqueue(object):
    def __init__(self, item=[]):
        self.queue = minheap()
        self.queue.buildminheap(item)
            
    def put(self, priority, item):
        self.queue.insert((priority, item))    
            
    def get(self):
        self.queue.get_min()