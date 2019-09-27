from datetime import datetime

from dash.dependencies import Input, Output

from app1 import app

@app.callback(Output('placeholder', 'children'),
              [Input('update_button', 'n_clicks')])
def update(n_clicks):
    return datetime.now().strftime('%H:%M:%S')