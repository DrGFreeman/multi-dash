from flask import Flask

flask_app = Flask(__name__)
flask_app.title = 'Home'

@flask_app.route('/')
def index():
    index = \
"""<!DOCTYPE html>
<html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Home</h1>
        <a href="/app1">App1</a>
        <br>
        <a href="/app2">App2</a>
    </body>
</html>"""
    return index