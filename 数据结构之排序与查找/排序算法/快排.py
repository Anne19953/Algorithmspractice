#!/usr/bin/env python
# coding:utf-8
"""
Name : 快排.py
Author  : anne
Time    : 2019-08-28 21:16
Desc:
"""
def quick_sort(alist,start,end):

    #递归退出条件
    if start >= end :
        return
    #设定起始划分元素
    mid = alist[start]

    #low为序列左边的由左向右移动的游标
    low = start
    #high为序列右边从由右向左移动的游标
    high = end
    while low < high:
        while low < high and alist[high] >= mid:
            high -= 1
        #将high指向的元素放到low的位置
        alist[low] = alist[high]
        # 如果low与high未重合，low指向的元素比基准元素小，则low向右移动
        while low < high and alist[low] <= mid:
            low += 1
        #将low指向的元素放到high的位置
        alist[high] = alist[low]

    #退出循环后，low和high重合，此时所指的位置为基准元素的正确位置
    #此时的low和high相等
    alist[low] = mid

    #对基准右边子序列进行快排
    quick_sort(alist,low+1,end)
    #对基准左边子序列进行快排
    quick_sort(alist,start,low-1)

alist = [56,99,34,10,38,7]

quick_sort(alist,0,len(alist)-1)

print(alist)