#!/usr/bin/python3
"""
script that run a flask app and return Hello HBNB and HBNB
listening to port 0.0.0.0:5000
"""
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_HBNB():
    """method that displays Hello HBNB!"""
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """method that displays HBNB on the browser """
    return "HBNB"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
