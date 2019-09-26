from datetime import datetime

from dash.dependencies import Input, Output

from app import app

@app.callback(Output('a1_placeholder', 'children'),
              [Input('a1_update_button', 'n_clicks')])
def update(n_clicks):
    return datetime.now().strftime('%H:%M:%S')