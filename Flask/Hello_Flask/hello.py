from flask import Flask

app = Flask(__name__)


def make_bold(function):
    def wrapper_function():
        string = function()
        return "<b>"+string+"</b>"
    return wrapper_function

def make_emphasis(function):
    def wrapper_function():
        string = function()
        return "<em>"+string+"</em>"
    return wrapper_function

def make_underlined(function):
    def wrapper_function():
        string = function()
        return "<u>"+string+"</u>"
    return wrapper_function

@app.route("/")
@make_bold
@make_emphasis
@make_underlined
def hello_world():
    return "<p>Hello, World!</p> \
        <p>Sup</p>"

@app.route("/username/<name>")
def greeting(name):
    return f"<p>Hi, {name}..</p>"

@app.route("/bye")
def bye():
    return "<h1> Ciao </h1> \
        Bye!!"

if(__name__=="__main__"):
    app.run(debug=True)