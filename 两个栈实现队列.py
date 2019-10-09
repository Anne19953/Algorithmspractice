#!/usr/bin/env python
# coding:utf-8
"""
Name : 两个栈实现队列.py
Author  : anne
Time    : 2019-09-14 22:19
Desc:
"""
class Solution:
    def __init__(self):
        self.stackA = []
        self.stackB = []
    def push(self,node):
        self.stackA.append(node)
    def pop(self):
        if self.stackB:
            return self.stackB.pop()
        elif not self.stackA:
            return None
        else:
            while self.stackA:
                self.stackB.append(self.stackA.pop())
            return self.stackB.pop()



