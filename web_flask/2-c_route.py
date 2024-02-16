#!/usr/bin/python3
"""script that starts a Flask web application"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def say_hello():
    """Function that says hello"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def say_hbnb():
    """Function that says hbnb"""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def say_c_is(text=None):
    """Function that say some text about C."""
    return f"C {text.replace('_', ' ')}"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
