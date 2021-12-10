import constants
import dash_bootstrap_components as dbc
from app import app
from dash import dcc, html
from dash.dependencies import Input, Output
from utils.helper_functions import get_humidity

time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
humidity_list = []

layout = html.Div([
    html.H3('Humidity Dashboard',
            style={
                'textAlign': 'center',
                'color': 'white',
                'padding': '10px',
                'margin-bottom': '20px',
                'background-color': constants.THIRD_COLOR
            }),
    dcc.Graph(
        id='humidity-graph',
        figure={}
    ),
    dcc.Interval(
        id="photoresistor-interval", interval=1*10000, n_intervals=0)
    
])


@app.callback(
    Output('humidity-graph', 'figure'),
    [Input('photoresistor-interval', 'n_intervals')])
def run_script_onClick(n_clicks):
    """
    Get the current humidity and display the data on the graph.
    """
    humidity_list.append(get_humidity())
    return {
        'data': [
            {'x': time_of_day, 'y': humidity_list,
             'type': 'line', 'name': 'Humidity'},
        ],
        'layout': {
            'title': 'Plant average humidity per hour',
            'xaxis': {
                'title': 'Time of day',
                'marker': {"color": constants.THIRD_COLOR}
            },
            'yaxis': {
                'title': 'Humidity'
            },
            'plot_bgcolor': constants.PRIMARY_COLOR,
            'paper_bgcolor': constants.PRIMARY_COLOR,
            'font': {
                'color': constants.TEXT_COLOR
            }
        }
    }
