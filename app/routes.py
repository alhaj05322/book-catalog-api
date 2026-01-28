from flask import Blueprint, request, jsonify, flash
from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from .models import Book, User
from .extensions import db, login_manager, bp

# CallBack function: used to reload the user object from the user ID stored in the session
@login_manager.user_loader
def load_user(user_id):
     # Return the User object corresponding to the user ID
    return db.get_or_404(User, user_id)

# Endpoint for user login
@bp.post("/api/login")
def login():
    if request.method == "POST":
        login_credentials = request.get_json()
         # Get user's email
        email = (login_credentials.get("email") or "").strip()
        # Get user's passowrd
        password = login_credentials.get("password") or ""

        if not email:
            return jsonify({"success": False, "message": "Email is required"})
        if not password:
            return jsonify({"success": False, "message": "Password is required"})
        
        # Get the user from the database
        user = db.session.execute(db.select(User).filter_by(email=email)).scalar_onr()
        if not user or not check_password_hash(user.password, password):
            return jsonify({"success": False, "message": f"Invalid email or password {email}"})
        else:
            login_user(user, remember=True)
            return {"success": True,"message": f"User {user.name} logged in"}
            
        

# Endpoint for user registration
@bp.post("/api/register")
def register():
    pass

# Endpoint for user logout
@bp.post("/api/logout")
def logout():
    pass


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

