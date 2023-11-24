# import sqlite3
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# import sqlalchemy as sa
import os
currdir = os.path.dirname(__file__)
filename = "books-collection.db"
fullPath = os.path.join(currdir, filename)


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"]="sqlite:///"+currdir+"/new-books-collection.db"
db = SQLAlchemy()
db.init_app(app)


class books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __init__(self, title, author, rating):
        self.title=title
        self.author=author
        self.rating=rating

with app.app_context():
    db.create_all()
    # db.session.add(books("Tale of two cities", "Jane Austen",7.8))
    # db.session.commit()

    all_books = db.session.query(books).all()
    Books = books.query.all()
    print(all_books)

# db = sqlite3.connect(fullPath)
# cursor = db.cursor()

# cursor.execute("create table books(id integer primary key, title varchar(250) not null unique, author varchar(250) not null, rating float not null)")

# cursor.execute("Insert into books values(1, 'Harry Potter', 'J.K. Rowling', '9.3')")
# db.commit()