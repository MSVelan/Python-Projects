from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FloatField
from wtforms.validators import DataRequired
import requests, os

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
Bootstrap(app)

currdir = os.path.dirname(__file__)
# print(currdir)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"+currdir+"/movie-collection.db"
db = SQLAlchemy(app)

theMovieDbAPI = "8f20191464b277f109b3dc6b9b956d10"

class Movies(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    title = db.Column(db.String(100), nullable=False)
    year = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(500), nullable = False)
    rating = db.Column(db.Float, nullable = False)
    ranking = db.Column(db.Integer, nullable = False)
    review = db.Column(db.String(300), nullable = False)
    img_url = db.Column(db.String(500), nullable = False)

    def __init__(self, title, year, desc, rating, ranking, review, img_url):
        self.title = title
        self.year = year
        self.description = desc
        self.rating = rating
        self.ranking = ranking
        self.review = review
        self.img_url = img_url

class RateMovieForm(FlaskForm):
    rating = FloatField("Your rating out of 10", validators=[DataRequired()])
    review = StringField("Your review", validators=[DataRequired()])
    submitbtn = SubmitField("Done")

class AddMovieForm(FlaskForm):
    title = StringField("Movie Title", validators=[DataRequired()])
    submitbtn = SubmitField("Add Movie")

new_movie = Movies("Phone Booth",2002,"Publicist Stuart Shepard finds himself trapped in a phone booth, pinned down by an extortionist's sniper rifle. Unable to leave or receive outside help, Stuart's negotiation with the caller leads to a jaw-dropping climax.",7.3,10,"My favourite character was the caller.","https://image.tmdb.org/t/p/w500/tjrX2oWRCM3Tvarz38zlZM7Uc10.jpg")

with app.app_context():
    db.create_all()
    # db.session.add(new_movie)
    # db.session.commit()

@app.route("/")
def home():
    movies = Movies.query.order_by(Movies.rating).all()
    n = len(movies)
    for i in range(n):
        movies[i].ranking = n-i
    db.session.commit()

    trendURL = "https://api.themoviedb.org/3/trending/movie/week"

    params = {
        "language":"en-US",
        "api_key":theMovieDbAPI
    }

    trending = []
    data = requests.get(trendURL, params=params).json()["results"]
    for i in data:
        imgBase = i["poster_path"]
        img_url = "https://image.tmdb.org/t/p/w500"+imgBase
        movie = Movies(i["title"],i["release_date"],i["overview"],"","","",img_url)
        trending.append(movie)

    for i in range(len(trending)):
        trending[i].ranking=i+1

    return render_template("indexNew.html", movies=movies, rc=trending)

@app.route("/edit", methods=['GET','POST'])
def edit():
    editForm = RateMovieForm()
    if(request.method=="POST"):
        id = request.args.get("id")
        if(editForm.validate_on_submit()):
            rating = editForm.rating.data
            review = editForm.review.data
            movie = Movies.query.get(id)
            movie.rating = rating
            movie.review = review
            db.session.add(movie)
            db.session.commit()
        return redirect(url_for("home"))
    else:
        id = request.args.get("id")
        return render_template("edit.html", form=editForm, id=id)

@app.route("/delete")
def delete():
    id = request.args.get("id")
    movie = Movies.query.get(id)
    db.session.delete(movie)
    db.session.commit()
    return redirect(url_for("home"))

@app.route("/add", methods=["GET","POST"])
def add():
    addForm = AddMovieForm()
    if request.method=="GET":
        return render_template("add.html", form=addForm)
    else:
        movieTitle = addForm.title.data
        parameters = {
            "query":movieTitle,
            "api_key":theMovieDbAPI
        }
        movieDbURL = "https://api.themoviedb.org/3/search/movie"
        response = requests.get(movieDbURL,params=parameters).json()
        data = response["results"]
        return render_template("select.html", movies=data)

@app.route("/fetch")
def fetch():
    id = request.args.get("id")
    fetchURL = "https://api.themoviedb.org/3/movie/"+id
    parameters = {
        "api_key":theMovieDbAPI
    }
    data = requests.get(fetchURL,params=parameters).json()
    imgBase = data["poster_path"]
    img_url = "https://image.tmdb.org/t/p/w500"+imgBase
    title = data["title"]
    description = data["overview"]
    release_date = data["release_date"]
    year = release_date.split("-")[0]

    new_movie = Movies(title,year,description,1,10,"None",img_url)
    db.session.add(new_movie)
    db.session.commit()
    return redirect(url_for("edit", id = new_movie.id))

if __name__ == '__main__':
    app.run(debug=True)
