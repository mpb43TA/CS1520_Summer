from flask import Flask, render_template, request, session, redirect
from login import login_blueprint
from profile import profile_blueprint
from model import db, User, Blogpost
import os
import datetime


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    db.init_app(app)    
    app.register_blueprint(login_blueprint)
    app.register_blueprint(profile_blueprint)
    app.secret_key = 'terrible secret'
    return app 


def setup_database(app):
    with app.app_context():
        db.create_all()
    
if __name__ == '__main__':
    app = create_app()
    if not os.path.isfile('/database.db'):
      setup_database(app)
    app.run(debug = True)