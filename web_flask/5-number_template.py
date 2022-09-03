#!/usr/bin/python3
"""create app"""
from flask import Flask, request, render_template

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
    """def c that return the variable text"""
    return 'C {}'.format(text.replace("_", " "))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python', strict_slashes=False)
def python(text="is cool"):
    """def python"""
    return 'Python {}'.format(text.replace("_", " "))


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    """def number"""
    return '{} is a number'.format(n)


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """def number"""
    if n.isdigit() is True:
        return render_template("5-number.html", number=n)


if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
