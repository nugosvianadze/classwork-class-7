from bcrypt import hashpw, gensalt
from flask_login import UserMixin

from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password = mapped_column(String(120))
    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    @staticmethod
    def set_password(password):
        return hashpw(password.encode('utf-8'), gensalt())

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __str__(self):
        return self.username
