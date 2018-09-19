# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-19 16:37
# File    : 1.Flask中的session.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
""
"""
Session的请求流程;
1、请求刚刚到达;
2、视图函数;
3、请求结果;
"""
from flask import Flask, session

app = Flask(__name__)

app.secret_key = 'fdjljfaljfkla'


@app.route('/index/')
def index():
    session['k1'] = 123
    return 'Index'


@app.route('/order/')
def order():
    print(session['k1'])
    return 'Order'


if __name__ == '__main__':
    app.run()
"""
1、Flask
2、RequestContext
3、Request
4、SecureCookieSessionInterface
5、SecureCookieSession(dict )
"""
