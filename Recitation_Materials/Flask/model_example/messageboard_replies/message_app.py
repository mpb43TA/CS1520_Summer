from flask import Flask, render_template, request, session, redirect
from extensions import db
import os
import datetime
from profile import views


def create_app():
    app = Flask(__name__)
    app.config['DEBUG'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
    db.init_app(app)    
    app.register_blueprint(views.login.login_blueprint)
    app.register_blueprint(views.profile.profile_blueprint)
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