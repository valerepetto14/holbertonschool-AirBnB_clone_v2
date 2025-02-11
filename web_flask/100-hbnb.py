#!/usr/bin/python3
"""create app"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


#!/usr/bin/python3
"""create app"""
from flask import Flask, request, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/hbnb", strict_slashes=False)
def states_list():
    """Import data from storage"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template("100-hbnb.html", states=states,
                           amenities=amenities)


if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)



if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
