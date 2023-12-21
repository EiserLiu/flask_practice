from flask import Flask, request
from urllib.parse import parse_qs
app = Flask(__name__)


@app.route("/gs")
def index():
    # print(request.query_string)
    # # b'user=liuzepu&password=159753'
    # query_string=parse_qs(request.query_string)
    # print(query_string)

    print(request.args)
    # ImmutableMultiDict([('user', 'liuzepu'), ('password', '159753')])
    print(request.args["user"])
    print(request.args.getlist("password"))

    return "hello flask"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
