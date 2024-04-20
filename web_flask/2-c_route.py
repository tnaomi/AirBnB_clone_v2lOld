#!/usr/bin/python3
"""
Starts a Flask app; Runs at 0.0.0.0, at port=5000

"""
from flask import Flask as F, app

app = F(__name__)

if app == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route('/', strict_slashes=False)
def index():
    """Displays at index"""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Another Route to display HBNB"""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_txt(text):
    """Displays C and custom input text"""
    return "C {}".format(text).replace("_", " ")
