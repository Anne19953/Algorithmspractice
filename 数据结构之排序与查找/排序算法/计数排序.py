#!/usr/bin/env python
# coding:utf-8
"""
Name : 计数排序.py
Author  : anne
Time    : 2019-09-09 13:53
Desc:
"""
def countingSort(arr):  # the elements in the array are all integers
    maximum, minimum = max(arr), min(arr)
    countArr = [0] * (maximum - minimum + 1)  #用0初始化countArr
    for i in arr: # record the number of times of every element in the array
        countArr[i - minimum] += 1
    print('--------记录每个元素出现的次数',countArr)
    for i in range(1, len(countArr)): # calculate the position of every element
        countArr[i] += countArr[i-1]  #该元素的位置是这个元素前一个元素的位置+该元素的个数
    print('---------记录每个元素的位置',countArr)
    targetArr = [None] * len(arr)  #申请一个用来放排序结果的列表
    for i in range(len(arr)-1, -1, -1): # reverse-order traversal is for the stability
        countIndex = arr[i] - minimum # 原素主在新的列表中的对应位置
        targetArr[countArr[countIndex] - 1] = arr[i]
        countArr[countIndex] -= 1
    return targetArr

a = [-2,5,-3,0,-3,4,3,2,4]


print(countingSort(a))


