# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 22:23
# File    : 1.模板.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask, render_template, redirect, jsonify, make_response, Markup

app = Flask(__name__)


# 全局模板——每个模板均可调用的函数;
@app.template_global()
def cxz(a1, a2):
    return a1 + a2


def input(value):
    return Markup("<input value:'%s'/>" % value)


def gen_input(value):
    return Markup("<input value:'%s'/>" % value)


@app.route('/computed/', methods=['GET', 'POST'])
def computed():
    context = {
        'k1': 123,
        'k2': [11, 22, 33],
        'k3': {'name': 'cuixiaozhao', 'age': 84},
        'k4': lambda x: x + 1,  # 用户写简单的函数;
        'k5': gen_input
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()
