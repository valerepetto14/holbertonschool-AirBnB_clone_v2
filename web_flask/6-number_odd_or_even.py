#!/usr/bin/python3}
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
    """def hbnb"""
    return f'C {text.replace("_"," ")}'


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/')
def python(text="is cool"):
    """def hbnb"""
    return f'Python {text.replace("_"," ")}'


@app.route('/number/<n>', strict_slashes=False)
def number(n):
    """def number"""
    if n.isdigit() == True:
        return f'{n} is a number'


@app.route('/number_template/<n>', strict_slashes=False)
def number_template(n):
    """def number"""
    if n.isdigit() == True:
        return render_template("5-number.html", number=n)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def number_odd_or_even(n):
    """def number_odd_or_even"""
    if n.isdigit() == True:
        if int(n) % 2 == 0:
            return render_template("6-number_odd_or_even.html",number=n, type="even")
        return render_template("6-number_odd_or_even.html", number=n, type="odd")


if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
