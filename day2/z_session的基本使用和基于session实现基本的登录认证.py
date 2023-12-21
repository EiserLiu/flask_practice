from flask import Flask, request, redirect, url_for, Response, session, make_response

app = Flask(__name__)

# 因为session是基于cookie加密实现的,所以使用之前必须设置SECRET_KEY选项
app.config["SECRET_KEY"] = "asjdkawnfiuwecinwuegv13213gjg1jg1j"


@app.route("/set_session")
def set_session():
    session["user"] = "Liuzepu"
    session["user_id"] = 31
    session["data"] = [1, 2, 3]

    return "set_session"


@app.route("/get_session")
def get_session():
    print(f'user={session.get("user")}')
    print(f'user_id={session.get("user_id")}')
    print(f'data={session.get("data")}')
    return "get_session"


@app.route("/del_session")
def del_session():
    session.pop("user")
    session.pop("data")
    return "del_session"


@app.route("/login", methods=["get", "post"])
def login():
    form = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <title>登录</title>
        </head>
        <body>
            <form action="" method="post">
                账号:<input type="text" name="user"><br><br>
                密码:<input type="password" name="password"><br><br>
                <input type="submit" value="登录">
            </form>
        </body>
        </html>
    """

    if request.method == "GET":
        return make_response(form)

    user = request.form.get("user")
    password = request.form.get("password")

    if user == "root" and password == "123456":
        session["user"] = "root"
        session["password"] = "123456"
        response = make_response("登录成功")
        return response
    else:
        response = redirect("/login")
        return response


@app.route("/user")
def user():
    if not session.get("user"):
        response = redirect("/login")
        return response

    return "个人信息中心"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
