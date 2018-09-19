# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 10.中间件:45
# File    : 1.装饰器.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

import functools
def wapper(func):
    @functools.wraps(func)
    def inner(*args,**kwargs):
        return func(*args,**kwargs)
    return inner
'''
1、执行wapper函数，并将被装饰的函数当做参数。wapper(index)
2、将第一步的返回值，重新赋值给index = wapper（old index）

'''

#1、为什么要使用装饰器？在不改变原来函数的基础之上，对函数执行前后进行自定义操作；
@wapper
def index(a1):
    return a1 +1000

v = index(2)
print(v)
#获取函数名
print("打印函数名:",index.__name__)


@wapper
def order(a1):
    return a1+1000

print(index.__name__)
print(order.__name__)