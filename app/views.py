from app import app
from flask import render_template
from flask import Flask, request, jsonify, render_template, redirect, session

import requests

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

# will have to install pip dependencies again from inside virtual env
# as I added requests
# pip install -r requirements.txt
def get_jaya(pv_list):
    url_full = "https://beta.hla.triumf.ca/jaya/get"
    data = {'readPvList': pv_list}
    r = requests.post(url_full, json=data)
    jsondata = r.json()
    return jsondata

@app.route("/try_this", methods=["GET", "POST"])
def try_this():

    if request.method == "GET":
        return render_template("/public/submit_pv.html")

    # pv_list = [
    #         'IOS:MB:MASSOVERQ2', 'IOS:MB:MASSOVERQ.INPA',
    #         'IOS:XCB1AW:STATON', 'IOS:B1A:POS:STATON',
    #         'IOS:XCB1AW:RDVOL', 'IOS:B1A:POS:RDVOL',
    #         'IOS:PSWXCB1A:STATON', 'MCIS:BIAS0:STATON',
    #         'MCIS:BIAS0:RDVOL', 'IOS:BIAS:STATON',
    #         'IOS:BIAS:RDVOL', 'IOS:FC3:SCALECUR',
    #         'IOS:FC3:STATOFF', 'IOS:FC6:SCALECUR',
    #         'IOS:FC6:STATOFF',
    #         ]

    if request.method == "POST":
        pv_from_form = request.form
        pv_list = []
        pv_list.append(pv_from_form['address'])

        jaya_json = get_jaya(pv_list)

        return jaya_json
