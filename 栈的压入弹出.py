#!/usr/bin/env python
# coding:utf-8
"""
Name : 栈的压入弹出
Author  : anne
Time    : 2019-10-09 11:09
Desc:
"""
class Soluton:
    def IsPopOrder(self,pushV,popV):
        stack = []
        for push in pushV:
            stack.append(push)
            if stack[-1] == popV[0]:
                popV.pop(0)
                stack.pop()
        for pp in popV:
            if pp == stack[-1]:
                # popV.pop(0)
                stack.pop()
        return stack == []
    # def IsPopOrder(self, pushV, popV):
    #     stack = []
    #     for pushv1 in pushV:
    #         stack.append(pushv1)
    #         while len(stack) and stack[-1] == popV[0]:
    #             stack.pop()
    #             popV.pop(0)
    #     if len(stack):
    #         return False
    #     else:
    #         return True


pushv1 = [1,2,3,4,5]
popv1 = [4,5,3,2,1]
popv2 = [4,3,5,1,2]
A = Soluton()
print(A.IsPopOrder(pushv1,popv1))
print(A.IsPopOrder(pushv1,popv2))


