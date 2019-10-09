#!/usr/bin/env python
# coding:utf-8
"""
Name : 从头到尾打印链表
Author  : anne
Time    : 2019-09-12 22:57
Desc:
"""
#-----------------------递归法

class ListNode():
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution1:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        if listNode is None:
            return []
        return self.printListFromTailToHead(listNode.next) + [listNode.val]

head = ListNode(1)
head.next = ListNode(2)
b = head.next
b.next = ListNode(3)




a = Solution1()
b = a.printListFromTailToHead(listNode=head)
print(b)

#--------------法二 将链表转为list 再用切片
class Solution2:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead2(self, listNode):
        result = []
        if listNode is None:
            return result
        while listNode is not None:
            result.append(listNode.val)
            listNode = listNode.next
        return result[::-1]


head = ListNode(1)
head.next = ListNode(2)
b = head.next
b.next = ListNode(3)


a = Solution2()
b = a.printListFromTailToHead2(listNode=head)
print(b)







