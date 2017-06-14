from flask import Flask, request, abort, url_for, redirect, session, render_template, Blueprint
from data import users

"""
***Blueprint for login view
"""
#***
login_blueprint = Blueprint('login', __name__, template_folder = 'templates')

#***
@login_blueprint.route("/login/", methods=["GET", "POST"])
def logger():
	# first check if the user is already logged in
	if "username" in session:
		return redirect(url_for("profile.profile", username=session["username"]))

	# if not, and the incoming request is via POST try to log them in
	elif request.method == "POST":
		if request.form["user"] in users and users[request.form["user"]] == request.form["pass"]:
			session["username"] = request.form["user"]
			#*** need to specify the blueprint name and view
			return redirect(url_for("profile.profile", username=session["username"]))

	# if all else fails, offer to log them in
	return render_template("loginPage.html")
	
@login_blueprint.route("/logout/")
def unlogger():
	# if logged in, log out, otherwise offer to log in
	if "username" in session:
		# note, here were calling the .clear() method for the python dictionary builtin
		session.clear()
		return render_template("logoutPage.html")
	else:
		return redirect(url_for("logger"))