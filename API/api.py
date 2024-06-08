import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
DB_NAME = 'bread.db'

app = Flask(__name__)
CORS(app, resources={r"*": {"origins": "*"}})
app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
db = SQLAlchemy()
db.init_app(app)
from .model import product
with app.app_context():
    db.create_all()

@app.route('/')
def default():
    return render_template('home.html')

@app.route('/api/get-most-liked-products', methods=['GET'])
@cross_origin()
def get_most_liked_products():
    from .get_most_liked_product import get_most_liked_products
    return get_most_liked_products()
