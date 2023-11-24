from flask import Flask, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired,Email,Length
from flask_bootstrap import Bootstrap

class ContactForm(FlaskForm):
    email=StringField("Email", validators=[DataRequired(), Email(message="Invalid email address.")])
    password=PasswordField("Password", validators=[DataRequired(), Length(min=8,message="Password must be atleast 8 characters long.")])
    submit = SubmitField("Log In")


def create_app():
  app = Flask(__name__)
  Bootstrap(app)
  return app

app = create_app()
app.secret_key="MSVgeek"

@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET","POST"])
def login():
    contactForm = ContactForm()
    if contactForm.validate_on_submit():
        emailData = (contactForm.email.data)
        passwordData = (contactForm.password.data)
        if(emailData=="admin@email.com" and passwordData=="12345678"):
            return render_template("success.html")
        else:
            return render_template("denied.html")
    return render_template("login.html", form=contactForm)

if __name__ == '__main__':
    app.run(debug=True)