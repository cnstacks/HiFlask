# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-19 18:13
# File    : 1.Flask之中间件.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask

app = Flask(__name__)
app.secret_key = 'fjaljfdklajfkdasl'


@app.route('/x2', methods=['GET', 'POST'])
def index():
    return 'x2'


class MiddleWare(object):
    def __init__(self, old_wsgi_app):
        self.old_wsgi_app = old_wsgi_app

    def __call__(self, *args, **kwargs):
        print('before')
        obj = self.old_wsgi_app(*args, **kwargs)
        print('after')
        return obj


if __name__ == '__main__':
    app.wsgi_app = MiddleWare(app.wsgi_app)
    app.run()
"""
1、执行app.__call__方法;
2、在调用app.wsgi_app方法;
"""
