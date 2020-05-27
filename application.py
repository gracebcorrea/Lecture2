#eu quero criar uma nova aplicação e quero que seja uma app web usando Flask

from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello World!"

@app.route("/Grace")
    def Grace():
        return "Hello World! I am Here :)"

@app.route("/<string:name>")
    def name():
        return f "Hello, {name}! Good to see you)"

#$ export FLASK_APP=application.py
#$ export FLASK_ENV=development
#flask run --host=0.0.0.0
