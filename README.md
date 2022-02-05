# IT-Workshop-Project-2
Extension of IT Workshop Project 1

## Steps to run Backend Server on Linux :
- Open the terminal in the Backend Folder
- First install virtual environment through the following commands:
  - python3 -m venv venv (or) python -m venv venv (based on the version of python in your system)
- Create a virtual environment through the following commands:
  - . venv/bin/activate
  - pip install Flask
  - pip install -U flask-cors
  - pip freeze
  - export FLASK_APP=development
  - export FLASK_DEBUG=1
  - export FLASK_APP=server.py
  - flask run

## Steps to run Backend Server on Windows :
- Open the terminal in the Backend Folder
- First install virtual environment through the following command:
  - pip install virtualenv
- Create a virtual environment through the following commands:
  - virtualenv venv
  - . .\venv\Scripts\activate.ps1
  - pip install Flask
  - pip install Flask-Cors
  - set FLASK_APP=development
  - set FLASK_APP='server.py'
  - $env:FLASK_APP = "server.py"
  - python -m flask run
