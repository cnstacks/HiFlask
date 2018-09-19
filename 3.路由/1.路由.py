# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 11:48
# File    : 1.路由.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org

from flask import Flask

app = Flask(__name__)
app.debug = True


# 添加的第一种方式;
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return '# 添加的第一种方式;'


# 添加路由的另外一种方式;


def order():
    return '# 添加路由的第二种方式;'


app.add_url_rule('/order/', view_func=order)
if __name__ == '__main__':
    app.run()
