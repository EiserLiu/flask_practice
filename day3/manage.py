from flask import Flask, render_template, request

app = Flask(__name__, template_folder="templates")

@app.route("/")
def index():
    pass



if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
