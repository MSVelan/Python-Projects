from flask import Flask, render_template, request, url_for, redirect, flash, send_from_directory
from werkzeug.security import generate_password_hash, check_password_hash
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin, login_user, LoginManager, login_required, current_user, logout_user

import os

app = Flask(__name__)
login_manager = LoginManager()

login_manager.init_app(app)

fullPath = os.path.join(os.path.dirname(__file__),"users.db")

app.config['SECRET_KEY'] = 'any-secret-key-you-choose'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+fullPath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

##CREATE TABLE IN DB
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

#Line below only required once, when creating DB. 
with app.app_context():
    db.create_all()


@app.route('/')
def home():
    return render_template("index.html")

def validate_email(email):
    if User.query.filter_by(email=email).first():
        return ("Email already registered!")

def validate_uname(uname):
    if User.query.filter_by(name=uname).first():
        return ("Username already taken!")

@app.route('/register', methods=["GET","POST"])
def register():
    errors = []
    if(request.method=="POST"):
        name = request.form.get("name")
        email = request.form.get("email")
        password = request.form.get("password")

        hashed_password = generate_password_hash(password, method='pbkdf2:sha256', salt_length=8)
        
        if(validate_email(email)):
            flash("Email already registered!")
            return redirect(url_for("login"))
        
        if(validate_uname(name)):
            errors.append("Username already taken!")
            return render_template("register.html", errors=errors)

        newUser = User(name, email, hashed_password)

        db.session.add(newUser)
        db.session.commit()

        login_user(newUser)
        return redirect(url_for('secrets'))
    
    return render_template("register.html", errors=errors)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

@app.route('/login', methods=["GET","POST"])
def login():
    if(request.method=="POST"):
        email = request.form.get("email")
        password = request.form.get("password")
        user = db.session.query(User).filter_by(email=email).first()
        
        if(user):
            if(check_password_hash(user.password,password)):
                login_user(user)
                return redirect(url_for("secrets"))
            else:
                flash("Incorrect Password!")
        else:
            flash("User doesn't exist!")

        return redirect(url_for("login"))

    return render_template("login.html")

@app.route('/secrets/', methods=["GET"])
@login_required
def secrets():
    return render_template("secrets.html", name=current_user.name)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for("home"))

@app.route('/download')
@login_required
def download():
    return send_from_directory("static/files","cheat_sheet.pdf")


if __name__ == "__main__":
    app.run(debug=True)
