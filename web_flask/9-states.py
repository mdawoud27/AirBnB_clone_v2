#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
def display_states():
    """Function that displays a html page with the states listed"""
    states = sorted(list(storage.all("State").values()), key=lambda x: x.name)
    return render_template("9-states.html", states=states)


@app.teardown_appcontext
def close_storage():
    """Close the storage"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
