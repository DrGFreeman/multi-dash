from datetime import datetime

import dash
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash(__name__, requests_pathname_prefix='/app2/')
app.title = 'App2'

layout = html.Div([
    html.H1('App2'),
    html.P(id='placeholder'),
    html.Button('Update', 'update_button'),
    html.Br(),
    html.A('Home', href='/'),
    html.Br(),
    html.A('App1', href='/app1'),
])

app.layout = layout

@app.callback(Output('placeholder', 'children'),
              [Input('update_button', 'n_clicks')])
def update(n_clicks):
    return datetime.now().strftime('%H:%M:%S')