from flask import Flask

app = Flask(__name__)


@app.before_request
def before_requset():
    print("before_requset被执行了")
"""当项目被客户端访问时执行"""

@app.after_request
def after_request(response):
    """响应时执行"""
    print("after_request被执行了")
    return response

@app.teardown_request
def teardown_requset(exc):
    """每次访问报错,执行@app.teardown_request的函数"""
    print("teardown_request被执行了")
    print(f"错误信息{exc}")




@app.route("/")
def index():
    print("start")
    return "ok"

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)