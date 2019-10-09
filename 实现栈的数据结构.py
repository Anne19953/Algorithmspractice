#!/usr/bin/env python
# coding:utf-8
"""
Name : 实现栈的数据结构
Author  : anne
Time    : 2019-09-27 20:54
Desc:
"""
"""
类中有top属性，用来指示栈的存储情况，初始值为1，
一旦插入一个元素，其值加1，利用top的值乐意判定栈是空还是满。
执行时先将0,1,2,3,4,5依次入栈，然后删除栈顶的前三个元素
"""

class Stack():
    def __init__(self,size):
        self.size=size
        self.stack=[]
        self.top=-1

    # 入栈之前检查栈是否已满
    def push(self,x):
        if self.isfull():
            print("stack is full")
        else:
            self.stack.append(x)
            self.top=self.top+1

    # 出栈之前检查栈是否为空
    def pop(self):
        if self.isempty():
            print("stack is empty")
        else:
            self.top=self.top-1
            self.stack.pop()

    def isfull(self):
        return self.top+1 == self.size
    def isempty(self):
        return self.top == '-1'
    def showStack(self):
        print(self.stack)

s=Stack(10)
# 此时的push是带参数的
for i in range(6):
    s.push(i)
s.showStack()

# 执行力三次POP
for i in range(3):
    s.pop()
s.showStack()