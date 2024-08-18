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
    """Display a string 'HBNB'."""
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c(text):
    """Displays 'C' followed by the value of 'text'."""
    basename = text.replace('_', ' ')
    return "C {}".format(basement)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python(text="is cool"):
    """Displays 'Python' followed by the value of 'text'."""
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def number(n):
    """Display a string '<n> is a number' if it is."""
    return "{} is a number".format(n)



if __name__ == "__main__":
    app.run(host="0.0.0.0")
