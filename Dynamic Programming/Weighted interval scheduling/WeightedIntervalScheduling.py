# -*- coding: utf-8 -*-
"""
Created on Wed Jul 18 16:47:31 2018

@author: Arc
"""
import bisect

class wjob(object):
    def __init__(self, title, start, finish, weight):
        """title: job title; start: start time; finish: finish time"""
        self.title = title
        self.start = start
        self.finish = finish
        self.weight = weight
        
    def __repr__(self):
        return str((self.title, self.start, self.finish, self.weight))
    
def compatible(sortedjoblist):
    """sortedjoblist: joblist sorted by finish time"""
    start = [i.start for i in sortedjoblist]
    finish = [i.finish for i in sortedjoblist]
    
    p = []
    for i in range(len(sortedjoblist)):
        idx = bisect.bisect_right(finish, start[i])  # index of compatible job of job i(index i)
        if idx < 0 :
            p.append(0)
        else:
            p.append(idx)
    return p


def OPT(p, joblist, mem, i):
    """mem: memory list, i : find subset from job 1~i """
    if mem[i] != None:
        return mem[i]
    elif i == 0:
        mem[i] = 0
        return mem[i]
    else:
        job_i = joblist[i-1]
        if OPT(p, joblist, mem, i-1) >= (OPT(p, joblist, mem, i-1) + job_i.weight):
            mem[i] = OPT(p, joblist, mem, i-1)
        else:
            mem[i] = OPT(p, joblist, mem, i-1) + job_i.weight
        return mem[i]
    
def solve(joblist):   
    sortedjoblist = joblist.copy()
    sortedjoblist.sort(key = lambda x: x.finish)
    p = compatible(sortedjoblist)
    
    mem = [None]*(len(joblist)+1)
    return OPT(p, joblist, mem, len(joblist))

if __name__ == '__main__':
    joblist = [wjob(7,6,10,2), wjob(4,4,7,4), wjob(1,1,4,5),wjob(6,5,9,5), wjob(2,3,5,1), wjob(5,3,8,6), wjob(3,0,6,8), wjob(8,8,11,4)]
    print(solve(joblist))
    
    
    
    
    