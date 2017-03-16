Tools and Languages Used
========================

Language: Python 3.6.0
Web Framework: Flask
HTML Template Engine: Jinja2
JavaScript Library: Google Charts
Database: SQLite3 (Python)

Steps to setup the project
==========================
Windows
=======
Run CMD as administrator
Run
CMD> cd "C:\Program Files\Python36\Scripts"
pip install virtualenv
pip install flask
pip install dropbox
pip install Flask-Session

Create a folder for the web app (e.g. C:\WebApp)
Create a virtual environment (say "VE")
Run
CMD> cd "C:\WebApp" in CMD
virtualenv VE

Activate the virtual environment
Run
CMD> cd "C:\WebApp\VE\Scripts"
activate

Copy the SpaceAnalyzer (code folder) to VE
"C:\WebApp\VE\SpaceAnalyzer"

Run the server
Run
CMD> cd "C:\WebApp\VE\SpaceAnalyzer"
python main.py

Log-in to the App
In the browser type "http://localhost:5000"
Use a valid access token to login
