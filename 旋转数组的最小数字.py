#!/usr/bin/env python
# coding:utf-8
"""
Name : 旋转数组的最小数字
Author  : anne
Time    : 2019-09-18 09:29
Desc:
"""
#############################单纯找最小值,没意义
# class Solution:
#     def minNumberInRotateArray(self,rotateArray):
#         return min(rotateArray)
#
# a = Solution()
# list = [3,4,5,1,2]
# print(a.minNumberInRotateArray(list))

#########################使用二分查找
"""
1.array[mid] < array[high]
最小值为array[mid]或者在左边，因为是右边的数是递增的
high = mid 
2.array[mid] > array[high]
此时最小值在array[mid]右边
low = mid + 1
3.array[mid] = array[high]
如果数组为[1,0,1,1,1,1]或者[1,1,1,0,1]，不好判断,一个一个试
high = high -1

"""

class Solution():
    def minNumberInRotateArray(self, rotateArray):
        low = 0
        high = len(rotateArray)-1
        while(low<high):
            mid = (low + high)//2
            if(rotateArray[mid]>rotateArray[high]):
                low = mid + 1
            elif(rotateArray[mid]== rotateArray[high]):
                high = high-1
            else:
                high = mid

        return rotateArray[low]

a = Solution()
list = [3,4,5,1,2]
list2 = [1,0,1,1,1,1]
list3 = [1,1,1,0,1]
print(a.minNumberInRotateArray(list))
print(a.minNumberInRotateArray(list2))
print(a.minNumberInRotateArray(list3))