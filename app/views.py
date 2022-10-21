from app import app
from flask import render_template, request, jsonify, redirect, session
import requests
import json
import os

app.secret_key="session_key666"



@app.route("/", methods=["GET", "POST"])
def index():
    try:
        if request.method=="GET":
            session['user']=None
            return render_template("public/index.html")

        if request.method=="POST":
            if request.form.get("password")=="Test":
                session['user']='yes'
                return redirect("/dashboard")
        return redirect('/error')
    except:
        return redirect("/error")


@app.route("/dashboard", methods=["GET", "POST"])
def home():
    try:
        if session["user"]:
            if request.method=="GET":
                return render_template("/public/dash.html")
            if request.method=="POST":
                
                dashboard=request.form.get("dashboard")
                if dashboard==None:
                    return render_template("dash.html")
                else:
                    return redirect(f"/view/{dashboard}")
        return redirect('/error')
    except:
        return render_template('/public/error.html')


@app.route("/view/<dashboard>", methods=["GET", "POST"])
def dashboard(dashboard):
    try:
        if session['user']:
            dash_file = os.path.join("dashboard_files", f"{dashboard}.json")
            if request.method == "GET":
                # check if json file exists for dashboard, otherwise send default page
                if os.path.exists(dash_file):
                    with open(dash_file, "r") as file_read:
                        json_for_dash = json.load(file_read)
                    return render_template("/public/test_dash.html", data=json_for_dash)
                return render_template("/public/test_dash.html")
            if request.method == "POST":
                pv_from_form = request.form.get("pv-input")
                pv_list = []
                pv_list.append(pv_from_form)
                jaya_json = get_jaya(pv_list)
                # write to json file if it does not exist
                if not os.path.exists(dash_file):
                    with open(dash_file, "w") as file_write:
                        file_write.write(json.dumps(jaya_json, indent=4))
                # update json file
                else:
                    with open(dash_file, "r+") as file_update:
                        current_data = json.load(file_update)
                        current_data["readPvDict"][pv_from_form] = jaya_json["readPvDict"][pv_from_form]
                        file_update.seek(0)
                        json.dump(current_data, file_update, indent=4)
                # read from the json file
                with open(dash_file, "r") as file_read:
                    json_for_dash = json.load(file_read)
                return render_template("public/test_dash.html", data=json_for_dash)
        return redirect('/error')
    except:
        return redirect('/error')


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
    try:
        if session['user']:
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
        return redirect('/error')
    except:
        return redirect("/error")

@app.route('/create', methods=["GET", "POST"])
def create():
    try:
        if session['user']:
            if request.method == "GET":
                return render_template("/public/create.html")
            if request.method == "POST":
                pass
        return redirect('/error')
    except:
        return redirect('/error')
  

@app.route('/error')
def error():
    return render_template('/public/error.html')

