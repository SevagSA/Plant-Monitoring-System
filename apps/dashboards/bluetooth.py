import RPi.GPIO as GPIO
import time
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
from utils.helper_functions import get_devices, get_information

from app import app
pin = 32
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)

layout = html.Div([
    html.Button('Scan', id='submit-val', n_clicks=0),
    html.Div(id='container-devices',
             children='Press to check nearby bluetooth devices.'),
    html.Div(id='container-information',
             children='Press to device information.'),
    dcc.Link('Go to Home Page', href='/')
])

@app.callback(
    Output('container-devices', 'children'),
    Output('container-information', 'children'),
    Input('submit-val', 'n_clicks')
)
def update_bluetooth(n_clicks):
    devices = "Current number of devices : {}".format(get_devices())
    information_list = get_information()
    return devices,("Device information : " + information_list)
    

