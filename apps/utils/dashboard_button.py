import RPi.GPIO as GPIO
import time
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go

from app import app

GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(6, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

layout = html.Div([
    html.Div(dcc.Input(id='input-on-submit')),
    html.Button('Submit', id='submit-val', n_clicks=0),
    html.Div(id='container-button-basic',
             children='Enter a value and press submit')
])

@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    if (n_clicks % 2 == 1):
        print("ON")
        GPIO.output(6, True)
    else:
        print("OFF")
        GPIO.output(6, False)
