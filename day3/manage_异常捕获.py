from flask import Flask,request,abort

app = Flask(__name__)


@app.route("/")
def index():
    password = request.args.get("password")
    if password != "123456":
        print(a)
        #abort参数:http状态异常码;错误相关的提示内容
        # abort(400)
    return "ok"
@app.errorhandler(NameError)
def NameErrorFunc(exc):

    print(exc.__traceback__)
    return f"错误提示:{exc}"

@app.errorhandler(400)
def error_400(exc):
    print(exc.args)
    print(exc.__traceback__)
    return {"error": f"{exc}"}


if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)