from app.extensions import db
from sqlalchemy import Integer, String, SmallInteger
from sqlalchemy.orm import Mapped, mapped_column


class Book(db.Model):
    __tablename__ = 'books'
    id: Mapped[int] = mapped_column(primary_key=True)
    title: Mapped[str]
    author: Mapped[str]
    reviews = db.relationship('Review', backref='book', lazy='dynamic')

    def __str__(self):
        return self.title


class Review(db.Model):
    __tablename__ = 'reviews'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(String, db.ForeignKey('users.id'))
    book_id: Mapped[int] = mapped_column(String, db.ForeignKey('books.id'))
    name: Mapped[str]
    review: Mapped[str]
