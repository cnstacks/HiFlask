# -*- coding:utf-8 -*-
# Project: Day123 
# Software: PyCharm
# Time    : 2018-09-18 22:13
# File    : 2.请求和响应.py
# Author  : 天晴天朗
# Email   : tqtl@tqtl.org


from flask import Flask, render_template, request, redirect, jsonify, make_response

app = Flask(__name__)

app.config.from_object("settings.DevelopmentConfig")


@app.route('/index/', methods=['GET', 'POST'])
def index():
    # 请求相关;
    request.args

    # 响应相关;
    return ''
    return render_template()
    return redirect('/index/')
    # 返回json数据;
    return json.dumps({})  # return jsonify({})


if __name__ == '__main__':
    app.run()
"""
        # 请求相关信息;
        # request.method
        # request.args
        # request.form
        # request.values
        # request.cookies
        # request.headers
        # request.path
        # request.full_path
        # request.script_root
        # request.url
        # request.base_url
        # request.url_root
        # request.host_url
        # request.host
        # request.files
        # obj = request.files['the_file_name']
        # obj.save('/var/www/uploads/' + secure_filename(f.filename))

        # 响应相关信息;
        # return "字符串"
        # return render_template('html模板路径',**{})
        # return redirect('/index.html')

        # response = make_response(render_template('index.html'))
        # response是flask.wrappers.Response类型;
        # response.delete_cookie('key')
        # response.set_cookie('key', 'value')
        # response.headers['X-Something'] = 'A value'
        # return response
"""
