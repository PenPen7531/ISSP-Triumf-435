# high-level-apps (main page)



## Installation notes for Developers

```
cd /my/devel/dir/
git clone git@gitlab.triumf.ca:hla/high-level-apps.git
cd high-level-apps
python3 -m venv venv-py3
source venv-py3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
python run.py
```

Following these steps the app should be visible at http://localhost:4994


---
### Environment Variables

This app requires the following environment variables:

export APPCODEDIR=$MYAPPSDIR/high-level-apps/


These environment variables can be defined in your `~/.bashrc` file and then applied in your terminal by running command `source ~/.bashrc`.

Sample `~/.bashrc`:

```
export MYAPPSDIR=/home/cbarquest/workspace
export APPDATADIR=$MYAPPSDIR/data/
```

---
### Virtual environments

To set up a new python 3 virtual environment:

```
python3 -m venv venv-py3
```

To activate virtual environment:

```
source venv-py3/bin/activate
```

Once activated, note that in your shell the name will appear like: `(venv-py3) username@hostname:`. To upgrade pip and install packages within your venv from a requirements.txt file:
```
pip3 install --upgrade pip
pip3 install -r requirements.txt
```

To deactivate the virtual environment, simply:

```
deactivate
```
