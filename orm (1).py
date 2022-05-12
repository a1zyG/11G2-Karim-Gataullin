from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///Base.db'
db = SQLAlchemy(app)



class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    login = db.Column(db.String(80), nullable=True)
    password = db.Column(db.String(80), nullable=True)
    payment = db.Column(db.String(80), nullable=True)
    sign_up_date = db.Column(db.String(80), nullable=True)
    birthday = db.Column(db.String(80), nullable=True)



class Products(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    amount = db.Column(db.Integer, nullable=True)
    price = db.Column(db.Integer, nullable=True)
    discription = db.Column(db.String(80), nullable=True)
    picture_url = db.Column(db.String(80), nullable=True)

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Catalog_id = db.Column(db.Integer, db.ForeignKey('catalog.id'), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    photo = db.Column(db.String(80), nullable=True)
    Catalog = db.relationship('catalog',
                               backref=db.backref('item', lazy=False))

class history_of_orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    users_id = db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(80), nullable=False)

db.create_all()
