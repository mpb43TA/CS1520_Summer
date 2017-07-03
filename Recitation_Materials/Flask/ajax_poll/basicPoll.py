import json
from flask import Flask, render_template, request

app = Flask(__name__)

items = [["FIRST NAME - ", "LAST NAME - ", "FLAVOR"]]
choices = ["vanilla", "chocolate", "stawberry"]

@app.route("/")
def default():
	return render_template("poll.html", items=items, flavors = choices)

@app.route("/new_item", methods=["POST"])
def add():
    if request.form['flavor'] not in choices:   
        choices.append(request.form['flavor'])
    items.append([request.form["first"], request.form["last"], request.form["flavor"]])
    return "OK!"

@app.route("/items")
def get_items():
    return json.dumps({'choices': choices,'results': items})
	
if __name__ == "__main__":
	app.run(debug = True)

