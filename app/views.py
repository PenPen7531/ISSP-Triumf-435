from app import app
from flask import render_template
from flask import Flask, request, jsonify, render_template, redirect, session

@app.route("/", methods=["GET", "POST"])
def index():
    print(request.form.get("password"))
    if request.method=="GET":
        return render_template("public/index.html")

    if request.method=="POST":
        if request.form.get("password")=="Test":
            return redirect("/dashboard")
    return redirect("/error")

@app.route("/dashboard", methods=["GET", "POST"])
def home():
    if request.method=="GET":
        return render_template("public/dash.html")
    if request.method=="POST":
        
        dashboard=request.form.get("dashboard")
        if dashboard==None:
            return render_template("public/dash.html")
        else:
            return redirect(f"/view/{dashboard}")


@app.route("/view/<dashboard>", methods=["GET"])
def dashboard(dashboard):
    if dashboard=="test":
        return render_template("/public/test_dash.html")
    
