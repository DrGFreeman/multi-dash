import sys

from dash.dependencies import Input, Output
import dash_core_components as dcc
import dash_html_components as html

from app import app, server
from apps import app1 # Multi file app with __init__.py in sub-folder
from apps import app2 # Single file app directly in apps folder

def home():
    layout = html.Div([
        html.H1('Home'),
        html.A('App1', href='/app1'),
        html.Br(),
        html.A('App2', href='/app2'),
    ])
    return layout

app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page_content')
])

@app.callback(Output('page_content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/app1':
        return app1.layout
    elif pathname == '/app2':
        return app2.layout
    else:
        return home()

if __name__ == '__main__':
    app.run_server(debug=True)