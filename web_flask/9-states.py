#!/usr/bin/python3
"""Starts a Flask web application."""
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def teardown(exc):
    """Removes the current SQLAlchemy session."""
    storage.close()


@app.route("/states/<string:id>", strict_slashes=False)
def state(id):
    """Render an HTML page to display all cities
    in a state sorted in ascending order.
    """
    state = storage.all("State").get("State." + id)
    return render_template("9-states.html", state=state)


@app.route("/states", strict_slashes=False)
def states():
    """Renders an HTML page to display all states sorted in ascending order."""
    states = storage.all("State")
    return render_template("9-states.html", states=states)


if __name__ == "__main__":
    app.run(host="0.0.0.0")
