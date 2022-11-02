from app import app
from flask import render_template, request, redirect, session
import datetime
import requests
import json
import os

app.secret_key="session_key666"


def get_jaya(pv_list):
    """
    Use JAYA

    Send PV list to JAYA.

    Return JSON from JAYA with readings.
    """
    url_full = "https://beta.hla.triumf.ca/jaya/get"
    data = {'readPvList': pv_list}
    r = requests.post(url_full, json=data)
    jsondata = r.json()
    return jsondata


@app.route("/delete/<dashboard_name>/<pv>")
def delete( dashboard_name,pv):
    """
    Dashboard PV deletion

    Delete PV from dashboard (JSON file) and redirect to dashboard view.
    """
    dash_file = os.path.join("dashboard_files", f"{dashboard_name}.json")
    print(dash_file)
    with open(dash_file, "r") as file_read:
        json_data=json.load(file_read)
        pv_variables=json_data["readPvDict"]
        try:
            pv_variables.pop(pv)
        except:
            return ("Error PV not found")

    with open(dash_file, 'w') as file_write:
        json.dump(json_data, file_write)
    return redirect(f"/view/{dashboard_name}")


@app.route("/", methods=["GET", "POST"])
def index():
    """
    Landing page

    GET: Route user to landing page (index.html)

    POST: Verify password, start user session, redirect user to
          dashboard selection.

    If any errors occur, redirect to error page.
    """
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


@app.route("/dashboard/delete/<dash_name>")
def delete_dash(dash_name):
    """
    Dashboard deletion

    Remove dashboard (JSON file) if it exists.
    """
    if session['user']:
        dash_file = os.path.join("dashboard_files", f"{dash_name}.json")
        if os.path.exists(dash_file):
            os.remove(dash_file)
            return redirect ("/dashboard")


@app.route("/dashboard", methods=["GET", "POST"])
def home():
    """
    Dashboard Selection Route

    GET: Route user to dashboard selection page.

    POST: Use user input to redirect to dashboard view.

    If any errors occur, redirect to error page.
    """
    try:
        if session["user"]:
            if request.method=="GET":
                dashes = []
                dash_path = "dashboard_files"
                files = os.listdir(dash_path)
                for f in files:
                    if ".json" in f:
                        if os.path.isfile(dash_path+'/'+f):
                            dashes.append(os.path.splitext(f)[0])
                return render_template("/public/dash.html", dashes=dashes)

            if request.method=="POST":
                dashboard=request.form.get("dashboard")
                if dashboard==None:
                    return render_template("/public/dash.html")
                else:
                    return redirect(f"/view/{dashboard}")

        return redirect('/error')
    except:
        return redirect('/error')

@app.route("/monitor/<dashboard>", methods=["GET"])
def monitor(dashboard):
    """
    Monitor PVs on dashboard
    """
    try:
        if session['user']:
            dash_file = os.path.join("dashboard_files", f"{dashboard}.json")
            if request.method == "GET":
                # check if json file exists for dashboard, otherwise send default page
                if os.path.exists(dash_file):
                    with open(dash_file, "r") as file_read:
                        json_for_dash = json.load(file_read)
                    pv_list_get_request = []
                    for pv in json_for_dash['readPvDict']:
                        pv_list_get_request.append(pv)
                    updated_readings_from_jaya = get_jaya(pv_list_get_request)
                    return render_template("/public/monitor_dash.html", data=updated_readings_from_jaya, dashboard_name=dashboard)
                return render_template("/public/monitor_dash.html")
        return redirect('/error')
    except:
        return redirect('/error')


@app.route("/view/<dashboard>/<refresh>")
@app.route("/view/<dashboard>", defaults={'refresh': 5}, methods=["GET", "POST"])
def dashboard(dashboard, refresh):
    """
    Dashboard view route

    GET: Route user to dashboard view and update PV readings upon each request.

    POST: Use user input and call JAYA to get PV readings.

    If any errors occur, redirect to error page.
    """
    try:
        if session['user']:
            dash_file = os.path.join("dashboard_files", f"{dashboard}.json")
            if request.method == "GET":
                # check if json file exists for dashboard, otherwise send default page
                if os.path.exists(dash_file):
                    with open(dash_file, "r") as file_read:
                        json_for_dash = json.load(file_read)
                    # pv_list_get_request = []
                    # for pv in json_for_dash['readPvDict']:
                    #     pv_list_get_request.append(pv)
                    # updated_readings_from_jaya = get_jaya(pv_list_get_request)
                    return render_template("/public/edit_dash.html", data=json_for_dash, dashboard_name=dashboard, rate=refresh)
                return render_template("/public/edit_dash.html")
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
                return render_template("public/edit_dash.html", data=json_for_dash, dashboard_name=dashboard, rate=refresh)
        return redirect('/error')
    except:
        return redirect('/error')


@app.route('/create', methods=["GET", "POST"])
def create():
    """
    Dashboard creation route

    GET: Route user to dashboard creation page.

    POST: Use user input (dashboard name) to create new dashboard and redirect
          user to their new dashboard.

    Note: New dashboard results is new JSON file in
          <project_root_directory>/dashboard_files.

    If any errors occur, redirect to error page.
    """
    try:
        if session['user']:
            if request.method == "GET":
                return render_template("/public/create.html")
            if request.method == "POST":
                name = request.form.get("dash-name")
                dash_file = os.path.join("dashboard_files", f"{name}.json")
                now = datetime.datetime.now()
                template_for_dash_files = {"readPvDict": {}, "timestamp": now.strftime("%Y-%m-%d %H:%M:%S")}
                # if dashboard exists, return message, else create dashboard
                if not os.path.exists(dash_file):
                    with open(dash_file, 'w') as file_to_create:
                        file_to_create.write(json.dumps(template_for_dash_files, indent=4))
                    return redirect(f"/view/{name}")
                return redirect(f"/view/{name}")
        return redirect('/error')
    except:
        return redirect('/error')


@app.route('/error')
def error():
    """
    Error page route

    Route user to error page.
    """
    return render_template('/public/error.html')

