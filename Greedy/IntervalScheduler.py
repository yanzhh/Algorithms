# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 14:04:40 2018

@author: Arc
"""



class job(object):
    def __init__(self, title, start, finish):
        """title: job title; start: start time; finish: finish time"""
        self.title = title
        self.start = start
        self.finish = finish

        
    def __repr__(self):
        return str((self.title, self.start, self.finish))
    
def ras(sortedjoblist, k, n):
    """start: list of start time; finish: list of finish time; k: start index; n: total size of activity set"""
    s = sortedjoblist
    m = k + 1
    while m <= n and s[m].start < s[k].finish:
        m += 1                      #结束时 m>n: 没有与活动k相容的活动，返回None; s[m] > f[k]:返回活动 k
    if m <= n:
        return [s[m]] + ras(sortedjoblist, m, n)
    else:
        return [None]
    
    
    
def solver(joblist):
    """sortedjoblist: joblist sorted by finish time"""
    joblist.append(job(0,0,0))
    sortedjoblist = joblist.copy()# job 0 是虚拟任务，结束时间为0
    sortedjoblist.sort(key = lambda x: x.finish)
#    start = [i.start for i in sortedjoblist]
#    finish = [i.finish for i in sortedjoblist]
    mcs = ras(sortedjoblist, 0, len(joblist)-1)
    if mcs[len(mcs)-1] == None:
        mcs.pop()
    return mcs

joblist = [job(7,6,10), job(4,4,7), job(1,1,4),job(6,5,9), job(2,3,5), job(5,3,8), job(3,0,6), job(8,8,11)]
print(solver(joblist))