# JSON
JSON or JavaScript Object Notation, is a lightweight way to send and transfer data over the web. It is formatted in a way where each chunk of data is stored and retrieved in a key and value pair. The key acts like a title or name of the object, and the value will be the actual data of the object. This document will contain a breif introduction into JSON, how we use JSON in our project, and how to modify and save JSON data with Python.

<br>

We use JSON to store data we want to modify and easily access, this includes dahsboard names and their saved process variables. We can also consider JSON to be very similar to Python Dictionaries or dictionaries in most coding languages, using a key and value pair to save and access values. 

# Using JSON with Python
In our project, we use JSON to store data which will then be access by Python. To do this, we import the JSON module like this:
```Python
import json
```
<br>
This allows json functions to be used within our Python script. We can use functions such as dump, which will dump our dictionary into a JSON file. 
<br>
In addition, you should also import the module os, which will allow us to delete JSON files when an user deletes their dashboard. 

```Python
import os
```
<br>

# Accessing JSON files in Python
As said above, JSON is very similar to Python dictionaries, this allows us to read or open the JSON file, make it into a Python dictionary, modify the dictionary to what we want, and then dump the contents back into the JSON file. 
To open the JSON file, we use the Pytonh command:

```Python
with open(json_file, 'r') as json_data:
    # Do some code
```
<br>
The code above shows the file or variable json_file being open in read mode (r), you are also able to specify if you want to write (w). In addition, it is also safe to only allow Python to have the nessiary permissions into a file, this means only allowing a file to be read and not be written, or having a file to only be written and not read. This helps with the security of the file. 
<br>
Nice work, you are now able to access the contents of the JSON file. 

# Converting JSON data to a Python Dictionary
To convert the data within the JSON file to a Python Dictionary, we use the command load, which is from the json module. After we use the function load, we must put this data into a Python variable so it can be modified later on. 

```Python
import json

with open(json_file, 'r') as json_data:
    python_dictionary = json.load(json_data)
```
The example above shows us converting the JSON data (json_data) and converting it to a Python dictionary (python_dictionary). This will now allow us to modify and send this data to our HTML page!
<br>
An example of this is down below:
```Python
with open(dash_file, "r") as file_read:
    json_for_dash = json.load(file_read)
return render_template("public/edit_dash.html", data=json_for_dash, dashboard_name=dashboard)
```       