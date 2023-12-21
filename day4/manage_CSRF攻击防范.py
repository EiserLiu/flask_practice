import random

from flask import Flask, request, render_template, session, g
from flask_wtf import CSRFProtect
app = Flask(__name__, template_folder="templates")

app.config["SECRET_KEY"] = "my secret key"

csrf = CSRFProtect()
csrf.init_app(app)


def do_mobile(data, dot="*"):
    return data[:3] + dot * 4 + data[-4:]


app.add_template_filter(do_mobile, 'mobile')


@app.route("/user")
def user():
    title = "用户中心"
    html = render_template("index9.html", **locals())
    return html


@app.route("/transfer", methods=["POST"])
def transfer():
    return "转账成功"


if __name__ == '__main__':
    app.run(debug=True)
