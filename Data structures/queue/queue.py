# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 10:41:22 2018

@author: Arc
"""

class queue(object):
    def __init__(self, maxlength): #maxlength即队列最大的元素个数
        self.q = []
        self.head = self.tail = 0 #初始时 q.head = q.tail = 1
        self.size = 0  # q.size变量记录了队列的实际长度
        self.length = maxlength
        
    def isEmpty(self):
        return self.__len__() == 0
    
    def enqueue(self, x):
        if self.__len__() == self.length:  #队列已满时
            assert self.__len__() != self.length, 'overflow!'
        elif len(self.q) < self.length:    #队列未满的第一种情况
            self.q.append(x)
            if self.tail == self.length -1:
                self.tail = 0
            else:
                self.tail += 1
            self.size += 1
        else:                                       #队列未满，但len(self.q) == self.length
            self.q[self.tail] = x #给self.tail指向位置赋值x
            if self.tail == self.length - 1: # self.tail指向了array最后的位置
                self.tail == 0
            else:
                self.tail += 1
            self.size += 1
        
    def dequeue(self): #将q.head向后移动一位，并返回被删除的x，但array中对应位置的值并不改变
        if self.__len__() == 0:
            assert self.__len__() != 0, 'underflow!';
        else:
            if self.head == len(self.q):
                self.head == 0
            else:
                self.head += 1
            self.size -= 1
            return self.q[self.head-1]
    
    def __len__(self):
        return self.size
    
    def __str__(self):
        if self.head < self.tail:
            return str(self.q[self.head:self.tail])
        elif self.head >= self.tail and self.__len__() != 0 :
            return str(self.q[self.head:]+ self.q[:self.tail])
        elif self.__len__() == 0:
            return str([])
   