from flask import Flask, request, redirect, url_for, Response

app = Flask(__name__)


@app.route("/user")
def index():
    if request.args.get("token"):
        return "个人信息"
    # # 跳转页面到登录视图
    # return redirect("/login")
    # 跳转页面到其他视图
    url = url_for("login")
    print(app.url_map)
    print(url)
    return redirect(url)


@app.route("/login")
def login():
    return "登录视图"


@app.route("/jump")
def jump():
    """跳转页面到站外"""
    """
    301:永久重定向,页面没有了,站点没有了,永久转移
    302:临时重定向,验证失败,访问需要权限的页面进行登录跳转,都属于临时跳转
    """
    # response = redirect("https://www.qq.com",302)
    # print(response)
    # return response

    # 底层原理
    response = Response("", 302, {"location": "https://www.jd.com"})
    return response


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
