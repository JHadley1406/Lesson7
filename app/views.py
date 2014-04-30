from app import app
from flask import render_template

@app.route("/")
@app.route("/index")
def main_page():
	return render_template('main.html')
	
@app.route("/disemvowel")
def disemvoweler():
	return render_template("disemvowel.html")
	
@app.route("/mileage")
def mileage():
	return render_template("mileage.html")