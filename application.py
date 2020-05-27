#eu quero criar uma nova aplicação e quero que seja uma app web usando Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"


#$ export FLASK_APP=application.py
#$ export FLASK_ENV=development
