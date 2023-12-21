import json

from flask import Flask, request
from urllib.parse import parse_qs

app = Flask(__name__)


@app.route("/form/", methods=["post"])
def form():
    print(request.args)
    print(request.form.get("user"))
    print(request.files.get("password"))
    print(request.files.getlist("password"))

    return "hello flask"


@app.route("/data/", methods=["post"])
def data():
    # print(request.is_json)  # 判断本次请求是不是ajax请求
    print(request.json)       # 获取JSON数据
    print(json.loads(request.data))
    return "hello flask_form"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
