# Library of functions for HLA homepage application
import json, os, sys, requests, datetime
from lxml import etree
from io import StringIO, BytesIO

####### ENVIRONMENT VARIABLES ##########
def check_and_get_env(env_var_name):
    env_var = os.getenv(env_var_name)
    if env_var is None:
        sys.exit(env_var_name + " must be defined in environment variables")
    return env_var

app_dir = check_and_get_env('APPCODEDIR')
config_dir = os.path.join(app_dir, 'config')

olisArray = []
olisHeaders = []

json_file = os.path.join(config_dir, 'olis.json')
with open(json_file) as f:
    olisDict = json.load(f)
    olisArray = olisDict["tabledata"]
    olisHeaders = olisDict["headers"]

olisPVs = []
for item in olisArray:
	for pvDict in item["table"]:
		if 'pv' in pvDict.keys():
			olisPVs.append(pvDict['pv'])

for item in olisHeaders:
	if 'pv' in item.keys():
		olisPVs.append(item['pv'])

ebisArray = []
ebisHeaders = []

json_file = os.path.join(config_dir, 'ebis.json')
with open(json_file) as f:
    ebisDict = json.load(f)
    ebisArray = ebisDict["tabledata"]
    ebisHeaders = ebisDict["headers"]

ebisPVs = []
for item in ebisArray:
    for pvDict in item["table"]:
        if 'pv' in pvDict.keys():
            ebisPVs.append(pvDict['pv'])

for item in ebisHeaders:
    if 'pv' in item.keys():
        ebisPVs.append(item['pv'])


def get_homepage_text():
    json_file = os.path.join(config_dir, 'our_apps.json')
    with open(json_file) as f:
        our_appsDict = json.load(f)
    return our_appsDict
    

def get_jaya(readPvList):
    url_full = "https://beta.hla.triumf.ca/jaya/get"
    data = {'readPvList': readPvList}
    r = requests.post(url_full, json=data)
    jsondata = r.json()
    return jsondata['readPvDict']


def get_olis_html():
    pvDict = {'mq':'IOS:MB:MASSOVERQ2', 'bias_sel':'IOS:MB:MASSOVERQ.INPA',
                'xcb1aw_on':'IOS:XCB1AW:STATON', 'b1a_on':'IOS:B1A:POS:STATON',
                'xcb1aw_vol':'IOS:XCB1AW:RDVOL', 'b1a_vol':'IOS:B1A:POS:RDVOL',
                'xcb1_pol': 'IOS:PSWXCB1A:STATON',
                'mcis_bias_stat': 'MCIS:BIAS0:STATON', 'mcis_bias_vol': 'MCIS:BIAS0:RDVOL',
                'mws_bias_stat': 'IOS:BIAS:STATON', 'mws_bias_vol': 'IOS:BIAS:RDVOL',
                'fc3_curr':'IOS:FC3:SCALECUR', 'fc3_in':'IOS:FC3:STATOFF', 
                'fc6_curr':'IOS:FC6:SCALECUR', 'fc6_in':'IOS:FC6:STATOFF', 
    }
    pvList = list(pvDict.values())
    jayaData = get_jaya(pvList)
    mass = '87'
    element = 'Rb'
    charge = '1'

    bias_status = jayaData[ pvDict['mws_bias_stat'] ] or jayaData[ pvDict['mcis_bias_stat'] ]
    on_status = jayaData[ pvDict['xcb1aw_on'] ] and jayaData[ pvDict['b1a_on'] ]
   # print( type(jayaData[ pvDict['xcb1aw_vol'] ] ))
   # print( type(jayaData[ pvDict['b1a_vol'] ]))
    vol_status = ( float(jayaData[ pvDict['xcb1aw_vol'] ]) > 400.0 ) and ( float(jayaData[ pvDict['b1a_vol'] ]) > 500.0    )

    if bias_status:
        if on_status and vol_status:
            if float(jayaData[ pvDict['xcb1_pol'] ]) > 0.5:
                source = 'SIS Online' # (Surface Ion Source) 
            else:
                source = 'MWS Online' # (Microwave Source) 
        else:
            source = 'MCIS Online' # (Multi-charge Ion Source) 
    else:
        source = 'OLIS Offline'

    output_html = '<div class="col-6">'
    output_html += '<table class="table table-striped">'
    output_html += '<thead><tr>'
    output_html += '<th><h4>OLIS STATUS</h4></th>'
    output_html += '<th>'
    output_html += '<h4>'+source+'</h4>'
    output_html += '</th></tr></thead>'

    if source not in ['OLIS Offline']:
        output_html += '<tbody>'
        output_html += '<tr><td>Beam (expert input)</td><td>'+ str(mass)+element+str(charge) + '+</td></tr>'
        output_html += '<tr><td>OLIS dipole M/Q</td><td>'+ str(round(float(jayaData[ pvDict['mq'] ]),2)) + '</td></tr>'

        if 'MCIS' in source:
            output_html += '<tr><td>MCIS:BIAS [V]</td><td>'+ str(round(float(jayaData[ pvDict['mcis_bias_vol'] ]),1)) + '</td></tr>'
        else:
            output_html += '<tr><td>IOS:BIAS [V]</td><td>'+ str(round(float(jayaData[ pvDict['mws_bias_vol'] ]),1)) + '</td></tr>'

        if jayaData[ pvDict['fc3_in'] ] and ( float(jayaData[ pvDict['fc3_curr'] ]) > 1e-11):
            output_html += '<tr><td>Beam on IOS:FC3 [A]</td><td>'+ '{:0.3e}'.format(float(jayaData[ pvDict['fc3_curr'] ])) + '</td></tr>'
        elif jayaData[ pvDict['fc6_in'] ] and ( float(jayaData[ pvDict['fc6_curr'] ]) > 1e-11):
            output_html += '<tr><td>Beam on IOS:FC6 [A]</td><td>'+ '{:0.3e}'.format(float(jayaData[ pvDict['fc6_curr'] ])) + '</td></tr>'
        output_html += '</tbody>'

    output_html += '</table>'

    output_html += 'Status above was as of ' + str(datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") ) + '<br/>'
    output_html += 'Go <a href="https://beta.hla.triumf.ca/high-level-apps/olis" target="_blank">'
    output_html += 'here</a> for up-to-date OLIS status and details.'
    return(output_html)
