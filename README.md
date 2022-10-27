# ISSP-Triumf-435 HLA Documentation
## Authors
    Luke Birol
    Jake Martin
    Jeffrey Wang

## Introduction

### Who we are
We are a project group from BCIT that has been assigned to complete a project. This project was given to us in September of 2022. The project was to create a webpage that will display partical accelerator data in real-time. 

### What is the purpose of the webpage
The purpose of creating this webpage was to allow scientists, data analysis, or anyone working at TRIUMF to access real-time data to quick and easily get updates. This webpage will be a read-only webpage, cutting the risk of anyone accessing or having control of any machine. This will also reduce the troubles of accessing EPICS through a VPN and using MFA. With this webpage, we are able to quickly read and see the status of multiple devices. 

### What will this documentation tell you
This documentation will contain information that will help anyone to modify this webpage. We will go through the basics of how this webpage was created, what languages were used, some resources that may help others to understand the code better. We will explain how multiple components and files connect and interact with each other to display data. 

## Quick Resources

### Python

### JavaScript

### HTML

### CSS

### Python Flask
Flask Installation
    https://flask.palletsprojects.com/en/2.2.x/installation/


Routing 
    https://flask.palletsprojects.com/en/2.2.x/quickstart/#routing


Rendering Templates and Pages
    https://flask.palletsprojects.com/en/2.2.x/quickstart/#rendering-templates


## Setup Development Environment:

### LINUX:  
    cd ISSP-Triumf-435;
    python3 -m venv venv;
    source venv/bin/activate;
    pip3 install -r requirements.txt;
    

### WINDOWS: 
    cd ISSP-Triumf-435;
    python -m venv venv; 
    ./venv/bin/activate;
    pip install -r requirements.txt;



\
\
Start Flask app:

    flask run;

