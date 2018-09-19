# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 11:06
# File    : 3.面向对象.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


""
"""
谈谈你对面向对象的认识？
封装：
    将同一类方法分为一类，方法封装到类中；
    将方法中的共同的参数封装到对象中，把共同的值封装到对象中；
"""


# 用户类实现;
class File:
    def __init__(self, a1, a2, a3, a4):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4

    def file_add(self):
        pass

    def file_del(self):
        pass

    def file_update(self):
        pass

    def file_fetch(self):
        pass


# 给了一些值，将数据加工，应用场景:Django自定义分页;
class Foo():
    def __init__(self, a1, a2, a3, a4, a5, a6, a7):
        self.a1 = a1
        self.a2 = a2
        self.a3 = a3
        self.a4 = a4
        self.a5 = a5
        self.a6 = a6
        self.a7 = a7

    def sum(self):
        return self.a1 + self.a2

    def reduce(self):
        return self.a5 - self.a7


obj = File(1, 2, 3, 4)
print(obj)  # <__main__.File object at 0x10bbf25c0>


class A(object):
    def __init__(self):
        self.age1 = 123
        self.a = A()


class B(object):
    def __init__(self):
        self.age2 = 123
        self.b = B()


class C(object):
    def __init__(self):
        self.age3 = 123
        self.c = C()


class D(object):
    def __init__(self):
        self.age4 = 123
        self.d = D()
