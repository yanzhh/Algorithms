# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 21:12:52 2018

@author: Arc
"""

class stack(object):
    def __init__(self):
        self.item = []
        #self.length = maxlength
        
    def __str__(self):
        return str(self.item)
    
    def push(self, x):
       # if self.size() < self.length:
       #     self.item.append(x)
       # else:
       #     assert self.size() < maxlength, 'Overflow!'
        self.item.append(x)
        
    def pop(self):
        if len(self.item) == 0:
            assert len(self.item)!=0, 'underflow!'
        else:
            return self.item.pop()
    
    def clear(self):
        self.item.clear() #or self.item.del[:]
    
    def isEmpty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)
    
    def top(self):
        return self[-1]
    
    
class queue(object):
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def enqueue(self, x):  #不考虑overflow
        self.s1.push(x)
    
    def dequeue(self):
        if self.s2.isEmpty():
            while self.s1.isEmpty() is False:
                self.s2.push(self.s1.pop())
            return self.s2.pop()
        else:
            return self.s2.pop()