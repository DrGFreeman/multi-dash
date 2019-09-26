import dash_html_components as html

layout = html.Div([
    html.H1('App1'),
    html.P(id='a1_placeholder'),
    html.Button('Update', 'a1_update_button'),
    html.Br(),
    html.A('Home', href='/'),
    html.Br(),
    html.A('App2', href='/app2'),
])