import dash
from dash import dcc, html
from time import time, sleep
import plotly.graph_objects as go

from helper_functions import get_temperature, get_humidity

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)
time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
humidity_list = []
temperature_list = []
while True:
    humidity_list.append(get_humidity())
    temperature_list.append(get_temperature())
    sleep(60 - time() % 60)


app.layout = html.Div(children=[
    html.H1(children='Plant Monitoring DashBoard'),

    dcc.Graph(
        id='humidity-graph',
        figure={
            'data': [
                {'x': time_of_day, 'y': humidity_list, 'type': 'line', 'name': 'Humidity'},
            ],
            'layout': {
                'title': 'Plant Average Humidity per Hour'
            }
        }
    ),

    dcc.Graph(
        id='temperature-graph',
        figure={
            'data': [
                {'x': time_of_day, 'y': temperature_list, 'type': 'line', 'name': 'Humidity'},
            ],
            'layout': {
                'title': 'Plant Average temperature per Hour'
            }
        }
    )
])


if __name__ == '__main__':
    app.run_server(debug=True)