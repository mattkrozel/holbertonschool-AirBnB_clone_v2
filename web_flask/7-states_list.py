#!/usr/bin/python3
"""script that starts web flask application on port 5000 fetching from storage engine"""
from flask import Flask
from flask import render_template
from models import storage, State
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """display html page with states list"""
    return render_template('7-states_list.html',
                           states=storage.all(State))


@app.teardown_appcontext
def teardown(exc):
    """closes out or tears down"""
    storage.close()


if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0', port=5000)
