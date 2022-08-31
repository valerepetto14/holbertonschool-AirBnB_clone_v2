#!/usr/bin/python3}
"""create app"""
from flask import Flask, request

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """def hello"""
    return 'Hello HBNB!'


if __name__ == '__main__':
    """app run"""
    app.run(host='0.0.0.0', port=5000)
