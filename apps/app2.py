from datetime import datetime

import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    html.H1('App2'),
    html.P(id='placeholder'),
    html.Button('Update', 'update_button'),
    html.Br(),
    html.A('Home', href='/'),
    html.Br(),
    html.A('App1', href='/app1'),
])

@app.callback(Output('placeholder', 'children'),
              [Input('update_button', 'n_clicks')])
def update(n_clicks):
    return datetime.now().strftime('%H:%M:%S')