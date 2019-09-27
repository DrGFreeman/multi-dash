import dash_html_components as html

layout = html.Div([
    html.H1('App1'),
    html.P(id='placeholder'),
    html.Button('Update', 'update_button'),
    html.Br(),
    html.A('Home', href='/'),
    html.Br(),
    html.A('App2', href='/app2'),
])