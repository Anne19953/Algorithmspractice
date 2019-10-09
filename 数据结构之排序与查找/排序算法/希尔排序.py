#!/usr/bin/env python
# coding:utf-8
"""
Name : 希尔排序.py
Author  : anne
Time    : 2019-08-29 11:13
Desc:是插入排序的升级
"""
def shll_sort(alist):
    n = len(alist)
    #初始步长
    gap = int(n / 2)
    while gap > 0:
        # 按步长进行插入排序
        for i in range(gap,n):
            for j in (i,gap+1,-gap):
                if alist[j] < alist[j-gap]:
                    alist[j],alist[j-gap] = alist[j-gap],alist[j]


        #得到新步长：
        gap = int(gap / 2)


alist = [54,26,93,17,77,31,44,55,20]

shll_sort(alist)

print(alist)




