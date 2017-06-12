"""
Initial structure from nfarnan github repository cs1520_examples
"""
from flask import Flask, redirect
#call for the bluueprint
from views.login import login_blueprint
from views.profile import profile_blueprint

app = Flask(__name__)
"""
Blue prints of our login (logger and unlogger) and profile (profile) views
"""
app.register_blueprint(login_blueprint)
app.register_blueprint(profile_blueprint)

# by default, direct to login
@app.route("/")
def default():
	return redirect("/login/")

# needed to use sessions
# note that this is a terrible secret key
app.secret_key = "this is a terrible secret key"

if __name__ == "__main__":
    #NOTE DEBUG to Reload after change
    app.run(debug = True)