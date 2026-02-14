from flask import Blueprint, request, jsonify, flash, abort
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from .models import Book, User
from .extensions import db, login_manager
from flask import Blueprint
from sqlalchemy import select
import json
import re

bp = Blueprint("main", __name__)

# CallBack function: used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
     # Return the User object corresponding to the user ID
    return db.get_or_404(User, user_id)

# Endpoint for user login
@bp.post("/api/auth/login")
def login():
    if request.method == "POST":
        login_credentials = request.get_json()
         # Get user's email
        email = (login_credentials.get("email") or "").strip()
        # Get user's passowrd
        password = login_credentials.get("password") or ""

        if not email:
            return jsonify({"success": False, "message": "Email is required"}), 401
        if not password:
            return jsonify({"success": False, "message": "Password is required"}), 401
        
        # Get the user from the database
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_one()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"success": False, "message": f"Invalid email or password {email}"}), 401
        else:
            login_user(user, remember=True)
            return jsonify({"success": True,"message": f"User {user.name} logged in"}), 200
            
        

# Endpoint for user registration
@bp.post("/api/auth/register")
def register():
    if request.method == "POST":
        # Fetch user's data from request
        user_data = request.get_json()
        name = (user_data.get("name") or "").strip()
        email = (user_data.get("email") or "").strip()
        password = user_data.get("password") or ""
        confirm_password = user_data.get("confirm") or ""

        # Validate user's data befor store it in database
        if not(3 <= len(name) <= 80):
            return jsonify({"success": False, "message": "User name must be between 3 and 80 chars"})
        if not re.match(r"^[^@\s]+@[^@\s]+\.[^@\s]+$", email):
            return jsonify({"success": False,"message": "Invalid email"})
        if len(password ) < 8:
            return jsonify({"success": False,"message": "Passord need to be atleast 8 chars"})
        #Check if passord and confirm passord are matched
        if password != confirm_password:
            return jsonify({"success": False,"message": "Passowrd do not match"})
        
        # If data is valid ad user to the database
        try:
            password_hash = generate_password_hash(password)
            user = User(name = name, email = email, password = password_hash)
            db.session.add(user)
            db.session.commit()
            return jsonify({"success": True, "message": f"User : {name} is added to the database successfully"}), 201
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred during registration: {e}")
            flash("An unexpected error occurred. Please try again later.", "danger")


# Endpoint for user logout
@bp.post("/api/auth/logout")
@login_required
def logout():
    logout_user()
    return jsonify({"success": True, "message": "User logged out"}), 200


# Endpoint to retrieve all books.
@bp.get("/api/books")
@login_required
def get_books():
    if current_user.is_authenticated:
        stmt = select(Book)
        result = db.session.execute(stmt).scalars().all()
        # Convert the list of model objects into a list of dictionaries
        books_list = [book.to_dict() for book in result]
        return books_list

# Endpoint to add a new book.
@bp.post("/api/books")
@login_required
def add_books():
    if current_user.is_authenticated:
        book_data = request.get_json()
        isbn = (book_data.get("isbn") or "").strip()
        title = (book_data.get("title") or "").strip()
        author = (book_data.get("author") or "").strip()
        genre = (book_data.get("gener") or "").strip()
        published_date = (book_data.get("published_date") or "").strip()
        cover_image_path = (book_data.get("cover_image_path") or "").strip()

        if not isbn:
            return jsonify({"success": False, "message": "ISBN is required"}), 401
        if not title:
            return jsonify({"success": False, "message": "Title is required"}), 401
        if not author:
            return jsonify({"success": False, "message": "Author is required"}), 401
        if not cover_image_path:
            return jsonify({"success": False, "message": "URL is required"}), 401
    
        try:
            book = Book(isbn=isbn, title=title, author=author, genre=genre, published_date=published_date,cover_image_path=cover_image_path)
            db.session.add(book)
            db.session.commit()
            return jsonify({"success": True, "message": f"User : {title} is added to the database successfully"}), 201
        except Exception as e:
            db.session.rollback()
            print(f"An error occurred during adding a book: {e}")
            flash("An unexpected error occurred. Please try again later.", "danger")
            return jsonify({"success": False,"message": f"Could not add:  {title}"}), 500
    



    
   

# Endpoint to update an existing book.
@bp.put("/api/books/<int:book_id>")
def update_book(book_id):
    book = db.session.get(Book, book_id)
    # If the book is not found, return a 404 error
    if book is None:
        abort(404, description="Book not found")

    # Ensure the request contains JSON data
    if not request.json:
        abort(400, description="Invalid request format, must be JSON")

    # Extract data from the request and update book attributes
    # The 'or book.title' part ensures that if a field is missing in the request,
    # the existing value is kept (a common pattern for PATCH, but also useful for PUT)
    book.isbn = request.json.get('isbn', book.isbn)
    book.title = request.json.get('title', book.title)
    book.author = request.json.get('author', book.author)
    book.genre = request.json.get('genre', book.genre)
    book.published_date = request.json.get('published_date', book.published_date)
    book.cover_image_path = request.json.get('cover_image_path', book.cover_image_path)
    # Commit the changes to the database
    try:
        db.session.commit()
        return jsonify({"success": True,'message': 'Book updated successfully', 'book_id': book.id}), 200
    except Exception as e:
        db.session.rollback()
        abort(500, description=f"An error occurred: {str(e)}")

# Endpoint to delete a book.
@bp.delete("/api/books/<int:book_id>")
def delete_book(book_id):
    pass

