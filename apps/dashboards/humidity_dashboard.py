from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app

from utils.helper_functions import get_humidity


time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
humidity_list = []

layout = html.Div([
    html.H3('Humidity Dashboard',
            style={
            'textAlign': 'center',
            'color': 'white',
            'padding': '10px',
            'margin-bottom': '20px',
            'background-color' : '#000080'
        }),
    dcc.Graph(
        id='humidity-graph',
        figure={}
    ),
    html.Div([
        dcc.Link('Go to Home Page', href='/'),
        dbc.Button("Get Humidity", id='get-humidity-btn', n_clicks=0, style={'background-color':'chocolate', 'border':'none'}, className="me-1"),
    ], style={'display': 'flex', 'justify-content': 'space-between'})
])

@app.callback(
    Output('humidity-graph', 'figure'),
    [Input('get-humidity-btn', 'n_clicks')])
def run_script_onClick(n_clicks):
    humidity_list.append(get_humidity())
    return {
            'data': [
                {'x': time_of_day, 'y': humidity_list, 'type': 'line', 'name': 'Humidity'},
            ],
            'layout': {
                'title': 'Plant average humidity per hour',
                'xaxis': {
                    'title': 'Time of day'
                },
                'yaxis': {
                    'title': 'Humidity'
                }
            }
        }
