import random
import dash_bootstrap_components as dbc

from paho.mqtt import client as mqtt_client
from dash import dcc, html
from dash.dependencies import Input, Output, State

from app import app

from utils.helper_functions import get_light, led_on

time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

light_list = []
values = []

threshold_value = 1500


broker = 'broker.emqx.io'
port = 1883
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
                'background-color': '#000080'
            }),
    dcc.Graph(
        id='photoresistor-graph',
        figure={}
    ),
    html.Div([
        dcc.Link('Go to Home Page', href='/'),
        html.Div([
            # html.Div(id='output-container-button', children='Hit the button to update.'),
            dcc.Input(id='light-threshold', type='number'),
            dbc.Button("Submit Threshold", id='submit-light-threshold', n_clicks=0, type='submit',
                       style={'background-color': '#000080', 'border': 'none', 'height': '45px', 'margin': '10px 0px'}, className="me-1"),
            html.P(id='light-threshold-text',
                   children='Please enter a photoresistor threshold.'),
        ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'align-items': 'center', 'padding': '10px'}),
        dbc.Button("Get Light", id='get-light-btn', n_clicks=0,
                   style={'background-color': 'chocolate', 'border': 'none', 'height': '45px'}, className="me-1"),
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}),
    html.Div(id='input-on-submit'),
])


@ app.callback(Output('light-threshold-text', 'children'), [Input('submit-light-threshold', 'n_clicks')], [State('light-threshold', 'value')],)
def update_output(n_clicks, input_value):
    if input_value:
        
        print(input_value)
        global threshold_value
        threshold_value = input_value
        print("Modified thresholdValue : " + str(threshold_value))
        if n_clicks is not None:
            return u'''
            The current threshold is {}.
        '''.format(input_value)
    return "Please enter a value"


@ app.callback(
    Output('photoresistor-graph', 'figure'),
    Input('get-light-btn', 'n_clicks'),
    State('input-on-submit', 'value')
)
def run_script_onClick(n_clicks, value):
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
                'title': 'Time of day'
            },
            'yaxis': {
                'title': 'Temperature'
            }
        },
    }


def connect_mqtt() -> mqtt_client:
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
    def on_message(client, userdata, msg):
        values.append(int(msg.payload.decode()))
        
        if len(values) == 1:
            light_list.append(values[0])
            print("This is the value : " + str(threshold_value))
            print(values[0] > threshold_value)
            if threshold_value and values[0] > threshold_value:
                led_on()
                print("light is higher than threshold")
        #print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    #subscribe(client)
    client.loop_start()
