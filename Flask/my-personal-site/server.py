from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homePage():
    return render_template("CSS-MySite.html")

if(__name__=="__main__"):
    app.run(debug=True)

#shift+reload for hard reload in chrome to remove the cached static files