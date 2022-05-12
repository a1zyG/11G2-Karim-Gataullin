import sqlalchemy
from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)

@app.route("/")
def main_page():
    return render_template("main.html")

@app.route("/2.html")
def katalog():
    return render_template("2.html")



@app.route("/keyboard.html")
def prod1():
    return render_template("keyboard.html")

@app.route("/mouse.html")
def prod2():
    return render_template("mouse.html")

@app.route("/review.html")
def review():
    return render_template("review.html")

  
app.run()
