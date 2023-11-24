from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def homePg():
    return render_template("index.html")

@app.route("/login", methods=["POST"])
def login():
    if request.method=="POST":
        username = request.form["username"]
        password = request.form["password"]
        return render_template("login.html", name=username.capitalize(), password=password)
if(__name__=="__main__"):
    app.run(debug=True)