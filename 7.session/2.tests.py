# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-19 16:45
# File    : 2.tests.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


# 方式一:
# class Foo(object):
#     def __setitem__(self, key, value):
#         pass
#
#
# obj = Foo()
#
# obj['name'] = 'cuixiaozhao'
# 方式二:
class Foo(dict):
    pass


obj = Foo()
