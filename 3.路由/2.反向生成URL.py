# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 12:06
# File    : 2.反向生成URL.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


# endpoint&url_for不起别名默认就是函数名;
@app.route('/index/', methods=['GET', 'POST'])
def index():
    v1 = url_for('n1')
    # v2 = url_for('n1')
    # v2 = url_for('n2')
    v2 = url_for('login')
    v3 = url_for('logout')
    print(v1, v2, v3)
    return 'Index'


@app.route('/login/', methods=['GET', 'POST'], endpoint='n2')
def login():
    return 'Login'


@app.route('/logout/', methods=['GET', 'POST'], endpoint='n3')
def logout():
    return 'Logout'
