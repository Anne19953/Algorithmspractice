#!/usr/bin/env python
# coding:utf-8
"""
Name : 基数排序.py
Author  : anne
Time    : 2019-09-09 17:03
Desc:
"""


# !/usr/bin/python
def RadixSort(input_list):
    def MaxBit(input_list):
        # 获得最大数的位数的值
        max_data = max(input_list)
        bits_num = 0
        while max_data:
            bits_num += 1
            max_data //= 10  #整除结果
        return bits_num

    def digit(num, d):
        # 取数num上的第d（从右往左第d位）位数字
        p = 1
        while d > 1:
            d -= 1
            p *= 10
        return num // p % 10

    if len(input_list) == 0:
        return []
    sorted_list = input_list
    length = len(sorted_list)
    bucket = [0] * length

    for d in range(1, MaxBit(sorted_list) + 1):
        count = [0] * 10

        for i in range(0, length):
            count[digit(sorted_list[i], d)] += 1
        # count[i]表示针对所有数的第d位数，小于等于i的数的个数是count[i]
        for i in range(1, 10):
            count[i] += count[i - 1]   #这里和计数排序很像
        # 针对所有数，按第d位数从小到大放入bucket里
        for i in range(0, length)[::-1]:
            k = digit(sorted_list[i], d)
            bucket[count[k] - 1] = sorted_list[i]
            count[k] -= 1
        for i in range(0, length):
            sorted_list[i] = bucket[i]
        print("%dth" % d)
        print(sorted_list)

    return sorted_list


if __name__ == '__main__':
    input_list = [3,67,983,234,56,32,358,4,1]
    print('input_list')
    print(input_list)
    sorted_list = RadixSort(input_list)
    print('sorted_list')
    print(sorted_list)



