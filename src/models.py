# WARNING: NOT TESTED
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class User(db.model):
    username = db.Column(db.String(255), nullable=False, primary_key=True, unique=True)
    email = db.Column(db.String(255), nullable=False, unique=True)
    name = db.Column(db.String(255), nullable=False)
    password = db.Column(db.String(255), nullable=False)