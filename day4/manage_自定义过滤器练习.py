import random

from flask import Flask, request, render_template, session, g

app = Flask(__name__, template_folder="templates")


def do_mobile(data, dot="*"):
    return data[:3] + dot * 4 + data[-4:]


app.add_template_filter(do_mobile, 'mobile')


@app.route("/")
def index():
    user_list = [
        {"id": 1, "name": "张三", "mobile": "13712345678"},
        {"id": 2, "name": "李四", "mobile": "13712345678"},
        {"id": 3, "name": "王五", "mobile": "13712345678"},
        {"id": 4, "name": "赵六", "mobile": "13712345678"},
    ]
    html = render_template("index5.html", **locals())
    return html


if __name__ == '__main__':
    app.run(debug=True)
