#!/usr/bin/env python
# coding:utf-8
"""
Name : 替换空格
Author  : anne
Time    : 2019-09-12 22:01
Desc:
# """
# s = 'anne nn '
# class Solution1():
#     def replace(self,s):
#         m = ''
#         for i in s:
#             if i ==' ':
#                 i = '%20'
#             m = m+i
#         return m
# a = Solution1()
# b = a.replace(s)
# print(b)


#-------------------------------法二 对一的改进
# class Solution2(object):
#     def replace(self,s):
#         # if s is None or len(s):
#         #     return ''
#         l = ['%20' if x == ' ' else x for x in s]
#         return ''.join(l)
#
#
# s = 'love eat'
# a = Solution2()
# b = a.replace(s)
# print(b)


#--------------法三
class Solution():
    def replaceSpace(self,s):
        return s.replace(' ','%20')

s = 'delicious food '
a = Solution()
b = a.replaceSpace(s)
print(b)



