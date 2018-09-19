from flask import Flask, render_template, redirect, Markup

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
