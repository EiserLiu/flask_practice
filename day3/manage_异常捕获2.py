from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")


class NetWorkError(Exception):
    pass


@app.route("/")
def index():
    password = request.args.get("password")
    if password != "123456":
        raise NetWorkError("网络请求错误")
    return render_template("get_offer.html", title="offer")


@app.errorhandler(NetWorkError)
def network_error(exc):
    return {"error": f"{exc}"}


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
