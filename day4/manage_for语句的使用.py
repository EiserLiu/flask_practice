import random

from flask import Flask, request, render_template, session, g

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():
    book_list = [
        {"id": 10, "title": "图书标题1"},
        {"id": 11, "title": "图书标题2"},
        {"id": 12, "title": "图书标题3"}
    ]
    html = render_template("index3.html", **locals())
    return html


if __name__ == '__main__':
    app.run(debug=True)
