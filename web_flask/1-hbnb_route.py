#!/usr/bin/python3
"""Starts a Flask web application

listening on 0.0.0.0, port 5000
Displaying:
    "Hello HBNB!"
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """Displays a string returned."""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


if __name__ == "__main__":
    app.run(host="0.0.0.0")
