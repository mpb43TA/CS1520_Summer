from flask import Flask, request, abort, url_for, redirect, session, render_template, Blueprint
from data import users

"""
Blueprint for profile view
"""
profile_blueprint = Blueprint('profile', __name__, template_folder = 'templates')


@profile_blueprint.route("/profile/")
@profile_blueprint.route("/profile/<username>")
def profile(username=None):
	if not username:
		# if no profile specified, either:
		#	* direct logged in users to their profile
		#	* direct unlogged in users to the login page
		if "username" in session:
			return redirect(url_for("profile", username=session["username"]))
		else:
		    #*** need to specify the login blueprint and view name
			return redirect(url_for("login.logger"))
			
	elif username in users:
		# if specified, check to handle users looking up their own profile
		if "username" in session and session["username"] == username:
			return render_template("curProfile.html")
		else:
			return render_template("otherProfile.html", name=username)
			
	else:
		# cant find profile
		abort(404)