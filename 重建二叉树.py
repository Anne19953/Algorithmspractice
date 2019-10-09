#!/usr/bin/env python
# coding:utf-8
"""
Name : 重建二叉树
Author  : anne
Time    : 2019-09-13 10:32
Desc:
"""
class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def reConstructBinaryTree(self, pre, tin):
        if not pre or not tin:
            return None
        root = TreeNode(pre.pop(0)) #pre将顶点弹出了
        index = tin.index(root.val)  #找到中序遍历中顶点的位置
        root.left = self.reConstructBinaryTree(pre,tin[:index])
        root.right = self.reConstructBinaryTree(pre,tin[index + 1:])
        return root


def printorder(node):
    if node is None:
        return

    printorder(node.left)
    printorder(node.right)
    print(node.val)




if __name__ == '__main__':
    solution = Solution()
    pre = [1, 2, 4, 7, 3, 5, 6, 8]
    tin = [4, 7, 2, 1, 5, 3, 8, 6]
    root = solution.reConstructBinaryTree(pre,tin)
    printorder(root)



