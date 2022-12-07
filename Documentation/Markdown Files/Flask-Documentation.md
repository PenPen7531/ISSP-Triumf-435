# Python Flask Documentation :snake:

## What is Flask

Flask is a web-framework that supplies a backend server to run webpages on browsers. With Flask, we are able to send specific HTML pages based on the URL, redirect URLs, keep cookies, send error messages, specify the methods allowed, and perform specific actions based on the URL input.

## Importing Flask 
Before starting to use Flask, we must download it to our virtual environment, and then we must import the Flask module to our Python script. To download this module, we can use pip. Pip is usually automatically installed if Python is installed on your system. If not, please check your Python installation and update the Python software to the newest. To use pip, we must use the command `pip install <module_name>`. <br> The code to install Flask would be:
```pip install flask```



## App Routing
Flask allows the user send specfic data from the backend to the frontend based on the address or the URL. For example, if we want to give the client a home page when the user puts the URL `www.example_page.com`, we are routing to `/`. Flask interprets request method given, and the route, and provides the specific HTML page that should be sent back to the client. Lets say the client wants another different page to create a new account, they may type in the URL `www.example_page.com/create`, we are trying to route to `/create`. With this route, we can specify another HTML page based on this route. <br>
An example of this is:
```Python
from flask import render_template, request, redirect, session

@app.route("/")
def homepage():
    "This is the route for the homepage"
    return render_template("home.html"), 200

@app.route("/")
def createpage():
    "This is the route for creating a new account"
    return render_template("create.html"), 200
```