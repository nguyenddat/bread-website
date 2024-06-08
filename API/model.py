from .api import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class product(db.Model, UserMixin):
    id = db.Column(db.String(10), primary_key = True)
    name = db.Column(db.String(150))
    img = db.Column(db.String(150))
    price = db.Column(db.String(150))
    like = db.Column(db.Integer)