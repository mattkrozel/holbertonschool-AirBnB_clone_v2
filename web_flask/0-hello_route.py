#!/usr/bin/python3
'''
script opens flask server
'''

from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello():
    return ('Hello HBNB!')

if __name__ == '__main__':
    app.run(host='0.0.0.0')