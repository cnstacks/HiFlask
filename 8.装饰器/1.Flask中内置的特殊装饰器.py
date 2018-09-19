# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-19 17:22
# File    : 1.Flask中内置的特殊装饰器.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask, render_template, redirect

app = Flask(__name__)


# before_request和after_request类似于Django中的中间件middleware；
@app.before_request
def before_req():
    print('before_request，前')


@app.before_request
def before_req1():
    print('before_request1，前')


# request之前，会添加一个reverse反转;
@app.after_request
def after_req(response):
    print('after_request, 后')
    return response


@app.after_request
def after_req1(response):
    print('after_request1, 后')
    return response


@app.route('/x1/', methods=['GET', 'POST'])
def x1():
    print('视图函数X1')
    return 'X1'


@app.route('/x2/', methods=['GET', 'POST'])
def x2():
    print('视图函数X2')
    return 'X2'


if __name__ == '__main__':
    app.run()
