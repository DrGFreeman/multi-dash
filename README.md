# multi-dash
Tests for multi-page Dash apps and multiple independent Dash apps deployed within a Flask server.

## Multiple Independent Apps

The [`independent-apps`](https://github.com/DrGFreeman/multi-dash/tree/independent-apps) branch demonstrates two independent Dash apps deployed within a Flask server as described in the [Dash User Guide](https://dash.plot.ly/integrating-dash).

#### Pros
* The two app are totally independent.

#### Cons
* The Flask development server cannot be used.

### App file structure

For demonstation purpose, `app1` is split in seperate files whereas `app2` is packaged in a single file.

```
.
├── app1
│   ├── callbacks.py
│   ├── __init__.py
│   ├── layout.py
├── app2
│   ├── __init__.py
├── flask_app.py
└── wsgi.py
```

### Usage

Run as a WSGI application with *gunicorn*, *waitress* or another server (see the [Flask deployment guide](http://flask.pocoo.org/docs/latest/deploying/) for options). The example below uses [*waitress*](https://docs.pylonsproject.org/projects/waitress/en/latest/index.html).

```
$ waitress-serve wsgi:application
```

## Multi-Page App

The [`multi-page-app`](https://github.com/DrGFreeman/multi-dash/tree/multi-page-app) branch demonstrates a single, multi-page Dash application as described in the [Dash User Guide](https://dash.plot.ly/urls).

#### Pros
* Can run on the Flask development server or be deployed as a wsgi application.

#### Cons
* This is essentially a single application displayed on multiple pages so all `id`s of layout elements used in callbacks must be unique (i.e. two different pages cannot use the same `id` for different elements)

### App file structure

For demonstation purpose, `app1` is contained in a sub-folder with seperate files and *\_\_init\_\_.py* file whereas `app2` is packaged in a single file.

```
.
├── apps
│   ├── app1
│   │   ├── callbacks.py
│   │   ├── __init__.py
│   │   └── layout.py
│   ├── app2.py
│   └── __init__.py
├── app.py
└── index.py
```

### Usage

Run the application with the Flask development server

```
$ python index.py
```

Or run as a WSGI application with *gunicorn*, *waitress* or another server (see the [Flask deployment guide](http://flask.pocoo.org/docs/latest/deploying/) for options). The example below uses [*waitress*](https://docs.pylonsproject.org/projects/waitress/en/latest/index.html).

```
$ waitress-serve index:server
```