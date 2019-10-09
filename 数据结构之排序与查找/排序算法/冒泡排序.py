#!/usr/bin/env python
# coding:utf-8
"""
Name : 冒泡排序.py
Author  : anne
Time    : 2019-08-28 19:01
Desc:
"""
def bubble_sort(alist):
    for j in range(len(alist)-1,0,-1):
        #j表示每次遍历需要比较的次数是逐渐减少的
        for i in range(j):
            if alist[i] > alist[i+1]:
                alist[i],alist[i+1] = alist[i+1],alist[i]
li = [56,99,34,10,38,7]
bubble_sort(li)
print(li)