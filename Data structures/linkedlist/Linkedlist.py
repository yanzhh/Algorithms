# -*- coding: utf-8 -*-
"""
Created on Thu Jul  5 02:45:06 2018

@author: Arc
"""
#Define object node
class node(object):
    def __init__(self, data, nxt=None , prev = None):
        self.data = data
        self.next = nxt
        self.prev = prev
    
    def getdata(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def getPrev(self):
        return self.prev
    
    def setdata(self, data):
        self.data = data
        
    def setNext(self, nxt):
        self.next =nxt
        
    def setPrev(self, prev):
        self.prev = prev




#define linkedlist
class linklist(object):  #后面所有的x都是链表中的某个node对象
    def __init__(self):
        self.head = None  #如果链表中有元素，设第一个元素为node x, 则self.head = x 
    
    #是否为空
    def isEmpty(self):
        return self.head == None
    
    def search(self, data): #查找第一个dataue为data的元素，并返回指向它的指针(即那个node)
        x = self.head
        while x.getdata() != data and x != None:  #当x的dataue不等于data，且x不是None（还可以继续指向下一个元素）
            x = x.getNext()
        return x    
    
    def add(self, x):  #将 x 加入到链表的首位
        x.next = self.head #x.next指向链表原来的第一个元素（如果原本为空链表，则x.next = None)
        if self.head != None: #如果原链表第一个元素 y 不为空，则要设置y.prev = x
            self.head.prev = x
        self. head = x           #然后设置新的链表的第一个元素为x
        x.prev = None     #第一个元素的prev为None.
        
    def remove(self, x): #x.prev(如果不为None)要设置next = x.next（无论x.next 是否为None); x.next(如果不为空) 要设置 prev = x.prev
        prev = x.getPrev()
        nxt = x.getNext()
        if prev != None: #x不是第一个元素
            prev.next = x.next
        else:
            self.head = nxt
        if nxt != None:
            nxt.prev = prev
    
    def removedata(self, data):
        self.remove(self.search(data))