# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 19:14
# File    : 4.Flask框架之app.route参数.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask

app = Flask(__name__)


# 从旧功能重定向至新功能页面;Js可以做重定向；meta头、js location href
@app.route('/index/', methods=['GET', 'POST'], redirect_to='/new/')
def index():
    return '旧的功能'


@app.route('/new/', methods=['GET', 'POST'])
def new():
    return '新功能'


if __name__ == '__main__':
    app.run()
