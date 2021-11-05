from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

from utils.helper_functions import get_temperature

time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
temperature_list = []

layout = html.Div([
    html.H3('Temperature Dashboard'),
    dbc.Button("Get Temperature", id='get-temp-btn', n_clicks=0, color="danger", className="me-1"),
    dcc.Graph(
        id='temperature-graph',
        figure={}
    ),
    html.Div(id='output-container-button', children='Hit the button to update.'),
    dcc.Link('Go to Home Page', href='/')
])


@app.callback(
    Output('temperature-graph', 'figure'),
    [Input('get-temp-btn', 'n_clicks')])
def run_script_onClick(n_clicks):
    temperature_list.append(get_temperature())
    return {
            'data': [
                {'x': time_of_day, 'y': temperature_list, 'type': 'line', 'name': 'Humidity'},
            ],
            'layout': {
                'title': 'Plant average temperature per hour',
                'xaxis': {
                    'title': 'Time of day'
                },
                'yaxis': {
                    'title': 'Temperature'
                }
            },
        }
