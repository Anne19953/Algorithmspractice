#!/usr/bin/env python
# coding:utf-8
"""
Name : 反转链表
Author  : anne
Time    : 2019-09-20 12:45
Desc:
"""


class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution():
    # 返回ListNode
    def ReverseList(pHead):
        if pHead == None or pHead.next == None:
            return pHead
        pre = None
        cur = pHead
        while cur != 0:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre


L1 = ListNode(1)
L1.next = ListNode(2)
L1.next.next = ListNode(3)
L1.next.next.next = ListNode(4)
L2 = Solution
L2.ReverseList(L1)
print(L2.val,L2.next.val,L2.next.next.val,L2.next.next.next.val)