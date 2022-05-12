import sqlalchemy
from flask import *
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


@app.route("/")
def main_p():
    return render_template("main.html")

@app.route("/keyboard")
def prod1():
    return render_template("keyboard.html")

@app.route("/mouse")
def prod2():
    return render_template("mouse.html")

@app.route("/review")
def review():
    return render_template("review.html")


if __name__ == '__main__':    
    app.run(debug=True)
