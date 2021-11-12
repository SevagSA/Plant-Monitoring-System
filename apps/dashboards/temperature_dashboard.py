from dash import dcc, html
from dash.dependencies import Input, Output,State
import dash_bootstrap_components as dbc

from app import app

from utils.helper_functions import get_temperature,dc_motor_on

time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]
temperature_list = []
global threshold_value
threshold_value = 24
layout = html.Div([
    html.H3('Temperature Dashboard',
            style={
                'textAlign': 'center',
                'color': 'white',
                'padding': '10px',
                'margin-bottom': '20px',
                'background-color' : '#000080'
            }),
    dcc.Graph(
        id='temperature-graph',
        figure={}
    ),
    html.Div([
        dcc.Link('Go to Home Page', href='/'),
        html.Div([
            # html.Div(id='output-container-button', children='Hit the button to update.'),
            dcc.Input(id='temperature-threshold', type='number'),
            dbc.Button('Submit Threshold', id='submit-temperature-threshold', type='submit', n_clicks=0,
                style={'background-color' : '#000080', 'border': 'none', 'height': '45px', 'margin':'10px 0px'}, className="me-1"),
            html.P(id='temperature-threshold-text', children='Please enter a photoresistor threshold.'),
        ], style={'display':'flex', 'flex-direction' : 'column', 'align-items':'center', 'align-items': 'center', 'padding':'10px'}),
            dbc.Button("Get Temperature", id='get-temp-btn', n_clicks=0,
                style={'background-color' : 'chocolate', 'border': 'none', 'height': '45px'}, className="me-1"),
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items':'center'})
])

@app.callback(Output('temperature-threshold-text', 'children'),[Input('submit-temperature-threshold', 'n_clicks')],[State('temperature-threshold', 'value')],)
def update_output(n_clicks, input_value):
        global threshold_value
        threshold_value = input_value
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
    print("Running....")
    print(threshold_value is not None)
    if threshold_value is not None and current_temperature > threshold_value:
        
        #print("Getting the threshold value : " + str(threshold_value))
        #print("Current Threshold is : ")
        #print(threshold_value)
        #print("Current Temperature is : ")
        #print(current_temperature)
        print("It is higher")
        #sendEmail
    
    temperature_list.append(current_temperature)
    return [{
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
        }]
