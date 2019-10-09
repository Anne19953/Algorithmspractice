#!/usr/bin/env python
# coding:utf-8
"""
Name : 整数中1的个数
Author  : anne
Time    : 2019-09-19 10:56
Desc:
"""

"""
原理是不断清除n的二进制表示中最右边的1，同时累加计数器，直至n为0
n &= (n – 1)能清除最右边的1呢？因为从二进制的角度讲，n相当于在n - 1的最低位加上1。
举个例子，8（1000）= 7（0111）+ 1（0001），
所以8 & 7 = （1000）&（0111）= 0（0000），清除了8最右边的1（其实就是最高位的1，因为8的二进制中只有一个1）。
再比如7（0111）= 6（0110）+ 1（0001），
所以7 & 6 = （0111）&（0110）= 6（0110），清除了7的二进制表示中最右边的1（也就是最低位的1）。
n & 0xffffffff 去掉负号，python中bin一个负数（十进制表示），输出的是它的原码的二进制表示加上个负号

"""
def BitCount(n):
    c =0
    if n < 0:
        n = n & 0xffffffff
    while n :
        c += 1
        n = (n-1) & n
    return c

print(BitCount(15))
print(BitCount(-3))
print(BitCount(0))


"""
转化为二进制统计里面1的个数
"""
def BitCount2(n):

    if n < 0:
        n = n & 0xffffffff

    return bin(n).count('1')

# print(BitCount2(15))
# print(BitCount2(-3))
# print(BitCount2(0))
b = BitCount2(-3) #str类型
print(b)