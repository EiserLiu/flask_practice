import random

from flask import Flask, request, render_template, session, g

app = Flask(__name__, template_folder="templates")


@app.route("/")
def index():

    html = render_template("index4.html", **locals())
    return html


if __name__ == '__main__':
    app.run(debug=True)

# safe：标记一个字符串为安全的，告诉 Jinja2 不需要转义该字符串。
# {{ "<strong>HTML</strong>"|safe }}

# capitalize：将字符串首字母大写。
# {{ "hello world"|capitalize }}

# lower：将字符串转换为小写。
# {{ "HELLO"|lower }}

# upper：将字符串转换为大写。
# {{ "hello"|upper }}

# title：将字符串内的每个单词的首字母大写。
# {{ "hello world"|title }}

# truncate：截断字符串至指定长度。
# {{ "This is a long text."|truncate(10) }}

# length：返回字符串或列表的长度。
# {{ "hello"|length }}
# {{ [1, 2, 3]|length }}

# default：如果变量为空或不存在，则使用默认值。
# {{ username|default("Guest") }}

# date：将日期对象格式化为指定格式的字符串。
# {{ datetime.now()|date("%Y-%m-%d") }}