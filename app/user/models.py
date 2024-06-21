from flask_login import UserMixin

from app.extensions import db
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column


class User(db.Model):
    __tablename__ = 'users'
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str]
    email: Mapped[str]
    password: Mapped[str]
    reviews = db.relationship('Review', backref='user', lazy='dynamic')

    def __str__(self):
        return self.username
