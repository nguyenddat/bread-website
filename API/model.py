from .api import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class product(db.Model, UserMixin):
    id = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(150))
    img = db.Column(db.String(150))
    price = db.Column(db.String(150))
    like = db.Column(db.Integer)

class BREAD_RECIPES(db.Model, UserMixin):
    id = db.Column(db.String(10), primary_key = True)
    img = db.Column(db.String)
    title = db.Column(db.String(244))
    description = db.Column(db.String)
