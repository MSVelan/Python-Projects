from flask import Flask
from flask import render_template, request
import requests, smtplib

app = Flask(__name__)

myEmail = "muthiahsivavelan2026@gmail.com"
password = "georbwnnngsbqtmr"

blogsUrl = "https://api.npoint.io/baa3d9f77f2dbc33d9d1"
blogsData = requests.get(url=blogsUrl).json()

@app.route("/about")
def aboutPg():
    return render_template("about.html")

@app.route("/")
def home():
    return render_template("index.html", blogsData = blogsData)

@app.route("/contact", methods=["GET","POST"])
def contactPg():
    if (request.method=="GET"):
        return render_template("contact.html", pgHeading="Contact Me")
    else:
        userName = request.form["userName"]
        userEmail = request.form["userEmail"]
        userPh = request.form["userPh"]
        userMsg = request.form["userMsg"]
        subject = "From the contact form"
        message = (f"Subject:{subject}\n\nUser: {userName}\n Email: {userEmail}\n Phone: {userPh}\n Message: {userMsg}")
        print(message)
        with smtplib.SMTP("smtp.gmail.com:587") as connection:
            connection.starttls()
            connection.login(myEmail, password=password)
            connection.sendmail(from_addr=userEmail, to_addrs=myEmail, msg=message.encode("utf8"))
        return render_template("contact.html",pgHeading="Successfully sent your message!")

@app.route("/post/<int:blogId>")
def samplePost(blogId):
    for blog in blogsData:
        if(blog["id"]==blogId):
            return render_template("post.html", blog=blog)


if(__name__=="__main__"):
    app.run(debug=True)