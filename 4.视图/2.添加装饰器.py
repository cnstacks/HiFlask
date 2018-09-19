# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 19:14
# File    : 2.添加装饰器.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask
import functools

app = Flask(__name__)


def wapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('before')
        return func(*args, **kwargs)

    return inner


@app.route('/xxxx/', methods=['GET', 'POST'])
@wapper
def index():
    return 'Index'


@app.route('/xxxx/', methods=['GET', 'POST'])
@wapper
def order():
    return 'Order'


if __name__ == '__main__':
    app.run()
