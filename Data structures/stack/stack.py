# -*- coding: utf-8 -*-
"""
Created on Wed Jul  4 21:51:42 2018

@author: Arc
"""

class stack:
    def __init__(self, maxlength):
        self.item = []
        self.length = maxlength
        
    def __str__(self):
        return str(self.item)
    
    def push(self, x):
        if self.size() < self.length:
            self.item.append(x)
        else:
            assert self.size() < self.length, 'Overflow!'
    
    def pop(self):
        if len(self.item) == 0:
            assert len(self.item)!=0, 'underflow!'
        else:
            self.item.pop()
    
    def clear(self):
        self.item.clear() #or self.item.del[:]
    
    def empty(self):
        return len(self.item) == 0
    
    def size(self):
        return len(self.item)
    
    def top(self):
        return self[-1]
    
    

stk = stack()
stk.push(1)
print(stk.item)