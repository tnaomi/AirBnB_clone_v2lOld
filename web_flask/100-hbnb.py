#!/usr/bin/python3
"""
Starts a Flask app; Runs at 0.0.0.0, at port=5000. Fetch data from storage

"""
from flask import Flask as F, app, render_template as RT
from models import storage, Amenity, Place, State


app = F(__name__)


@app.teardown_appcontext
def close_session(foo):
    """Closes session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb(id=None):
    """displays a HTML page like 8-index.html on /hbnb"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    places = storage.all(Place)
    return RT('100-hbnb.html', **locals())


if app == "__main__":
    storage.reload()
    app.run(host="0.0.0.0", port=5000)
