from flask import Flask, request, abort, url_for, redirect, session, Blueprint, render_template, jsonify
from profile.model import User, Blogpost
from extensions import db
import datetime


profile_blueprint = Blueprint('profile', __name__, template_folder = '../templates')
@profile_blueprint.route("/profile/", methods = ["GET", "POST"])
@profile_blueprint.route("/profile/<username>", methods = ["GET", "POST"])
def profile(username=None):
	if not username:
		if "username" in session:
			return redirect(url_for('profile.profile', username=session["username"]))
		else:
			return redirect(url_for("login.logger"))
	
	user = initialize_user(username)
	if "username" in session and session["username"] == username:
	    if request.method == "POST":	        
	        if 'delete' in request.form:
	            delete_post()
	        elif 'title' in request.form:
	            reply_post(user)
	        elif 'reply' in request.form:
	            post_to_feed(user)
	        return redirect(url_for('profile.profile'))
	    posts = get_posts()
	    return render_template("profile/curProfile.html", username = username, posts = posts)
	    
	return render_template("profile/otherProfile.html", name=username, posts = posts)

def initialize_user(username):
    return User.query.filter_by(username = username).first()

def reply_post(user):
    """
    TODO: Implement reply to post from db
    """

def delete_post():
    """
    TODO: Implement remove post from db
    """
	
def post_to_feed(user):
    """
    TODO: Implement add post to db
    """

def get_posts():
    """
    TODO: Implement retrieve posts
    """
        