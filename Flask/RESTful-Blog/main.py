from flask import Flask, render_template, redirect, url_for, request
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from flask_wtf.form import _Auto
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditor, CKEditorField
import os
from datetime import datetime

## Delete this code:
# import requests
# posts = requests.get("https://api.npoint.io/43644ec4f0013682fc0d").json()

app = Flask(__name__)
app.config['SECRET_KEY'] = '8BYkEfBA6O6donzWlSihBXox7C0sKR6b'
ckeditor = CKEditor(app)
Bootstrap(app)

##CONNECT TO DB
fullPath = os.path.join(os.path.dirname(__file__),"posts.db")
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+fullPath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CONFIGURE TABLE
class BlogPost(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), unique=True, nullable=False)
    subtitle = db.Column(db.String(250), nullable=False)
    date = db.Column(db.String(250), nullable=False)
    body = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(250), nullable=False)
    img_url = db.Column(db.String(250), nullable=False)

    def __init__(self, title, subtitle, date, body, author, img_url):
        self.title = title
        self.subtitle = subtitle
        self.date = date
        self.body = body
        self.author = author
        self.img_url = img_url


##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    author = StringField("Your Name", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")


@app.route('/')
def get_all_posts():
    posts = BlogPost.query.all()
    return render_template("index.html", all_posts=posts)


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    posts = BlogPost.query.all()
    for blog_post in posts:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/edit/<int:post_id>", methods=["GET","POST"])
def edit_post(post_id):
    post = BlogPost.query.get(post_id)
    form = CreatePostForm(title = post.title, subtitle= post.subtitle, author=post.author, body = post.body, img_url=post.img_url)
    if form.validate_on_submit():
        post.title = form.title.data
        post.subtitle = form.subtitle.data
        post.body = form.body.data
        post.author = form.author.data
        post.img_url = form.img_url.data
        db.session.commit()
        return redirect(url_for("show_post", index=post_id))
    return render_template("make-post.html", form=form, heading="Edit Post")

@app.route("/new-post", methods=['GET','POST'])
def makePost():
    form = CreatePostForm()
    if(request.method=="GET"):
        return render_template("make-post.html", form=form, heading="New Post")
    else:
        if form.validate_on_submit():
            date = datetime.now()
            d = date.strftime("%B %d, %Y")
            title = form.title.data
            subtitle = form.subtitle.data
            body = form.body.data
            author = form.author.data
            img_url = form.img_url.data
            post = BlogPost(title, subtitle, d, body, author, img_url)
            db.session.add(post)
            db.session.commit()
            return redirect(url_for("get_all_posts"))
        
        else:
            return "<h1>Enter Valid credentials</h1>"

@app.route("/delete/<int:post_id>")
def delete(post_id):
    post = BlogPost.query.get(post_id)
    db.session.delete(post)
    db.session.commit()
    return redirect(url_for("get_all_posts"))
        
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)