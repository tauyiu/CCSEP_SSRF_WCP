from flask import Flask, render_template, request, url_for, redirect
from random import randint

app = Flask(__name__)

@app.route("/")
def home():
    return "<h1>Welcome to Random Number Generator!</h1><p>Go to localhost:8080/generate to generate random numbers</p><p>Go to localhost:8080/admin and enter password to access admin page</p>"

@app.route("/generate")
def generate():
    return render_template("generator.html", content=getNumber())

def getNumber():
    n = randint(1, 1000000)
    return n

@app.route("/admin", methods=["POST", "GET"])
def admin():
    if request.method == "POST":
        value = request.form["password"]
        flag = request.form["trigger"]
        return adminPage(value, flag)
    else:
        return render_template("login.html")

def adminPage(pw, flag):
    if (pw == "qazwsxedcrfvtgbyhnujmikolp") or (flag == "t"):
        return render_template("admin.html")
    else:
        return "<h1>REQUEST DENIED</h1>"

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
