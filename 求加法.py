#!/usr/bin/env python
# coding:utf-8
"""
Name : 求加法
Author  : anne
Time    : 2019-10-08 21:05
Desc:求1+2+3+...+n，要求不能使用乘除法、
for、while、if、else、switch、case
等关键字及条件判断语句（A?B:C）
"""
class Solution:
    def __init__(self):
        self.sum = 0
    # def Sum_Solution(self,n):
        # def sum(n):
        #     self.sum += n
        #     n -= 1
        #     return n>0 and self.Sum_Solution(n)
        #
        # sum(n)
        # return self.sum

    def Sum_Solution2(self, n):
        return n and n+self.Sum_Solution2(n-1)



a = Solution()
b = a.Sum_Solution2(100)
print(b)