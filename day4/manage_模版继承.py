import random

from flask import Flask, request, render_template, session, g

app = Flask(__name__, template_folder="templates")


def do_mobile(data, dot="*"):
    return data[:3] + dot * 4 + data[-4:]


app.add_template_filter(do_mobile, 'mobile')


@app.route("/")
def index6():
    title = "站点首页"
    html = render_template("index6.html", **locals())
    return html


@app.route("/list")
def index7():
    title = "商品列表页"
    html = render_template("index7.html", **locals())
    return html


@app.route("/user")
def index8():
    title = "用户页"
    html = render_template("index8.html", **locals())
    return html


if __name__ == '__main__':
    app.run(debug=True)
