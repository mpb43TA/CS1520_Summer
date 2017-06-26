from flask import Flask, request, abort, url_for, redirect, session, render_template, Blueprint, flash
from profile.model import User
from extensions import db

login_blueprint = Blueprint('login', __name__, template_folder = '../templates')

# by default, direct to login
@login_blueprint.route("/")
def default():
	return redirect("/login/")


@login_blueprint.route("/login/", methods = ["GET", "POST"])
def logger():
    #user logged in?
    if "username" in session:
        return redirect(url_for("profile.profile", username = session["username"]))
    # if not, and the incoming request is via POST try to log them in
    elif request.method == "POST":
        user = User.query.filter_by(username = request.form['user']).first()
        if user != None and user.password == request.form['pass']:
            session['username'] = user.username        
            return redirect(url_for("profile.profile", username=session["username"]))
    # otherwise, offer to log them in
    return render_template("profile/loginPage.html")

@login_blueprint.route("/logout/")
def unlogger():
	# if logged in, log out, otherwise offer to log in
	if "username" in session:
		# note, here were calling the .clear() method for the python dictionary builtin
		session.clear()
		return render_template("profile/logoutPage.html")
	else:
		return redirect(url_for("login.logger"))

"""
    Register New User
"""
@login_blueprint.route("/register/", methods = ["GET", "POST"])
def register():
	# if logged in, redirect to user page
	error = None
	if "username" in session:
		return redirect(url_for("profile.profile"))
	elif request.method == "POST":
	    user = User(request.form['user'], request.form['pass'], 
	                request.form['fname'], request.form['lname'])	    
	    response = db.session.add(user)
	    db.session.commit()
	    print(response)
	    return redirect(url_for("login.logger"))
	return render_template("profile/register.html")
