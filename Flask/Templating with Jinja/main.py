from flask import Flask, render_template
import random
from datetime import datetime
import requests

app = Flask(__name__)

@app.route('/')
def home():
    randomNumber = random.randint(1,10)
    now = datetime.now().year
    return render_template("index.html",num=randomNumber, year=now)

@app.route('/guess/<name>')
def Guess(name):
    ageUrl = "https://api.agify.io"
    genderUrl = "https://api.genderize.io"
    parameters = {
        "name":name
    }
    response = requests.get(url=ageUrl,params=parameters).json()
    age = response["age"]
    response = requests.get(url=genderUrl,params=parameters).json()
    gender = response["gender"]
    return render_template("guess.html",name=name.capitalize(),age=age,gender=gender)

@app.route("/blog")
def getBlog():
    blogUrl = "https://api.npoint.io/baa3d9f77f2dbc33d9d1"
    response = requests.get(url=blogUrl)
    allPosts = response.json()
    return render_template("blog.html",posts=allPosts)

if __name__ == "__main__":
    app.run(debug=True)


