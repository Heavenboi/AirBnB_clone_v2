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


@app.route("/c/<text>", strict_slashes=False)
def display_text(text):
    """Displays 'C' and then the value of <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


@app.route("/python/<text>", strict_slashes=False)
def display_python_text(text):
    """Displays 'python' and then the value of <text> """
    text = text.replace("_", " ")
    return "C {}".format(text)


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
