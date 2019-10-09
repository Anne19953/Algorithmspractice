#!/usr/bin/env python
# coding:utf-8
"""
Name : 树的子结构
Author  : anne
Time    : 2019-09-27 17:02
Desc:
"""
class Solution:
    def HasSubtree(self,pRoot1,pRoot2):
        result = False
        # 当tree1和tree2都不为0时，才进行比较，否则直接返回false
        if pRoot1 != None and pRoot2 !=None:
            # 如果找到了对应Tree2的根结点的点
            if pRoot1.val == pRoot2.val:
                # 以这个根节点为起点判断是否包含tree2
                result = self.DoseTree1haveTree2(pRoot1,pRoot2)
            #如果找不到，那么就再去以root的左儿子为起点，去判断是否包含Tree2
            if not result:
                result = self.DoseTree1haveTree2(pRoot1.left,pRoot2)
            #如果还找不到，就再以root的右儿子为起点，去判断是否包含tree2
            if not result:
                result = self.DoseTree1haveTree2(pRoot1.right,pRoot2)
        return result
    def DoseTree1haveTree2(self,pRoot1,pRoot2):
        # 如果tree2已经遍历完了都能对应上，返回true
        if pRoot2 == None:
            return True
        #  如果tree2还没有遍历完，tree1却遍历完了，返回false
        if pRoot1 == None:
            return False
        # 如果其中有一个点没对应上，返回false
        if pRoot1.val != pRoot2.val:
            return False
        #     如果根节点对应上，那么就分别去子节点里面匹配
        return self.DoseTree1haveTree2(pRoot1.left,pRoot2.left) and self.DoseTree1haveTree2(pRoot1.right,pRoot2.right)



