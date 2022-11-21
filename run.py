from flask import Flask, render_template, request, jsonify, url_for, session, redirect
import math, requests, os, sys, datetime

import json
#from apex import mod_apex
#from lib import olisArray, olisPVs, olisHeaders, ebisArray, ebisPVs, \
    #get_homepage_text, get_olis_html

#from accpy import schedule

####### REGISTER APP ##########
app = Flask(__name__)

app.secret_key="session_key666"
# app.register_blueprint(mod_apex)
# settings = {
#     'title': 'High Level Applications',
#     'app_name': 'HLA',
#     'gitlab_url':'https://gitlab.triumf.ca/hla/high-level-apps'
# }

####### ROUTING ##########
# @app.route('/', methods = ['GET'])
# def landing():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()
#     pageText = get_homepage_text()
#     return render_template('home.html', header_settings=settings, \
#         navbar_left=navbar, pageTextDict=pageText)

@app.route("/", methods=["GET", "POST"])
def index():
    """
    Landing page

    GET: Route user to landing page (index.html)

    POST: Verify password, start user session, redirect user to
          dashboard selection.

    If any errors occur, redirect to error page.
    """
    # return render_template('/index.html')
    try:
        if request.method=="GET":
            session['user']=None
            return render_template("/index.html")

        if request.method=="POST":
            if request.form.get("password")=="Test":
                session['user']='yes'
                return redirect("/dashboard")
        return redirect('/error')
    except:
        return redirect("/error")


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
                return render_template("/dash.html", dashes=dashes)

            if request.method=="POST":
                dashboard=request.form.get("dashboard")
                if dashboard==None:
                    return render_template("/dash.html")
                else:
                    return redirect(f"/monitor/{dashboard}")

        return redirect('/error')

    except:
        return redirect('/error')


# @app.route('/tuning', methods = ['GET'])
# def tuning():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()
#     return render_template('tuning.html', header_settings=settings, \
#         navbar_left=navbar)


# @app.route('/developers', methods = ['GET'])
# def developers():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()

#     return render_template('developers.html', header_settings=settings, \
#         navbar_left=navbar)


# @app.route('/CSDs', methods = ['GET'])
# def CS_distros():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()

#     return render_template('CSDs.html', header_settings=settings, \
#         navbar_left=navbar)


# @app.route('/olis', methods = ['GET'])
# def olis():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()

#     return render_template('olis.html', header_settings=settings, \
#         navbar_left=navbar, tableArray=olisArray, PVs=olisPVs, \
#         tableHeaders=olisHeaders)


# @app.route('/olis-summary', methods = ['GET'])
# def olis_summary():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()

#     return render_template('olis-summary.html', header_settings=settings, \
#         navbar_left=navbar)


# @app.route('/olis-data', methods = ['GET'])
# def olis_data():
#     return get_olis_html() 


# @app.route('/ebis', methods = ['GET'])
# def ebis():
#     settings['app_url'] = url_for('landing')
#     navbar = make_navbar()

#     return render_template('ebis.html', header_settings=settings, \
#         navbar_left=navbar, tableArray=ebisArray, PVs=ebisPVs)


# @app.route('/get_schedule', methods = ['GET'])
# def get_schedule():
#     schedule_data = schedule.get_current_shift()
#     return jsonify(schedule_data)


# ##############################################
# ### ISAC-2 Linac routing
# ##############################################

# @app.route('/isac2linac')
# def isac2_home():
#     settings['title'] = 'ISAC-II Linac & Beamlines'
#     settings['app_name'] = 'ISAC-II Linac & Beamlines'
#     settings['app_url'] = url_for('isac2_home')
#     navbar = make_isac_2_navbar()
#     return render_template('isac2_home.html', header_settings=settings,
#         navbar_left=navbar)


# @app.route('/isac2linac/documentation')
# def references():
#     settings['title'] = 'ISAC-II Linac & Beamlines'
#     settings['app_name'] = 'ISAC-II Linac & Beamlines'
#     settings['app_url'] = url_for('isac2_home')
#     navbar = make_isac_2_navbar()
#     return render_template('isac2_documentation.html', header_settings=settings, 
#         navbar_left=navbar)


# @app.route('/isac2linac/drawings')
# def drawings():
#     settings['title'] = 'ISAC-II Linac & Beamlines'
#     settings['app_name'] = 'ISAC-II Linac & Beamlines'
#     settings['app_url'] = url_for('isac2_home')
#     navbar = make_isac_2_navbar()
#     return render_template('isac2_design_drawings.html', header_settings=settings, 
#         navbar_left=navbar)


# @app.route('/isac2linac/gallery')
# def gallery():
#     settings['title'] = 'ISAC-II Linac & Beamlines'
#     settings['app_name'] = 'ISAC-II Linac & Beamlines'
#     settings['app_url'] = url_for('isac2_home')
#     navbar = make_isac_2_navbar()
#     return render_template('isac2_gallery.html', header_settings=settings, 
#         navbar_left=navbar)






# ######################

# def make_navbar():
#     link1 = {'text':'Homepage', 'url': url_for('landing')}
#     link2 = {'text':'OLIS', 'url': url_for('olis')}
#     link3 = {'text':'EBIS', 'url': url_for('ebis')}
#     dropdown_links = [link1, link2, link3]
#     navbar = [{'type':'dropdown', 'text':'Other Pages','links':dropdown_links}]
#     return navbar


# def make_isac_2_navbar():
#     link11 = {'text':'Design Drawings', 'url': url_for('drawings')}
#     link12 = {'text':'Documentation', 'url': url_for('references')}
#     link13 = {'text':'Gallery', 'url': url_for('gallery')}

#     info_links = [link11, link12, link13]
#     navbar = [{'type':'dropdown','text':'Info','links':info_links}]
#     return navbar




######################### BCIT FLASK APPLICATION ISSP




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


@app.route("/dashboard/rename/<dname>", methods=['GET', 'POST'])
def rename_dash(dname):
    """
    Rename Dashboard

    Use OS import to rename JSON file of dashboard.
    """
    if session['user']:
        if request.method == 'GET':
            return render_template('/rename.html', dname=dname)
        if request.method == 'POST':
            dash_file = os.path.join("dashboard_files", f"{dname}.json")
            rename = request.form.get('rename')
            if rename=="":
                return render_template("/rename.html", error=True, dname = dname)
            new_name = os.path.join("dashboard_files", f'{rename}.json')
            if os.path.exists(dash_file):
                os.rename(dash_file, new_name)
                return redirect ('/dashboard')



@app.route("/monitor/<dashboard>/<refresh>")
@app.route("/monitor/<dashboard>", defaults={'refresh': 5}, methods=["GET", "POST"])
def monitor(dashboard, refresh):
    """
    Monitor PVs on dashboard - Refresh every 5 seconds

    ToDo: round PV readings
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
                    for pv in updated_readings_from_jaya['readPvDict']:
                        if isinstance(updated_readings_from_jaya['readPvDict'][pv], str) \
                                and not '[' in updated_readings_from_jaya['readPvDict'][pv] \
                                and not "\"" in updated_readings_from_jaya['readPvDict'][pv]:
                            updated_readings_from_jaya['readPvDict'].update({pv : f"{float(updated_readings_from_jaya['readPvDict'][pv]):.4f}"})
                    return render_template("/monitor_dash.html", data=updated_readings_from_jaya, dashboard_name=dashboard, rate=refresh)
                return render_template("/monitor_dash.html")
        #return redirect('/error')
        return "Fail get"
    except:
        #return redirect('/error')
        return "Fail try"

@app.route("/view/<dashboard>", methods=["GET", "POST"])
def dashboard(dashboard):
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
                    return render_template("/edit_dash.html", data=json_for_dash, dashboard_name=dashboard)
                return render_template("/edit_dash.html")
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
                return render_template("/edit_dash.html", data=json_for_dash, dashboard_name=dashboard)
       
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
                return render_template("/create.html")
            if request.method == "POST":
                name = request.form.get("dash-name")
                if name == "":
                    return render_template("/create.html", error=True)
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
    return render_template('/error.html')



if __name__ == '__main__':
    app.config['DEBUG'] = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    if os.environ.get('WERKZEUG_RUN_MAIN') == 'true':
       print('################### Restarting @ {} ###################'.format(
           datetime.datetime.utcnow()))    
    app.run(host='0.0.0.0', port=4994)

