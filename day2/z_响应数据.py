import json

from flask import Flask, make_response, Response, jsonify

app = Flask(__name__)


# 1.接受客户端请求
# 2.根据客户端的请求操作数据,文件
# 3.响应数据,操作结果


@app.route("/header/", methods=["get", "post", "put", "patch", "delete"])
def index():
    """
    响应html文本并设置状态码
    """
    # return "<h1>hello flask<h1>", 400
    """通过make_response返回response对象"""
    # reponse = make_response("<h1>hello flask<h1>", 201)
    # print(reponse)
    # return reponse
    """通过Response返回response对象"""
    response = Response("<h1>hello flask<h1>,201")
    return response


@app.route("/jsonapi/")
def jsonapi():
    """响应JSON数据(原生写法)"""
    # data = {"name": "liuzepu", "age": 16}
    # return json.dumps(data), 200, {"Content-Type": "application/json"}
    """响应JSON数据(jsonify)"""
    data = {"name": "liuzepu", "age": 16}
    response = jsonify(data)
    print(response)
    return response


@app.route("/img/")
def img():
    """响应图片格式给客户端"""
    with open("avatar.png", "rb") as f:
        data = f.read()
    return data, 200, {"Content-Type": "image/png"}

0
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
