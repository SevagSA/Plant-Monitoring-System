from dash.html.Div import Div
import constants
from dash import dcc, html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from rfid_config import get_temp_threshold, get_auth_user, set_temp_threshold

from app import app

from utils.helper_functions import get_temperature, send_email

time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
temperature_list = []
threshold_value = get_temp_threshold(get_auth_user())


layout = html.Div([
    html.H3('Temperature Dashboard',
            style={
                'textAlign': 'center',
                'color': 'white',
                'padding': '10px',
                'margin-bottom': '20px',
                'background-color': constants.THIRD_COLOR
            }),
    dcc.Graph(
        id='temperature-graph',
        figure={}
    ),
    html.Div([
        html.Div([
            # html.Div(id='output-container-button', children='Hit the button to update.'),
            dcc.Input(id='temperature-threshold', type='number', value=get_temp_threshold(get_auth_user())),
            dbc.Button('Submit Threshold', id='submit-temperature-threshold', type='submit', n_clicks=0,
                       style={'background-color': constants.THIRD_COLOR, 'border': 'none', 'height': '45px', 'margin': '10px 0px'}, className="me-1"),
            html.P(id='temperature-threshold-text',
                   children='Please enter a temperature threshold.', style={"color": "white"}),
        ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'align-items': 'center', 'padding': '10px'}),
        dbc.Button("Get Temperature", id='get-temp-btn', n_clicks=0,
                   style={'background-color': 'chocolate', 'border': 'none', 'height': '45px'}, className="me-1"),
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'})
])


@app.callback(Output('temperature-threshold-text', 'children'), [Input('submit-temperature-threshold', 'n_clicks')], [State('temperature-threshold', 'value')],)
def update_output(n_clicks, input_value):
    global threshold_value
    threshold_value = input_value
    set_temp_threshold(get_auth_user(), threshold_value)
    print("Modified thresholdValue : " + str(threshold_value))
    if n_clicks is not None:
        return u'''
        The current threshold is {}.
    '''.format(input_value)


@app.callback(
    Output('temperature-graph', 'figure'),
    [Input('get-temp-btn', 'n_clicks')])
def run_script_onClick(n_clicks):
    current_temperature = get_temperature()
    if threshold_value and current_temperature > threshold_value:
        print("Getting the threshold value : " + str(threshold_value))
        print("Current Threshold is : ")
        print(threshold_value)
        print("Current Temperature is : ")
        print(current_temperature)
        print("It is higher")
        send_email()

    temperature_list.append(current_temperature)
    print(current_temperature, "here")
    return {
        'data': [
            {'x': time_of_day, 'y': temperature_list,
             'type': 'line', 'name': 'Humidity'},
        ],
        'layout': {
            'title': 'Plant average temperature per hour',
            'xaxis': {
                'title': 'Time of day',
                'marker': {"color": constants.THIRD_COLOR}
            },
            'yaxis': {
                'title': 'Temperature'
            },
            'plot_bgcolor': constants.PRIMARY_COLOR,
            'paper_bgcolor': constants.PRIMARY_COLOR,
            'font': {
                'color': constants.TEXT_COLOR
            }
        },
    }
