from flask import Flask, render_template
from post import Post
import requests

app = Flask(__name__)

blogsUrl = "https://api.npoint.io/baa3d9f77f2dbc33d9d1"
blogs = requests.get(url=blogsUrl).json()
posts = []
for blog in blogs:
    post_obj = Post(blog["id"],blog["title"],blog["subtitle"],blog["body"])
    posts.append(post_obj)

@app.route('/')
def home():
    return render_template("index.html", blogs=blogs)

@app.route('/post/<int:blogId>')
def blogPage(blogId):
    for post in posts:
        if(post.id==blogId):
            return render_template("post.html",blog=post)

if __name__ == "__main__":
    app.run(debug=True)
