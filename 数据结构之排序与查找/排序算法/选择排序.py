#!/usr/bin/env python
# coding:utf-8
"""
Name : 选择排序.py
Author  : anne
Time    : 2019-08-28 20:10
Desc:
"""
def selection_sort(alist):
    n = len(alist)
    for i in range(n-1):
        #需要进行n-1次操作
        #记录最小位置
        min_index = i
        #从i+1位置到末尾选择最小数据
        for j in range(i+1,n):
            if alist[j] < alist[min_index]:
                min_index = j
        #如果此时的值不是在正确的位置
        if min_index != i:
            alist[i], alist[min_index] = alist[min_index], alist[i]


li = [56,99,34,10,38,7]
selection_sort(li)
print(li)

