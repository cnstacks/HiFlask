# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-19 17:22
# File    : 2.基于Flask中内置的特殊装饰器做登录验证.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask, render_template, redirect, request, session

app = Flask(__name__)
app.secret_key = 'fdsjklfdjaslkjflas'


# before_request和after_request类似于Django中的中间件middleware；
@app.before_request
def check_login():
    if request.path == '/login/':
        return None
    user = session.get('user_info')
    if not user:
        return redirect('/login/')


@app.route('/login/', methods=['GET', 'POST'])
def login():
    return 'Login'


@app.route('/index/', methods=['GET', 'POST'])
def index():
    return 'Index'


if __name__ == '__main__':
    app.run()
