from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
import os

currdir = os.path.dirname(__file__)
fullPath = os.path.join(currdir,"books-collection.db")

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+currdir+"/books-collection.db"

db=SQLAlchemy(app)

class books(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title = title
        self.author = author
        self.rating = rating

with app.app_context():
    db.create_all()

# all_books = []


@app.route('/', methods=['GET', 'POST'])
def home():
    if(request.method=='POST'):
        id = request.args.get("id")
        newRating = request.form["rating"]
        book = books.query.get(id)
        book.rating = newRating
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    else:
        all_books = books.query.all()
        return render_template("index.html", books=all_books)


@app.route("/add", methods=['GET','POST'])
def add():
    if(request.method=='GET'):
        return render_template("add.html")
    else:
        name = request.form["bkName"]
        author = request.form["bkAuthor"]
        rating = request.form["bkRating"]
        # print(name, author, rating)
        # tempDict = {"title": name, "author": author, "rating": rating}
        # all_books.append(tempDict)
        db.session.add(books(name,author, rating))
        db.session.commit()
        return redirect(url_for("home"))
    
@app.route("/edit")
def editRating():
    id=request.args.get("id")
    book = books.query.get(id)
    return render_template("editRating.html", book=book)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    book = books.query.get(id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))

if __name__ == "__main__":
    app.run(debug=True)

