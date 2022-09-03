#!/usr/bin/python3
"""create app"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """def hello that return helo HBNB"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """def hbnb that return HBNB"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """def c that return the variable text"""
    return f'C {text.replace("_"," ")}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    """def python"""
    return 'Python {}'.format(text.replace("_", " "))


if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
