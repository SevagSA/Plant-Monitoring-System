import RPi.GPIO as GPIO
import time
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from utils.helper_functions import get_information

from app import app
pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
threshold_value = -100
layout = html.Div([
    html.Button('Scan', id='submit-val', n_clicks=0),
    html.Div(id='container-devices',
             children='Press to check nearby bluetooth devices.'),
    html.Div(id='container-information',
             children='Press to device information.'),
     dcc.Input(id='bluetooth-threshold', type='number'),
            dbc.Button('Submit Threshold', id='submit-bluetooth-threshold', type='submit', n_clicks=0,
                style={'background-color' : '#000080', 'border': 'none', 'height': '45px', 'margin':'10px 0px'}, className="me-1"),
            html.P(id='bluetooth-threshold-text', children='Please enter a bluetooth threshold.'),
    dcc.Link('Go to Home Page', href='/')
])
@app.callback(Output('bluetooth-threshold-text', 'children'),[Input('submit-bluetooth-threshold', 'n_clicks')],[State('bluetooth-threshold', 'value')],)
def update_output(n_clicks, input_value):
        global threshold_value
        threshold_value = input_value
        print("Modified thresholdValue : " + str(threshold_value))
        if n_clicks is not None:
            return u'''
        The current threshold is {}.
    '''.format(input_value)

"""
@app.callback(
    Output('container-information', 'children'),
    Input('submit-val', 'n_clicks')
)
def update_bluetooth(n_clicks):
    print(threshold_value)
    return ("Device information : " + get_information(threshold_value))
"""
    

