#!/usr/bin/python3
"""
Starts a Flask app; Runs at 0.0.0.0, at port=5000

"""
from flask import Flask as F, app, render_template as RT
from models import storage
from models.state import State

app = F(__name__)

if app == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)


@app.teardown_appcontext
def close_session(foo):
    """Closes session"""
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def states_list():
    """lists states from storage engine"""
    states = list(storage.all(State).values())
    return RT('8-cities_by_states.html', states=states)
