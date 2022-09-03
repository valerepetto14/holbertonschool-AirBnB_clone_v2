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


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """def number_template that render a template"""
    return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    """def number_odd_or_even"""
    if n % 2 == 0:
        return render_template("6-number_odd_or_even.html", number=n,
                               type="even")
    return render_template("6-number_odd_or_even.html", number=n, type="odd")


if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
