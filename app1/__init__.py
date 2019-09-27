import dash

from app1.layout import layout

app = dash.Dash(__name__, requests_pathname_prefix='/app1/')
app.title = 'App1'
app.layout = layout

import app1.callbacks