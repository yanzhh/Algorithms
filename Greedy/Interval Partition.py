# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 19:55:08 2018

@author: Arc
"""

class classroom(object):
    def __init__(self, title, finish):
        self.title = title
        self.finish = finish
    
    def __repr__(self):
        return str((self.title,self.finish))
    

class job(object):
    def __init__(self, title, start, finish):
        """title: job title; start: start time; finish: finish time"""
        self.title = title
        self.start = start
        self.finish = finish

        
    def __repr__(self):
        return str((self.title, self.start, self.finish))
    
def solver(joblist):
    """sortedjoblist: joblist sorted by finish time"""
#    joblist.append(job(0,0,0))
    sortedjoblist = joblist.copy()# job 0 是虚拟任务，结束时间为0
    sortedjoblist.sort(key = lambda x: x.start)