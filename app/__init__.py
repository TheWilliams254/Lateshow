# app/__init__.py
from flask import Flask
from flask_migrate import Migrate
from .models import db

migrate = Migrate()

def create_app():
    app = Flask(__name__)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///late_show.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    migrate.init_app(app, db)

    return app
