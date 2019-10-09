#!/usr/bin/env python
# coding:utf-8
"""
Name : 返回链表的倒数第k个节点
Author  : anne
Time    : 2019-09-20 12:23
Desc:
"""
class ListNOde:
    def __init__(self,x):
        self.val = x
        self.next = None
###############################法一
class Solution:
    def FindKthToTail(self, head, k):
        res = []
        while head:
            res.append((head))
            head = head.next
        if k<1 or k >len(res):
            return
        return res[-k]


##########################法二
    """
    设置两个指针，p1，p2，先让p2走k-1步，然后再一起走，
    直到p2为最后一个 时，p1即为倒数第k个节点
    """
    def FindKthToTail2(self, head, k):
        if head== None or k <=0:
            return None
        p2 = head
        p1 = head
        #p2先走，走k-1步
        while k > 1:
            if p2.next != None:
                p2 = p2.next
                k -= 1
            else:
                return None
        #两个指针一起走
        while p2.next != None:
            p1=p1.next
            p2=p2.next
        return p1





head = ListNOde(1)
a = head.next = ListNOde(3)
b = a.next = ListNOde(4)
c = b.next = ListNOde(5)

a = Solution()
b = a.FindKthToTail(head,2)
c = a.FindKthToTail2(head,2)
print(b.val)
print(c.val)

