# -*- coding: utf-8 -*-
"""
Created on Wed Jul 25 04:30:57 2018

@author: Arc
"""

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right): # when both array left and right are not empty
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    if i == len(left): # array left is empty
        result += right[j:]
    else:
        result += left[i:]
    return result

def mergesort(L):
    if len(L) < 2:
        return L[:] #这里不能直接返回L，否则会改变实参L
    else:
        mid = len(L)//2
        left = mergesort(L[:mid])
        right = mergesort(L[mid:])
        return merge(left, right)