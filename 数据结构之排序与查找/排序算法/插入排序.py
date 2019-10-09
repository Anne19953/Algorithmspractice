#!/usr/bin/env python
# coding:utf-8
"""
Name : 插入排序.py
Author  : anne
Time    : 2019-08-28 20:40
Desc:
"""
def insert_sort(alist):
    #从第二个位置，下标为1的元素开始向前插入
    for i in range(1,len(alist)):
        #从第i个元素向前比较
        for j in range(i,0,-1):
            if alist[j] < alist[j-1]:
                alist[j],alist[j-1] = alist[j-1],alist[j]


li = [56,99,34,10,38,7]
insert_sort(li)
print(li)

