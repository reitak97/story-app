from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class Story(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(150))
    image = db.Column(db.String(300))
    content = db.Column(db.String(300))
    date_created = db.Column(db.DateTime (timezone=True), default=func.now())
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150))
    stories = db.relationship('Story')

