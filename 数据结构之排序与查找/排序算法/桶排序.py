#!/usr/bin/env python
# coding:utf-8
"""
Name : 桶排序.py
Author  : anne
Time    : 2019-09-10 23:54
Desc:
"""





# def bucketSort(arr):
#     maximum, minimum = max(arr), min(arr)
#     bucketArr = [[] for i in range(maximum // 10 - minimum // 10 + 1)]  # set the map rule and apply for space
#     for i in arr:  # map every element in array to the corresponding bucket
#         index = i // 10 - minimum // 10
#         bucketArr[index].append(i)
#     arr.clear()
#     for i in bucketArr:
#         # arr.sort(i)  # sort the elements in every bucket
#         arr.extend(i)  # move the sorted elements in bucket to array


def bucket_sort(array):
    maxer, miner = max(array), min(array)
    gap = (maxer - miner) // len(array) + 1
    #桶的数量
    bucket_num =  (maxer - miner) // gap + 1
    print('桶的数量',bucket_num)
    # 注意这里要+1
    bucket_size = (maxer - miner + 1) / bucket_num
    print('桶的大小',bucket_size)
    bucket = [[] for _ in range(bucket_num)]   #初始化桶
    # print(bucket)
    #将数放入桶中
    for num in array:
        bucket[int((num - miner) / bucket_size)].append(num)
    print('将数按照映射关系放到桶中',bucket)
    result = []
    #对每个桶内的数调用排序，将拍好序的数组链接起来就能得到最后结果
    for i in range(len(bucket)):
        result += sorted(bucket[i])
        print('第 %i 个桶的排序结果 '%i,sorted(bucket[i]))
    print('最终结果：',result)

arr = [23,45,6,7,9,12,3,10]

bucket_sort(arr)