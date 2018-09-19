# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 21:57
# File    : 1.Flask框架之CBV和FBV.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask, redirect, render_template, views

app = Flask(__name__)
import functools


def wapper(func):
    @functools.wraps(func)
    def inner(*args, **kwargs):
        print('before')
        return func(*args, **kwargs)

    return inner


@app.route('/xxx/', methods=['GET', 'POST'])
@wapper
def index():
    return 'Index'


class IndexView(views.View):
    methods = ['GET']
    decorators = [wapper, ]

    def dispatch_request(self):
        print('Index')
        return 'Index'


app.add_url_rule('/index/', view_func=IndexView.as_view(name='index'))  # name == endpoint


# CBV方式;
class IndexView(views.MethodView):
    methods = ['GET']
    decorators = [wapper]

    def get(self):
        return 'Index.GET'

    def post(self):
        return 'Index POST'


app.add_url_rule('/index/', view_func=IndexView.as_view(name='index'))  # name = endpoint

if __name__ == '__main__':
    app.run()
