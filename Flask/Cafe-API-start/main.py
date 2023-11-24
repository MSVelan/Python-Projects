from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy
import os, random

app = Flask(__name__)

filePath = os.path.join(os.path.abspath(os.path.dirname(__file__)), "cafes.db")

##Connect to Database


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+filePath
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)


##Cafe TABLE Configuration
class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def __init__(self, name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price):
        self.name = name
        self.map_url = map_url
        self.img_url = img_url
        self.location = location
        self.seats = seats
        self.has_toilet = has_toilet
        self.has_wifi = has_wifi
        self.has_sockets = has_sockets
        self.can_take_calls = can_take_calls
        self.coffee_price = coffee_price

    def obj_to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "map_url": self.map_url,
            "img_url": self.img_url,
            "location": self.location,
            "seats": self.seats,
            "has_toilet": self.has_toilet,
            "has_wifi": self.has_wifi,
            "has_sockets": self.has_sockets,
            "can_take_calls": self.can_take_calls,
            "coffee_price": self.coffee_price
        }
    def obj_to_json(self):
        return jsonify(Cafe=self.obj_to_dict())

with app.app_context():
    db.create_all()

def dict_helper(objlist):
    result = [item.obj_to_dict() for item in objlist]
    return result

@app.route("/")
def home():
    return render_template("index.html")
    
@app.route("/random")
def randomCafe():
    cafes = Cafe.query.all()
    n = db.session.query(Cafe).count()
    CafeId = random.randint(1,n)
    cafe = Cafe.query.get(CafeId)
    print(cafe)
    return cafe.obj_to_json()

@app.route("/all")
def allCafes():
    cafes = Cafe.query.all()
    return dict_helper(cafes)

@app.route("/search")
def searchCafe():
    location = request.args["loc"]
    cafe = Cafe.query.filter_by(location=location).all()
    if(cafe==[]):
        return jsonify(error={
            "Not found": "Sorry, we don't have a cafe at that location."
        })
    else:
        if(len(cafe)==1):
            return cafe.obj_to_json()
        else:
            return dict_helper(cafe)

@app.route("/add", methods=["POST"])
def addCafe():
    name = request.form.get("name")
    map_url = request.form.get("map_url")
    img_url = request.form.get("img_url")
    location = request.form.get("location",default="London")
    seats = request.form.get("seats")
    has_toilet = bool(request.form.get("has_toilet",default=False))
    has_wifi = bool(request.form.get("has_wifi",default=False))
    has_sockets = bool(request.form.get("has_sockets",default=False))
    can_take_calls = bool(request.form.get("can_take_calls",default=False))
    coffee_price = request.form.get("coffee_price")

    new_cafe = Cafe(name, map_url, img_url, location, seats, has_toilet, has_wifi, has_sockets, can_take_calls, coffee_price)

    db.session.add(new_cafe)
    db.session.commit()

    return jsonify(response={
        "success": "Successfully added the new cafe."
    })

@app.route("/update-price/<int:id>", methods=["PATCH"])
def updatePrice(id):
    cafe = Cafe.query.get(id)
    if(cafe is None):
        return jsonify(error={
            "Not Found": "Sorry a cafe with that id was not found in the database."
        }),404
    cafe.coffee_price = request.args["new_price"]

    db.session.commit()
    return jsonify(success="Successfully updated the price."),200

@app.route("/report-closed/<int:id>", methods=["DELETE"])
def deleteCafe(id):
    APIkey = "TopSecretAPIKey"
    key = request.args.get("api-key")
    if(APIkey!=key):
        return jsonify(error="Sorry, that's not allowed. Make sure you have the correct api_key."),403
    cafe = Cafe.query.get(id)
    if(cafe is None):
        return jsonify(error={
            "Not Found":"Sorry a cafe with that id was not found in the database"
        }),404
    db.session.delete(cafe)
    db.session.commit()

    return jsonify(success="Cafe with that id is closed."),200
    
## HTTP GET - Read Record

## HTTP POST - Create Record

## HTTP PUT/PATCH - Update Record

## HTTP DELETE - Delete Record


if __name__ == '__main__':
    app.run(debug=True)

