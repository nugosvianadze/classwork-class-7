from app.library.models import Book, db
from app import create_app
from faker import Faker

fake = Faker('ka_GE')
app = create_app()


books = [
    {'title': 'To Kill a Mockingbird', 'author': 'Harper Lee', 'year': 1960},
    {'title': '1984', 'author': 'George Orwell', 'year': 1949},
    {'title': 'Pride and Prejudice', 'author': 'Jane Austen', 'year': 1813},
    {'title': 'The Great Gatsby', 'author': 'F. Scott Fitzgerald', 'year': 1925},
    {'title': 'The Catcher in the Rye', 'author': 'J.D. Salinger', 'year': 1951},
    {'title': 'The Hobbit', 'author': 'J.R.R. Tolkien', 'year': 1937},
    {'title': 'The Lord of the Rings', 'author': 'J.R.R. Tolkien', 'year': 1954},
    {'title': "Harry Potter and the Sorcerer's Stone", 'author': 'J.K. Rowling', 'year': 1997},
    {'title': 'The Chronicles of Narnia', 'author': 'C.S. Lewis', 'year': 1950},
    {'title': 'Animal Farm', 'author': 'George Orwell', 'year': 1945},
    {'title': 'The Alchemist', 'author': 'Paulo Coelho', 'year': 1988},
    {'title': 'The Da Vinci Code', 'author': 'Dan Brown', 'year': 2003},
    {'title': 'The Book Thief', 'author': 'Markus Zusak', 'year': 2005},
    {'title': 'The Kite Runner', 'author': 'Khaled Hosseini', 'year': 2003},
    {'title': 'The Hunger Games', 'author': 'Suzanne Collins', 'year': 2008},
    {'title': 'The Girl on the Train', 'author': 'Paula Hawkins', 'year': 2015},
    {'title': 'Gone Girl', 'author': 'Gillian Flynn', 'year': 2012},
    {'title': 'The Help', 'author': 'Kathryn Stockett', 'year': 2009},
    {'title': 'The Fault in Our Stars', 'author': 'John Green', 'year': 2012},
    {'title': 'The Martian', 'author': 'Andy Weir', 'year': 2011}
]


def create_books():
    with app.app_context():
        book_list = [Book(title=book['title'], author=book['author'])
                    for book in books]
        db.session.add_all(book_list)
        db.session.commit()


create_books()
