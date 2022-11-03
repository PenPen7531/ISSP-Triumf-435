# Development Setup

Before developing or modifying the code, we must get the code from the GitHub remote repository, set up the virtual environment, and know how to run the Python Script. This document will teach you how to perform all of these actions.

## Using Git
Git is a software for distributed version control that keeps track of changes to files. If Git is not on the system, please use this link:
    https://git-scm.com/downloads
Once installed, we are now able to use Git to push to GitHub, an online repository that will store files. When using Git, there are 3 stages for each file: <br>
Untracked - Where changes are not yet saved or added to the staging area <br>
Staged - Changes are added to the staging area and are read to be commited <br>
Committed - Charges are now committed and is ready to be pushed to the remote repository <br>
Git contains multiple important commands, the primary ones are:
<ul>
    <li>Git add</li>
    <li>Git commit</li>
    <li>Git push</li>
    <li>Git pull</li>
    <li>Git clone</li>
    <li>Git status</li>
</ul>

### Git Add
Git add allows untracked files to be put in the staging area. When added, files added can be committed in the next command. <br>
Note: When added, data and changes are not yet saved.<br>

An example of this code would be: <br>
'''Python
    git add {filename} # Adds the specific file named
    git add .          # Adds all files to the staging area

'''

## GitHub Repository Clone or Pull

 To pull this data, we must clone or pull our code.<br> If the code does not exist on the system, run this command: 

## Development Environment Setup:

When developing multiple projects, using virtual environments in Python allows modules and dependences to be limited to a project. In the case where a dependcy is downloaded globally, it can affect other projects and conflict with other modules. By using a virtual environment, we can limit the reach of these dependencies to a specific scope so we can reduce conflicts between modules. 

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
