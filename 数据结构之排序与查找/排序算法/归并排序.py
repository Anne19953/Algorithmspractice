#!/usr/bin/env python
# coding:utf-8
"""
Name : 归并排序.py
Author  : anne
Time    : 2019-08-29 12:42
Desc:
"""


def merge_sort(alist):
    if len(alist) <= 1:
        return alist

    # 二分分解
    num = int(len(alist) / 2)
    # 两边分别调用分解
    left = merge_sort(alist[:num])
    right = merge_sort(alist[num:])
    # 合并
    return merge(left, right)


def merge(left, right):
    # 合并操作将两个有序数组left[]和right[]合并成一个有序的大数组
    # left和right的两个下标都是从0开始
    l, r = 0, 0
    result = []
    while l < len(left) and r < len(right):
        if left[l] < right[r]:
            result.append(left[l])
            l += 1
        else:
            result.append(right[r])
            r += 1
    # 如果比较到最后剩下的数都是left[]中的，那么直接加上left[]
    result += left[l:]
    # 如果比较到最后剩下的数都是right[]中的，那么直接加上right[]
    result += right[r:]
    return result


alist = [56, 99, 34, 10, 38, 7,3]

sort_alist = merge_sort(alist)

print(sort_alist)
