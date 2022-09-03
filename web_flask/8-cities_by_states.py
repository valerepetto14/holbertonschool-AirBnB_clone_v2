#!/usr/bin/python3
"""create app"""
from flask import Flask, render_template
from models import storage  # use storage for fetching data
from models import State  # Importo state para poder usar la clase

# Creando una instancia de flask con el nombre del archivo nuestro
app = Flask(__name__)


@app.teardown_appcontext
def tear_down(self):
    """
    After each request you must remove the current SQLAlchemy Session
    """
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def states_list():
    """
    Import data from storage
    """
    # Le paso la clase State al metodo all() de storage para que me traiga
    # todos los objetos de tipo State
    states = storage.all(State).values()
    return render_template("8-cities_by_states.html", states=states)


if __name__ == "__main__":
    """
    Set host IP addres and port
    """
    app.run(host='0.0.0.0', port=5000)
