#!/usr/bin/env python
# coding:utf-8
"""
Name : 调整数组顺序
Author  : anne
Time    : 2019-09-20 09:48
Desc:
"""
"""
调整数组顺序，使得所有的奇数位于数组的前半部分，
所有的偶数位于数组的后半部分，并保证奇数和奇数，
偶数和偶数之间的相对位置不变。
"""
#############思路一  用两个列表一个里面放奇数，一个里面放偶数
# def reOrderArray( array):
#     a,b = [],[]
#     for i in range(len(array)):
#         if array[i] % 2 == 0:
#             b.append(array[i])
#         else:
#             a.append(array[i])
#     return a + b
# array = [1,34,5,7,18,35,24,56,33,7]
# c = reOrderArray(array)
# print(c)


###############思路二 冒泡,每次确保第一数放的位置是正确的
def reOrderArray(array):
    for j in range(len(array)-1,0,-1):
        for i in range(j):
            if(array[i]%2==0 and array[i+1]%2==1):
                array[i],array[i+1]= array[i+1],array[i]


array = [1,34,5,7,18,35,24,56,33,8]
reOrderArray(array)
print(array)

##################思路三 插入排序  从前向后遍历，碰到一个奇数后，
# 就从该数向前找，遇到偶数就交换位置

def reOrderArray1(array):
    for i in range(len(array)):
        if array[i] % 2 == 1:
            for j in range(i,0,-1):
                if array[j-1] % 2 == 0:
                    array[j],array[j-1] = array[j-1],array[j]




array = [1,34,5,7,18,35,24,56,33,8]
reOrderArray1(array)
print(array)

