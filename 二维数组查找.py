#!/usr/bin/env python
# coding:utf-8
"""
Name : 二维数组查找
Author  : anne
Time    : 2019-09-12 21:20
Desc:
"""
class Solution:
    def Find(self,target,arry):
        rows = len(arry) - 1
        cols = len(arry[0]) - 1
        i = rows
        j = 0
        while j <= cols and i >= 0:
            if target > arry[i][j]:
                j += 1
            elif target < arry[i][j]:
                i -= 1
            else:
                print("找到该数")
                return

        print('该数不存在')

arry = [[2,8,10,14],[3,9,11,15],[5,11,12,17],[9,14,16,18]]

a = Solution()
a.Find(11,arry)



