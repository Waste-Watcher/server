from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SECRET KEY'] = ''
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.String(80), primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    avatar = db.Column(db.string(120),nullable=False,default = default.jpg)
    earth_coins = db.Column(db.Integer(100), nullable = False)
    def __repr__(self):
        return f"{self.username},{self.email},{self.earth_coins}"
    def update_earth_coins(self,newamount):
        self.earth_coins = newamount
    def update_avatar(self,newavatar):
        self.newavatar = newavatar
    

class Item(db.Model):
    itemid = db.Column(db.String(80), primary_key=True)
    ownerid = db.Column(db.String(80), nullable=False)
    item_type = db.Column(db.String(120), nullable=False)
    def __repr__(self):
        return f"{self.item_type},{self.ownerid}"
