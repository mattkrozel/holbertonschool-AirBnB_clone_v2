#!/usr/bin/python3
'''
script opens flask server
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ('Hello HBNB!')


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return ('HBNB')


@app.route('/c/<string:text>', strict_slashes=False)
def c(text=None):
    return ('C {}'.format(text.replace('_', ' ')))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def python(text='is_cool'):
    return ('Python {}'.format(text.replace('_', ' ')))

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
