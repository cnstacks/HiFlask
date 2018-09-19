from flask import Flask, render_template, redirect, Markup

app = Flask(__name__)
# Flask的配置文件这么玩耍;
app.config.from_object("settings.DevelopmentConfig")



if __name__ == '__main__':
    app.run()
