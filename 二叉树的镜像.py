#!/usr/bin/env python
# coding:utf-8
"""
Name : 二叉树的镜像
Author  : anne
Time    : 2019-09-27 19:27
Desc:
"""
class Solution:
    def Mirror(self,root):
        if not root:
            return None
        else:
            #根结点左右交换
            root.left,root.right = root.right,root.left
            self.Mirror(root.left)#递归调用左节点
            self.Mirror(root.right)#递归调用右节点
            return root
