from flask import Flask
from .config import Config
from .extensions import db, bp, login_manager
import os


def create_app(config_class: type = Config):


    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(config_class)

    #create the instnce folder
    os.makedirs(app.instance_path,exist_ok=True)

    #Initialize the database
    db.init_app(app)

    #If user not logged in redirect to login page
    login_manager.login_view="login"
    login_manager.init_app(app)
    
    # Register the blueprint
    app.register_blueprint(bp)


    return app


