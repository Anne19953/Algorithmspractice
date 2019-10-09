#!/usr/bin/env python
# coding:utf-8
"""
Name : 顺时针打印矩阵
Author  : anne
Time    : 2019-09-27 20:07
Desc:
"""
# 1  2  3  4
# 5  6  7  8
# 9  10 11 12
# 13 14 15 16
# def printMatrix(matrix):
#     res = []
#     while matrix:
#         res += matrix.pop(0)
#         if matrix and matrix[0]:
#             for row in matrix:
#                 res.append(row.pop())
#         if matrix:
#             res += matrix.pop()[::-1]
#         if matrix and matrix[0]:
#             for row in matrix[::-1]:
#                 res.append(row.pop(0))
#     return res

# matrix = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
# b = printMatrix(matrix)
# print(b)


#
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        result = []
        while(matrix):
            # result.append(matrix.pop(0))
            result += matrix.pop(0)
            if not matrix or not matrix[0]:
                break
            matrix = self.turn(matrix)
        return result
    def turn(self,matrix):
        num_r = len(matrix)
        num_c = len(matrix[0])
        newmat = []
        for i in range(num_c):
            newmat2 = []
            for j in range(num_r):
                newmat2.append(matrix[j][i])
            newmat.append(newmat2)
        newmat.reverse()
        return newmat
