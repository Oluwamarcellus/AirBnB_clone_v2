#!/usr/bin/python3

"""
2-c_route module
"""

from flask import Flask
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    """
    Web route that displays "Hello HBNB!"
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hello_b():
    """
    Web route that displays "HBNB"
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def c():
    """
    Route that display “C ” followed by the value of the text variable
    """
    text = {{ text }}
    text = text.replace("_", " ")
    return ("C {}".format(escape(text)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
