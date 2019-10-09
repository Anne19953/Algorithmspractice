#!/usr/bin/env python
# coding:utf-8
"""
Name : 斐波那契数列
Author  : anne
Time    : 2019-09-18 11:14
Desc:
"""
#
# def Fibonacci(n):
#     if n == 0:
#         return 0
#     if n == 1:
#         return 1
#     else:
#         return Fibonacci(n-1) + Fibonacci(n-2)
#
# a = Fibonacci(6)
# print(a)

"""
非递归解法
"""
class Solution():
    def Fibonacci(self,n):
        a = [0,1]
        if n < 2:
            return a[n]
        else:
            for i in range(2,n+1):
                a.append(a[i-1]+a[i-2])
            return a[n]
a = Solution()
print(a.Fibonacci(6))

