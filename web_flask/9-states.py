#!/usr/bin/python3
"""create app"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
app = Flask(__name__)

@app.teardown_appcontext
def tear_down(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/states", strict_slashes=False)
def states_list():
    """Import data from storage"""
    states = storage.all(State).values()
    return render_template("7-states_list.html", states=states)


@app.route("/states/<id>", strict_slashes=False)
def states_cities(id):
    """Import data from storage"""
    states = storage.all(State).values()
    return render_template("9-states.html", states=states)

if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
