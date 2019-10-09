#!/usr/bin/env python
# coding:utf-8
"""
Name : 数值的整数次方
Author  : anne
Time    : 2019-09-19 12:57
Desc:
"""
"""
如果指数为0，值为1，如果底数为1，值为1，如果指数为负数，值为指数为整数时的值

"""

def Power( base, exponent):
    result = 1
    if exponent == 0:
        return result
    if base == 1:
        return result
    if exponent < 0:
        exponent = -exponent
        for _ in range(exponent):
            result = result*base
        return 1/result
    else:
        for _ in range(exponent):
            result = result*base
        return result


##############改进
def Power1(base,exponent):
    flag = 0
    if base == 0:
        return False
    if exponent == 0:
        return 1
    if exponent < 0:
        flag = 1
    result = 1
    for _ in range(abs(exponent)):
        result *= base
    if flag == 1:
        result = 1/result
    return result






print(Power(3,3),Power1(3,3),)
print(Power(3,0),Power1(3,0),)
print(Power(1,2),Power1(1,2),)
print(Power(1,-2),Power1(1,-2),)
print(Power(3,-3),Power1(3,-3),)

