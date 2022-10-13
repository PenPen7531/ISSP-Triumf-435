from app import app
from flask import render_template

@app.route("/")
def index():
    return render_template("public/mobile_index.html")


@app.route("/webpage")
def home():
    return render_template("public/index.html")