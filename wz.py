
"""
An alternative to wsgi.py to run with the werkzeug server for local development.

Run with :

$ python wg.py

"""

from werkzeug.serving import run_simple
from werkzeug.wsgi import DispatcherMiddleware
from flask_app import flask_app

from app1 import app as app1
from app2 import app as app2

application = DispatcherMiddleware(flask_app, {
    '/app1': app1.server,
    '/app2': app2.server,
})
run_simple('localhost', 8080, application, use_reloader=True)