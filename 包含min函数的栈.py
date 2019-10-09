#!/usr/bin/env python
# coding:utf-8
"""
Name : 包含min函数的栈
Author  : anne
Time    : 2019-09-27 20:40
Desc:定义栈的数据结构，
请在该类型中实现一个能够得到栈中所含最小元素的min函数（
时间复杂度应为O（1））。
"""


class Solution:
    def __init__(self):
        self.stack = []
        self.assist = []

    def push(self, node):
        min = self.min()
        if not min or node < min:
            self.assist.append(node)
        else:
            self.assist.append(min)
        self.stack.append(node)
    def pop(self):
        if self.stack:
            self.assist.pop()
            return self.stack.pop()
    def top(self):
        if self.stack:
            return self.stack[-1]
    def min(self):
        if self.assist:
            return self.assist[-1]
#