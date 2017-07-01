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
	            post_to_feed(user)
	        elif 'reply' in request.form:
	            reply_post(user)
	        return redirect(url_for('profile.profile'))
	    posts = get_posts()
	    return render_template("profile/curProfile.html", username = username, posts = posts)
	    
	return render_template("profile/otherProfile.html", name=username, posts = posts)

def initialize_user(username):
    return User.query.filter_by(username = username).first()

def reply_post(user):
    if(request.form['body'] != ''):
        new_post = Blogpost(user.id,
                            request.form['body'],
                            datetime.datetime.now())
        new_post.set_parentId(int(request.form['id']))
        db.session.add(new_post)
        db.session.commit()

def delete_post():
    id = int(request.form['id'])
    Blogpost.query.filter_by(id = id).delete()
    db.session.commit()
	
def post_to_feed(user):
    if(request.form["title"] != '' and request.form['body'] != ''):
        new_post = Blogpost(user.id, 
                            request.form['body'], 
                            datetime.datetime.now(),
                            title = request.form['title'])
        db.session.add(new_post)
        db.session.commit()

def get_posts():
    raw_posts = Blogpost.query.all()
    posts = {}
    
    for post in raw_posts:
        posts[post.id] = {}
        posts[post.id]['content'] = post.serialize()
        if post.parentId ==-1:
            posts[post.id]['root'] = True
        else:
            posts[post.id]['root'] = False
        instances = Blogpost.query.filter_by(parentId = post.id).all()
        if(len(instances)>0):
            children = []
            for inst in instances:
                children.append(inst.id)
            posts[post.id]['children'] = children
    return posts
        