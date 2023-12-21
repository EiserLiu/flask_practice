from flask import Flask, request, redirect, url_for, Response

app = Flask(__name__)


@app.route("/sms/<int:mobile>")
def sms(mobile):
    """发送短信"""
    return f"发送短信给{mobile}"


@app.route("/info")
def info():
    # return redirect("/sms/13012345678")
    url = url_for("sms", mobile="13012345678")
    print(url)
    return redirect(url)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
