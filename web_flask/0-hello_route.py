#!/usr/bin/python3
"""Starts a Flask application

Returns:
        app: Runs at 0.0.0.0, at port=5000, Displays Hello HBNB!
"""
from flask import Flask as F, app

app = F(__name__)

if app == "__main__":
    app.run(host="0.0.0.0", port=5000)


@app.route('/', strict_slashes=False)
def index():
    """Displays at index"""
    return "Hello HBNB!"
