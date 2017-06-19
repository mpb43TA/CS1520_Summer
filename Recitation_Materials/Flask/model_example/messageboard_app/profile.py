from flask import Flask, request, abort, url_for, redirect, session, Blueprint, render_template, jsonify
from model import User, Blogpost, db
import datetime


profile_blueprint = Blueprint('profile', __name__, template_folder = 'templates')
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
	    """
	    TODO: add template form that will allow for posting a new message
	    TODO: add template form that allows for deleting a message of only the current user
	    TODO: add to posts dictionary content related to the post, should be passed from get post method
	    if request.method == "POST":
	        	        

	        return redirect(url_for('profile.profile'))
	    """
	    posts = {}
	    return render_template("curProfile.html", username = username, posts = posts)
	    
	return render_template("otherProfile.html", name=username, posts = posts)

def initialize_user(username):
    return User.query.filter_by(username = username).first()

def delete_post():
    """
    TODO: deletes the post in the model
    """
	
def add_post(user):
    """
    TODO: adds the post to the model
    """

def get_posts():
    """
    TODO: returns posts
    """
        