#!/usr/bin/python3

"""
5-number_template module
"""

from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Web route that displays "Hello HBNB!"
    """
    return ("Hello HBNB!")


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Web route that displays "HBNB"
    """
    return ("HBNB")


@app.route('/c/<text>', strict_slashes=False)
def hello_c(text):
    """
    Route that display “C ” followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return ("C {}".format(escape(text)))


@app.route('/python/<text>', strict_slashes=False)
@app.route('/python/', strict_slashes=False)
def hello_python(text="is cool"):
    """
    Route that display "C " followed by the value of the text variable
    """
    text = text.replace("_", " ")
    return ("Python {}".format(escape(text)))


@app.route('/number/<int:n>', strict_slashes=False)
def is_number(n):
    """
    Route that display display “n is a number” only if n is an integer
    """
    return ("{} is a number".format(escape(n)))


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template(n):
    """
    Route that display display “n is a number” only if n is an integer
    """
    return (render_template('5-number.html', number=escape(n)))


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
