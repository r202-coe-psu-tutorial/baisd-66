from flask import Flask, render_template, redirect, url_for, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html.j2", name=request.args.get("name"))


@app.route("/me")
def me():
    return "Hello World"


@app.route("/write")
def write():
    print("write -->", request.form)
    return render_template("write.html.j2")


@app.route("/save", methods=["POST"])
def save():
    print("save -->", request.form)
    return redirect(url_for("index", name=request.form.get("message", "No message")))
