# Development Environment Setup:

When developing multiple projects, using virtual environments in Python allows modules and dependences to be limited to a project. In the case where a dependcy is downloaded globally, it can affect other projects and conflict with other modules. By using a virtual environment, we can limit the reach of these dependencies to a specific scope so we can reduce conflicts between modules. 

## LINUX:

    cd ISSP-Triumf-435;
    python3 -m venv venv;
    source venv/bin/activate;
    pip3 install -r requirements.txt;

## WINDOWS:

    cd ISSP-Triumf-435;
    python -m venv venv;
    ./venv/bin/activate;
    pip install -r requirements.txt;

<br>

```
Start Flask app:

    flask run;
```