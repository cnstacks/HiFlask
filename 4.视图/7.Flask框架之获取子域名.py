# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 19:14
# File    : 7.Flask框架之获取子域名.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org
from flask import Flask

app = Flask(__name__)
app.config['SERVER_NAME'] = 'www.cuixiaozhao.com:5000'


# 从旧功能重定向至新功能页面;Js可以做重定向；meta头、js location href
@app.route('/dynamic/', methods=['GET', 'POST'], subdomain='<username>')
def sub_domain(username):
    print(username)
    return '旧的功能1'


if __name__ == '__main__':
    app.run()
