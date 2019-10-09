#!/usr/bin/env python
# coding:utf-8
"""
Name : 堆排序.py
Author  : anne
Time    : 2019-08-29 17:19
Desc:
"""

def sift_down(arr, node, end):
    root = node

    while True:
        # 从root开始对最大堆调整

        child = 2 * root + 1  # left child
        if child > end:

            break
        print("v:", root, arr[root], child, arr[child])
        print(arr)
        # 找出两个child中交大的一个
        if child + 1 <= end and arr[child] < arr[child + 1]:  # 如果左边小于右边
            child += 1  # 设置右边为大

        if arr[root] < arr[child]:
            # 最大堆小于较大的child, 交换顺序
            arr[root],arr[child] = arr[child],arr[root]
            # 正在调整的节点设置为root
            root = child  #
        else:
            # 无需调整的时候, 退出
            break

    print('-------------')


def heap_sort(arr):
    # 从最后一个有子节点的孩子开始调整最大堆
    first = len(arr)
    for i in range(first, -1, -1):
        sift_down(arr, i, len(arr) - 1)

    print('--------end---', arr)
    # 将最大的放到堆的最后一个, 堆-1, 继续调整排序
    for end in range(len(arr) - 1, 0, -1):
        arr[0], arr[end] = arr[end], arr[0]
        sift_down(arr, 0, end - 1)


def main():

    array = [56, 99,34, 10, 38, 7]
    print(array)
    heap_sort(array)
    print(array)



if __name__ == "__main__":
    main()