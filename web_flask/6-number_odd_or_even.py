#!/usr/bin/python3
"""
Starts a Flask app; Runs at 0.0.0.0, at port=5000

"""
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


@app.route('/c/<text>', strict_slashes=False)
def c_txt(text):
    """Displays C and custom input text"""
    return "{}".format(text).replace("_", " ")


@app.route('/python', defaults={"text": "is cool"}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def py_txt(text):
    """Displays Python texting and custom Py routing with default page"""
    return "Python {}".format(text).replace("_", " ")


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """Returns 'is a number' if integer, else a 404 status"""
    return "{} is a number". format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_template(n):
    """Handles /number_template/<int:n>, Returns HTML / 404"""
    return RT('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def even_or_odd(n):
    """Handles /number_odd_or_even/<int:n>, Returns HTML / 404"""
    def e_or_o(n):
        """Determine whether n is even or odd"""
        if n % 2 == 0:
            return "even"
        else:
            return "odd"
    condition = e_or_o(n)
    return RT('6-number_odd_or_even.html', n=n, condition=condition)
