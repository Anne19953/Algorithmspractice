#!/usr/bin/env python
# coding:utf-8
"""
Name : 合并两个排序的链表
Author  : anne
Time    : 2019-09-23 14:03
Desc:
"""
class ListNode:
    def __init__(self,x):
        self.val = x
        self.next = None

#递归解法
class Solution1:
    def Merge1(self,pHead1,pHead2):
        if pHead1 is None:
            return pHead2
        elif pHead2 is None:
            return pHead1
        elif pHead1.val < pHead2.val:
            pHead1.next = self.Merge1(pHead1.next,pHead2)
            return pHead1

        else:
            pHead2.next = self.Merge1(pHead2.next,pHead1)
            return pHead2

#非递归
class Solution2:
    def Merge2(self,pHead1,pHead2):
        tmp = ListNode(0)
        pHead = tmp
        while(pHead1 and pHead2):
            if pHead1.val < pHead2.val:
                tmp.next = pHead1
                pHead1 = pHead1.next
            else:
                tmp.next = pHead2
                pHead2 = pHead2.next
            tmp = tmp.next
            if  pHead1:
                tmp.next = pHead1
            if  pHead2:
                tmp.next = pHead2
            return pHead.next

