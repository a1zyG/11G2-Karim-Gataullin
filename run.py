from flask import *
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object("config")

