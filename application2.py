from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
    def index():
        return render_template("index.html", headline=headline)

#$ export FLASK_APP=application2.py
#$ export FLASK_ENV=development
#flask run --host=0.0.0.0
