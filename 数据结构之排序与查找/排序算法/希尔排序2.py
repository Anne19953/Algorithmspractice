#!/usr/bin/env python
# coding:utf-8
"""
Name : 希尔排序2.py
Author  : anne
Time    : 2019-08-29 12:46
Desc:
"""

def shell_sort(alist):
    n = len(alist)

    # 初始步长

    gap = int(n / 2)

    while gap > 0:

        # 按步长进行插入排序

        for i in range(gap, n):

            j = i

            # 插入排序

            while j >= gap and alist[j - gap] > alist[j]:
                alist[j - gap], alist[j] = alist[j], alist[j - gap]

                j -= gap

        # 得到新的步长

        gap = int(gap / 2)


alist = [56,99,34,10,38,7 ,23,45,90,40 ]
shell_sort(alist)
print(alist)
