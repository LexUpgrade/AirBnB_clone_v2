#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.route("/states_list", strict_slashes=False)
def state_list():
    """Displays a HTML page."""
    states = storage.all("State").values()
    return render_template("7-states_list.html", states=states)


@app.teardown_appcontext
def teardown(exc):
    """Removes all SQLAlchemy session."""
    storage.close()


if __name__ == "__main__":
    """Starts the web application and set the host to '0.0.0.0'."""
    app.run(host="0.0.0.0")
