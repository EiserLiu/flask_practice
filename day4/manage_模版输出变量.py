from flask import Flask, request, render_template, session, g

app = Flask(__name__, template_folder="templates")

app.config["SECRET_KEY"] = "asdkjhaskdkxct"


@app.route("/")
def index():
    # 基本类型
    num = 100
    num2 = 3.14
    is_bool = True
    title = "网页标题"
    # 复合类型
    set_var = {1, 2, 3, 4}
    list_var = ["小明", "小红", "小白"]
    dict_var = {"name": "root", "pwd": "123456"}
    tuple_var = (1, 2, 3, 4)
    # 更复杂的数据结构
    book_list = [
        {"id": 10, "title": "图书标题1"},
        {"id": 11, "title": "图书标题2"},
        {"id": 12, "title": "图书标题3"}
    ]

    session["name"] = "root"
    g.num = 300


    html = render_template("index.html", **locals())
    print(html, type(html))

    return html


if __name__ == '__main__':
    app.run()
