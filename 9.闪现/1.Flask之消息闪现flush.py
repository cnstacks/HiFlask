# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-19 18:03
# File    : 1.Flask之消息闪现flush.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from flask import Flask, session, flash, get_flashed_messages

app = Flask(__name__)
app.secret_key = 'fdjslkjflkafdaklfjdlakfj'


# # 生成session;
# @app.route('/x1/', methods=['GET', 'POST'])
# def login():
#     session['mgs'] = 'cuixiaozhao'
#     return '视图函数1'
#
#
# # 销毁session;;
# @app.route('/x2/', methods=['GET', 'POST'])
# def index():
#     msg = session.pop('msg')
#     print(msg)
#     return '视图函数2'
# 消息闪现之flask生成session;
@app.route('/x1/', methods=['GET', 'POST'])
def login():
    flash('cuixiaozhao', category='x1')
    flash('cuixiaozhao', category='x2')
    return '视图函数1'


# 消息闪现之flask销毁session;;
@app.route('/x2/', methods=['GET', 'POST'])
def index():
    data = get_flashed_messages(category_filter=['x1', 'x2'])
    print(data)
    return '视图函数2'


if __name__ == '__main__':
    app.run()
