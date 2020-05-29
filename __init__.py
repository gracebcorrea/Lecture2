from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

#$ export FLASK_APP=__init__.py
#$ export FLASK_ENV=development
#flask run --host=0.0.0.0
