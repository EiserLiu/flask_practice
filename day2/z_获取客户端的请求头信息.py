import json

from flask import Flask, request
from urllib.parse import parse_qs

app = Flask(__name__)


@app.route("/header/", methods=["get", "post", "put", "patch", "delete"])
def form():
    # # 获取所有请求头信息
    # print(request.headers, type(request.headers))
    # # 获取单个请求头信息
    # print(request.headers.get("User-Agent"))  # 获取客户端的网络代理工具名称
    # print(request.user_agent)
    # print(request.host)  # 获取本次客户端请求的服务端地址
    # print(request.content_type)  # 获取本次客户端请求的提交格式
    # print(request.path)  # 获取本次客户端请求的url路径
    # print(request.url)  # 获取本次客户端请求的完整url路径
    # print(request.root_url)  # 获取本次客户端请求的服务端域名
    # print(request.method)  # 获取本次客户端的http请求方法或请求动作
    # print(request.remote_addr)  # 获取本次客户端地址
    # print(request.server)  # 获取本次客户端的server信息
    # print(request.environ)  # 获取本次客户端请求时的系统环境变量信息
    #获取自定义的请求头
    print(request.headers.get("company"))
    return "hello flask"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
