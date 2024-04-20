#!/usr/bin/python3
"""
Starts a Flask app; Runs at 0.0.0.0, at port=5000

"""
from curses.ascii import isalpha
from flask import Flask as F, render_template as RT, app

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


@app.route('/c/<text>', strict_slashes=True)
def c_txt(text):
    """Displays C and custom input text"""
    def strip_inp(text):
        """Strip nonalpha characters from the route"""

        empty = [" " if not isalpha(char) else char for char in text]
        return "".join(str(el) for el in empty)

    return f"C {strip_inp(text)}"
