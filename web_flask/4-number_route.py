#!/usr/bin/python3}
"""create app"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """def hello"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """def hbnb"""
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c(text):
    """def hbnb"""
    return f'C {text.replace("_"," ")}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/')
def python(text="is cool"):
    """def hbnb"""
    return f'Python {text.replace("_"," ")}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """def number"""
    return f'{n} is a number'

if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
