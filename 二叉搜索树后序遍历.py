#!/usr/bin/env python
# coding:utf-8
"""
Name : 二叉搜索树后序遍历
Author  : anne
Time    : 2019-10-09 15:21
Desc:二叉搜索树的特点是左子树要比根结点小，右子树要比根结点大
        后序遍历的特点是最后一个数是根结点
"""
class Solution:
    def VerifySquenceOfBST(self, sequence):
        if sequence == None or len(sequence) == 0:
            return False
        length = len(sequence)
        root = sequence[-1]
        # print(root)
        #二叉搜索树中左子树比根结点小
        for i in range(length):
            if sequence[i] > root:
                break
        #二叉搜索树中右子树比根结点小
        for j in range(i,length):
            if sequence[j] < root:
                return False
        #判断左子树是否为二叉树：
        left = True
        if i > 0:
            left = self.VerifySquenceOfBST(sequence[:i])

        # 判断右子树是否为二叉树：
        right = True
        if j < length-1:
            right = self.VerifySquenceOfBST(sequence[j:-1])
        return left and right




if __name__ == '__main__':
    a = [4,3,8,10,1,5]
    b = [1,4,8,13,16,15,10]
    s = Solution()
    print(s.VerifySquenceOfBST(a))
    print(s.VerifySquenceOfBST(b))





