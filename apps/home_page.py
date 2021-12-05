import RPi.GPIO as GPIO
import random
import datetime
import time

from dash.html.Button import Button
import constants
import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from app import app
from dash.dependencies import Input, Output
from paho.mqtt import client as mqtt_client
from dash import dcc, html, Input, Output, State
from utils.helper_functions import get_humidity, get_temperature, dc_motor_on, user_login

import dash_daq as daq

from rfid_config import set_auth_user, get_auth_user, get_user_name

# For LED
pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

broker = 'broker.emqx.io'
port = 1883
topic = "iot/rfid/team3"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'

rfid_tag = None
valid_rfid_tags = ["124103131100", "131504313","4117726232"]
is_authenticated = False

GAUGE_STYLE = {
    "background-color": constants.SECONDARY_COLOR
}


def connect_mqtt() -> mqtt_client:
    def on_connect(client, userdata, flags, rc):
        if rc == 0:
            subscribe(client)
            print("herre")
        else:
            print("Failed to connect, return code %d\n", rc)

    client = mqtt_client.Client(client_id)
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.connect(broker, port)
    return client



def subscribe(client: mqtt_client):
    def on_message(client, userdata, msg):
        global is_authenticated
        global rfid_tag
        rfid_tag = msg.payload.decode()
        if not rfid_tag in valid_rfid_tags:
            print("not valid tag")
            is_authenticated = False
        else:
            is_authenticated = True
            

            user_login(f"Hi user, you have logged in at : {datetime.datetime.now()}")
            time.sleep(0.1)
            print("this is a valid tag")

        print(str(is_authenticated) + " here")
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    client.loop_start()


unauth_layout = html.P(
    "You're not authenticated. Please scan your rfid tag to authenticate")

run()
time_of_day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12,
               13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24]

# TODO
temperature_list = [5, 3, 4, 6, 6, 4, 6, 7, 5, 6]
# TODO
humidity_list = [54, 82, 46, 26, 65, 47, 75, 67, 61, 78, 39]

table_header = [
    html.Thead(html.Tr(
        [html.Th("Bluetooth Devices", style={"color": constants.SECONDARY_COLOR})]))
]

row1 = html.Tr([html.Td("1", style={
               "color": constants.SECONDARY_TEXT_COLOR, "width": "160px"}), html.Td("60-C1-15-F8-FA-2C"), html.Td("Some Info")])
row2 = html.Tr([html.Td("2", style={
               "color": constants.SECONDARY_TEXT_COLOR, "width": "160px"}), html.Td("19-A2-18-EC-DB-4F"), html.Td("Some Info")])
row3 = html.Tr([html.Td("3", style={
               "color": constants.SECONDARY_TEXT_COLOR, "width": "160px"}), html.Td("AB-F8-AE-E1-3A-40"), html.Td("Some Info")])
row4 = html.Tr([html.Td("4", style={
               "color": constants.SECONDARY_TEXT_COLOR, "width": "160px"}), html.Td("00:11:22:33:FF:EE"), html.Td("Some Info")])

table_body = [html.Tbody([row1, row2, row3, row4])]
table = dbc.Table(table_header + table_body,
                  style={"color": "white", "margin-bottom": "60px"})


auth_layout = html.Div([
    html.Div(id="graph-holder", children=[
        dcc.Graph(
            id='temperature-graph',
            figure={
                'data': [
                    {'x': time_of_day, 'y': temperature_list,
                        'type': 'line', 'name': 'Humidity',
                     'marker': {"color": constants.SECONDARY_COLOR}},
                ],
                'layout': {
                    'title': 'Plant\'s room temperature per hour',
                    'xaxis': {
                        'title': 'Time of day'
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
        ),
        dcc.Graph(
            id='temperature-graph',
            figure={
                'data': [
                    {'x': time_of_day, 'y': humidity_list,
                        'type': 'line', 'name': 'Humidity',
                     'marker': {"color": constants.THIRD_COLOR}},
                ],
                'layout': {
                    'title': 'Plant\'s room humidity per hour',
                    'xaxis': {
                        'title': 'Time of day'
                    },
                    'yaxis': {
                        'title': 'Humidity'
                    },
                    'plot_bgcolor': constants.PRIMARY_COLOR,
                    'paper_bgcolor': constants.PRIMARY_COLOR,
                    'font': {
                        'color': constants.TEXT_COLOR
                    }
                },
            }
        ),
        # dcc.Graph(
        #     id='temperature-graph',
        #     figure={
        #         'data': [
        #             {'x': time_of_day, 'y': temperature_list,
        #                 'type': 'line', 'name': 'Humidity',
        #              'marker': {"color": constants.SECONDARY_COLOR}},
        #         ],
        #         'layout': {
        #             'title': 'Photoresistor',
        #             'xaxis': {
        #                 'title': 'Time of day'
        #             },
        #             'yaxis': {
        #                 'title': 'Temperature'
        #             },
        #             'plot_bgcolor': constants.PRIMARY_COLOR,
        #             'paper_bgcolor': constants.PRIMARY_COLOR,
        #             'font': {
        #                 'color': constants.TEXT_COLOR
        #             }
        #         },
        #     }
        # ),
    ], style={"flex": 0.7}),
    html.Div(id="bluetooth-table-holder",
             children=[
                html.Div(id="led-btn-holder", children=[
                    html.H3("Toggle LED", style={
                            "color": constants.TEXT_COLOR, "margin-bottom": "20px"}),

                    html.Button("Open LED", id='', n_clicks=0, style={
                        "width": "100%",
                        "border": "none",
                        "height": "40px",
                        "background": constants.SECONDARY_COLOR,
                        "color": constants.TEXT_COLOR,
                        "font-size": "20px"
                    }),




                ], style={"margin-bottom": "60px"}),
                 table,
                 html.Div([
                     html.H4("Current Photoresistor Value", style={
                         "color": constants.TEXT_COLOR, "text-align": "center", "margin": "30px 0px 0px 20px"}),
                     html.Div([daq.Gauge(
                         showCurrentValue=True,
                         units="MΩ",
                         id='photoresistor-gauge',
                         size=300,
                         color=constants.SECONDARY_COLOR,
                         label="",
                         value=800,
                         max=1200,
                         min=0,)]),
                 ], style={"display": "flex", "flex-direction": "column", "align-items": "center"})
             ],
             style={"flex": 0.3})
], style={"display": "flex", "flex-direction": "row"})

layout = html.Div(children=[
    html.H1("Unauthorized Person", id="user_name",
            style={"color": constants.TEXT_COLOR}),
    html.Div(id="layout_Div"),
    dcc.Interval(
        id="page_renderer", interval=1*1000, n_intervals=0)
])


@app.callback(
    Output('led-status', 'children'),
    Input('led-btn', 'n_clicks'),
    State('input-on-submit', 'value'))
def update_output(n_clicks, value):
    print("here")
    if (n_clicks % 2 == 1):
        print("ON")
        GPIO.output(pin, True)
        return "Currently the LED is On"
    else:
        print("OFF")
        GPIO.output(pin, False)
        return "Currently the LED is Off"


@app.callback(
    [Output('user_name', 'children'),
     Output('layout_Div', 'children')],
    [Input('page_renderer', 'n_intervals')])
def rerender_layout(v):
    if is_authenticated:
        set_auth_user(rfid_tag)
        print(rfid_tag)
        return [f"Hi {get_user_name(rfid_tag)}", auth_layout]
    else:
        return ["Unauthorized Person", unauth_layout]

