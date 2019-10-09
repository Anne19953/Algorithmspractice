#!/usr/bin/env python
# coding:utf-8
"""
Name : 走楼梯
Author  : anne
Time    : 2019-09-18 13:24
Desc:
"""
# class Solution:
#     def jumperFloor(self,number):
#         a = 1
#         b = 1
#         for i in range(number):
#             a,b = b,a+b
#         return a
#
# a = Solution()
# print(a.jumperFloor(1))
# print(a.jumperFloor(2))
# print(a.jumperFloor(3))
# print(a.jumperFloor(5))




class Solution:
    def jumpFloor(self, number):
        res = [0,1,2]
        if number <= 2:
            return number
        else:
            for i in range(3,number+1):
                res.append(res[-1]+res[-2])
            return res[number]
a = Solution()

print(a.jumpFloor(1))
print(a.jumpFloor(2))
print(a.jumpFloor(3))
print(a.jumpFloor(5))

