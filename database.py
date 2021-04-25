from flask_sqlalchemy import SQLAlchemy
import pymysql
from dbinfo import db


class User(db.Model):
    id = db.Column(db.String(80), primary_key=True,unique=True)
    display_name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    #avatar = db.Column(db.String(120),nullable=False,default = default.jpg)
    earth_coins = db.Column(db.Integer(), nullable = False)
    items = db.relationship('Item', backref=db.backref("user"))
    def __repr__(self):
        return f"{self.name},{self.email},{self.earth_coins}"
    def update_earth_coins(self,newamount):
        self.earth_coins = newamount
    #def update_avatar(self,newavatar):
    #   self.newavatar = newavatar
    
    
class Item(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    item_name = db.Column(db.String(20), nullable=False)
    owner_id = db.Column(db.String(255), db.ForeignKey(User.id), nullable=False)
    def __repr__(self):
        return f"{self.item_type},{self.ownerid}"