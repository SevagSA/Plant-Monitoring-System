import random
import time

import constants
import dash_bootstrap_components as dbc
import RPi.GPIO as GPIO
from app import app
from dash import dcc, html
from dash.dependencies import Input, Output, State
from paho.mqtt import client as mqtt_client
from rfid_config import (get_auth_user, get_photoresistor_threshold,
                         set_photoresistor_threshold)
from utils.helper_functions import led_on

time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

light_list = []
values = []

threshold_value = 1500  # database value

pin = 37
pin2 = 35
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(pin2, GPIO.OUT)
GPIO.output(pin2, False)
GPIO.output(pin, False)
# Our broker server for MQTT
broker = 'broker.emqx.io'
port = 1883
# Our topic for the photoresistor
topic = "iot/photoresistor/team3"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'

layout = html.Div([
    html.H3('Photoresistor Dashboard',
            style={
                'textAlign': 'center',
                'color': 'white',
                'padding': '10px',
                'margin-bottom': '20px',
                'background-color': constants.THIRD_COLOR
            }),
    dcc.Graph(
        id='photoresistor-graph',
        figure={}
    ),
    html.Div([
        html.Div([
            # html.Div(id='output-container-button', children='Hit the button to update.'),
            dcc.Input(id='light-threshold', type='number',
                      value=get_photoresistor_threshold(get_auth_user())),
            dbc.Button("Submit Threshold", id='submit-light-threshold', n_clicks=0, type='submit',
                       style={'background-color': constants.THIRD_COLOR, 'border': 'none', 'height': '45px', 'margin': '10px 0px'}, className="me-1"),
            html.P(id='light-threshold-text',
                   children='Please enter a photoresistor threshold.', style={"color": constants.TEXT_COLOR}),
        ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'align-items': 'center', 'padding': '10px'}),
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}),
    html.Div(id='input-on-submit'),
    dcc.Interval(
        id="photoresistor-interval", interval=1*10000, n_intervals=0)
])


@ app.callback(Output('light-threshold-text', 'children'), [Input('submit-light-threshold', 'n_clicks')], [State('light-threshold', 'value')],)
def update_output(n_clicks, input_value):
    """
    Update the photoresistor threshold.
    """
    if input_value:

        global threshold_value
        threshold_value = input_value
        set_photoresistor_threshold(get_auth_user(), threshold_value)
        if n_clicks is not None:
            return u'''
            The current threshold is {}.
        '''.format(input_value)
    return "Please enter a value"


@ app.callback(
    Output('photoresistor-graph', 'figure'),
    Input('photoresistor-interval', 'n_intervals'),
    State('input-on-submit', 'value')
)
def run_script_onClick(n_clicks, value):
    """
    Get the current light value and display the data on the graph.
    """
    values.clear()
    run()
    return {
        'data': [
            {'x': time_of_day, 'y': light_list,
             'type': 'line', 'name': 'Humidity'},
        ],
        'layout': {
            'title': 'Plant average light per hour',
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


def connect_mqtt() -> mqtt_client:
    """
    Connect to mqtt server.
    """
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            subscribe(client)
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client


def subscribe(client: mqtt_client):
    """
    Subscribes to the photoresistor topic, which is being published by the MQTT on the NodeMCU side.
    """
    def on_message(client, userdata, msg):
        values.append(int(msg.payload.decode()))

        if len(values) == 1:
            light_list.append(values[0])
            if threshold_value and values[0] > threshold_value:
                led_on()
                GPIO.output(pin, True)
                GPIO.output(pin2, True)
                time.sleep(3)
                GPIO.output(pin, False)
                GPIO.output(pin2, False)
    client.subscribe(topic)
    client.on_message = on_message


def run():
    """
    Run the MQTT related functionality in a loop
    """
    client = connect_mqtt()
    client.loop_start()
