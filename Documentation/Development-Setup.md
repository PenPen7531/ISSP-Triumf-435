# Development Setup

Before developing or modifying the code, we must get the code from the GitHub remote repository, set up the virtual environment, and know how to run the Python Script. This document will teach you how to perform all of these actions.

## Using Git
Git is a software for distributed version control that keeps track of changes to files. If Git is not on the system, please use this link:
    https://git-scm.com/downloads
Once installed, we are now able to use Git to push to GitHub, an online repository that will store files. When using Git, there are 3 stages for each file: <br><br>
<b>Untracked</b> - Where changes are not yet saved or added to the staging area <br><br>
<b>Staged</b> - Changes are added to the staging area and are read to be commited <br><br>
<b>Committed</b> - Charges are now committed and is ready to be pushed to the remote repository <br><br>
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
```
    git add {filename}  # Adds the specific file named

    git add .           # Adds all files to the staging area

``` 

### Git Commit 
Git commit allows changes from the staging area to be in the committed area. Once committed, data is now prepared be sent to the remote repository to be saved. When using git commit, a message must always be attached to the commit, else an error will occur. To add a message, us the `-m` arugment and then insert your message between quotation marks. When making commits, it is important to be specific to what changes you made, just in case you need to find a specific version, the commit message can help ease that process of looking back. 

An example of this code will be: <br>
```
    git commit -m "I am a very detailed message"

```

### Git Push
Git push will push committed data to the remote repository. When pushing data, make sure you push to the correct repository, but also the correct branch. Branches are different snapshots that allows changes to be made to be separated until they need to be merged together. Usually, each deleoper or each feature is given a separate branch. The `main` or `master` branch should not be directly pushed into. When pushing, we use 2 arguments, `origin`, which specifies the location of where to push the data, and `{branch}`, which will be the branch to push this data to.  <br>

An example of a git push would be:
```
    git push origin main         # Will push these changes to the main branch

    git push origin my_branch    # Will push to a unique branch

```

### Git Pull
Git pull will pull new changes from an existing repository that is already initialized in the folder. If the folder has not been linked or initialized with the remote repository, you must git clone an existing repository or initialize a new repository. Git pull allows the system to have the current and newest data in the repository. <br>
An example of git pull would be:

```
    git pull origin main        # Will pull the newest data from the main branch

    git pull origin my_branch   # Will pull the newest data from my_branch

```

### Git Clone
Git clone allows a remote repository to be cloned and initialized onto the local system. When working with a new repository, we must clone it. This links the local folder with the remote repository. <br>
An example of git clone would be:

```
    git clone https://github.com/PenPen7531/ISSP-Triumf-435/tree/main   #This command will clone all the data from the main branch of the current repository
```

## GitHub
GitHub is an online repository that allows files and changes to be kept track of. In connection with Git, we are able to use Git commands to push our data to a repository on GitHub. 

### GitHub Connection
When working with GitHub, we must connect our local system with our account on GitHub. This helps us keep our data secure and allows an ecrypted SSH connection between our system and our respositories. Generally, GitHub will use an RSA public and private key to ensure that the connection is secure. We save one of these keys on our local system, and this allows an ecrypted path and connection. Please follow this documentation to perform this action:

<a href="https://git-scm.com/book/en/v2/GitHub-Account-Setup-and-Configuration#:~:text=The%20first%20thing%20you%20need,Sign%20up%20for%20GitHub%E2%80%9D%20button.">Click Here</a>

 
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

<br>


Start Flask app:

    flask run;
