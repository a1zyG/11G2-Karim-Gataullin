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

class Shopping_cart(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    user_id =db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    amount = db.Column(db.Integer, nullable=False)
    user = db.relationship('Users',
                            backref=db.backref('shop_cart', lazy=False))
    item = db.relationship('Items',
                              backref=db.backref('shop_cart', lazy=False))

class Items(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Integer, nullable=False)
    description = db.Column(db.String(80), nullable=False)
    photo = db.Column(db.String(80), nullable=True)



class History_of_orders(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    number = db.Column(db.Integer, nullable=False)
    total = db.Column(db.Integer, nullable=False)
    flag = db.Column(db.Integer, nullable=False)
    date = db.Column(db.String(80), nullable=False)
    user = db.relationship('Users',
                            backref=db.backref('order', lazy=False))

class Order_list(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    order_id = db.Column(db.Integer, db.ForeignKey('history_of_orders.id'), nullable=False)
    item_id = db.Column(db.Integer, db.ForeignKey('items.id'), nullable=False)
    ppi = db.Column(db.Integer, nullable=False)
    count = db.Column(db.Integer, nullable=False)
    order = db.relationship('History_of_orders',
                            backref=db.backref('order_list', lazy=False))
    item = db.relationship('Items',
                              backref=db.backref('order_list', lazy=False))

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=True)
    review = db.Column(db.String(500), nullable=True)

db.create_all()
