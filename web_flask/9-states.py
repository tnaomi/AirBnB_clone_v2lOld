#!/usr/bin/python3
"""
Starts a Flask app; Runs at 0.0.0.0, at port=5000. Fetch data from storage

"""
from flask import Flask as F, app, render_template as RT
from models import storage
from models.state import State

app = F(__name__)


@app.teardown_appcontext
def close_session(foo):
    """Closes session"""
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def states_state(id=None):
    """lists states from storage engine"""
    if id:
        states = storage.all(State)
        key = 'State.' + id
        if key in states:
            state = states[key]
        else:
            state = None
        states = []
    else:
        states = list(storage.all(State).values())
    return RT('9-states.html', **locals())


if app == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
