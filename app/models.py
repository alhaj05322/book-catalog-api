from datetime import datetime, timezone, timedelta
from .extensions import db
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from flask_login import UserMixin
from sqlalchemy import String, DateTime, func


class Base(DeclarativeBase, UserMixin):
    pass

class Book(Base):
    __tablename__ = "book"

    # ID: Unique identifier for each book.
    id: Mapped[int] = mapped_column(primary_key=True)
    # ISBN: A unique identifier for books
    isbn: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)
    # Title: The main name of the book
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    # Author(s): Can be a single author string
    author: Mapped[str] = mapped_column(String(255), nullable=False)
    # Genre/Category: Optional, can be used for filtering
    genre: Mapped[str] = mapped_column(String(100), nullable=True)
    # Published Date: Stores the publication year or full date
    #published_date: Mapped[datetime] = mapped_column(default=datetime.now(timezone.utc))
    published_date: Mapped[datetime] = mapped_column(String(100), nullable=True)
    # Stores the filename or URL of the cover image (e.g., 'covers/book1.jpg')
    cover_image_path: Mapped[str] = mapped_column(String(255), nullable=False)

 # A helpful representation method for debugging
    def __repr__(self):
        return f'<Book "{self.title}" by {self.author}>'
    
    def to_dict(self):
        """Converts the Book object to a JSON-serializable dictionary."""
        return {
            "isbn": self.isbn,
            "title": self.title,
            "author": self.author,
            "genre": self.genre,
            "published_date": self.published_date,
            "cover_image_path": self.cover_image_path
        }
    
class User(Base):
    __tablename__ = "user"

    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100), nullable=False)
    email: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    password: Mapped[str] = mapped_column(String(100), nullable=False, unique=True)

       
    def __repr__(self):
        return f'<Book "{self.name}" by {self.email}>'

