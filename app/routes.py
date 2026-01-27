from flask import Blueprint, request, jsonify, flash
from .models import Book
from .extensions import db, login_manager, bp

# Endpoint to retrieve all books.
@bp.get("/api/books")
def get_books():
    pass

# Endpoint to add a new book.
@bp.post("/api/books")
def add_books():
    pass

# Endpoint to update an existing book.
@bp.put("/api/books/<int: book_id>")
def update_book(book_id):
    pass

# Endpoint to delete a book.
bp.delete("/api/books<int: book_id>")
def delete_book(book_id):
    pass

