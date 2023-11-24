from flask import Flask
import random

app = Flask(__name__)

@app.route("/")
def mainPage():
    return "<h1>Guess a number between 0 and 9</h1> \
        <img src='https://media.giphy.com/media/3o7aCSPqXE5C6T8tBC/giphy.gif' alt='Gif for guess the number'/>"

def generateRandomNumber():
    random.seed()
    r = random.randint(0,9)
    return r

r = generateRandomNumber()

@app.route("/<int:n>")
def checkHigherLower(n):
    if(n<r):
        return "<h1 style= 'color: red'>Too low, try again!</h1> \
            <img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif' alt='Low gif'/>"
    elif(n>r):
        return "<h1 style= 'color: purple'>Too high, try again!</h1> \
            <img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif' alt='High gif'/>"
    else:
        return "<h1 style= 'color: green'>You found me!</h1> \
            <img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif' alt='Correct gif' />"

if(__name__=="__main__"):
    app.run(debug=True)