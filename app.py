from flask import Flask, render_template, redirect

app = Flask(__name__)
# Flask的配置文件这么玩耍;
app.config.from_object("settings.DevelopmentConfig")


# 添加的第一种方式,推荐使用装饰器的方式;
@app.route('/index/', methods=['GET', 'POST'])
def index():
    return '# 添加的第一种方式,推荐使用装饰器的方式;'


# 添加路由的另外一种方式;


def order():
    return '# 添加路由的第二种方式;'


app.add_url_rule('/order/', view_func=order)


@app.route('/old/', methods=['GET', 'POST'], redirect_to='/new/')
def old():
    return '旧的功能'


@app.route('/new/', methods=['GET', 'POST'])
def new():
    return '新功能'


if __name__ == '__main__':
    app.run()
