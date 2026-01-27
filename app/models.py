import datetime
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
    isbn: Mapped[str] = mapped_column(String(13), nullable=False, unique=True)
    # Title: The main name of the book
    title: Mapped[str] = mapped_column(String(100), nullable=False)
    # Author(s): Can be a single author string
    author: Mapped[str] = mapped_column(String(100), nullable=False)
    # Genre/Category: Optional, can be used for filtering
    genre: Mapped[str] = mapped_column(String(50), nullable=True)
    # Published Date: Stores the publication year or full date
    published_date: Mapped[datetime.datetime] = mapped_column(DateTime(datetime=True), server_default=func.now())
    # Stores the filename or URL of the cover image (e.g., 'covers/book1.jpg')
    cover_image_path: Mapped[str] = mapped_column(String(255), nullable=False)

    # A helpful representation method for debugging
    def __repr__(self):
        return f'<Book "{self.title}" by {self.author}>'

