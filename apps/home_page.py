# import RPi.GPIO as GPIO
import random
import dash
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from app import app
from dash.dependencies import Input, Output
from paho.mqtt import client as mqtt_client
from dash import dcc, html, Input, Output, State
from utils.helper_functions import get_humidity, get_temperature, dc_motor_on, get_light

# For LED
pin = 40
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(pin, GPIO.OUT)

broker = 'broker.emqx.io'
port = 1883
topic = "iot/rfid/team3"
# generate client ID with pub prefix randomly
client_id = f'python-mqtt-{random.randint(0, 100)}'
username = 'emqx'
password = 'public'

rfid_tag = None
valid_rfid_tags = ["124103131100", "131504313"]
is_authenticated = False


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
        rfid_tag = msg.payload.decode()
        break_while = False
        if not rfid_tag in valid_rfid_tags:
            print("is not a valid tag")
            is_authenticated = False
        else:
            is_authenticated = True
            print("this is a valid tag")
            
        print(str(is_authenticated) + " here")            
        # dash.callback_context.response.set_cookie('rfid_tag', rfid_tag)
        print(f"Received `{msg.payload.decode()}` from `{msg.topic}` topic")

    client.subscribe(topic)
    client.on_message = on_message


def run():
    client = connect_mqtt()
    client.loop_start()



unauth_layout = html.P("You're not authenticated. Please scan your rfid tag to authenticate")

run()

auth_layout = html.Div([
            html.H3(
                children='Plant Monitoring System Home Page',
                style={
                    'textAlign': 'center',
                    'color': 'white',
                    'padding': '10px',
                    'margin-bottom': '20px',
                    'background-color': '#000080'
                }
            ),
            html.Img(
                src="https://www.worldatlas.com/r/w1200-q80/upload/89/99/3b/shutterstock-1263201358.jpg",
                style={
                    'max-width': '100%',
                    'height': "200px",
                    'display': 'block',
                    'margin-left': 'auto',
                    'margin-right': 'auto'
                }
            ),
            html.Br(),
            dbc.Row(
                [
                    dbc.Col(html.Div([
                        html.H4("Temperature Dashboard"),
                        html.P(
                            "Track the temperature of the room that your plant is in."),
                        html.P("Current Temperature: " +
                               str(get_temperature())),
                        dcc.Link(dbc.Button("Temperature Dashboard", color="primary", className="me-1",
                                            style={"background-color": 'chocolate', "border": "none"}), href='/dashboards/temperature'),
                    ]),
                        style={'backgroundColor': '#000080', 'color': 'white', 'text-align': "center", 'margin': '5px', 'padding': '5px'}),
                    dbc.Col(html.Div([
                        html.H4("Humidity Dashboard"),
                        html.P(
                            "Track the humidity of the room that your plant is in."),
                        html.P("Current Humidity: " + str(get_humidity())),
                        dcc.Link(dbc.Button("Humidity Dashboard", color="primary", className="me-1",
                                            style={"background-color": '#000080', "border": "none"}), href='/dashboards/humidity'),
                    ]),  style={'backgroundColor': 'chocolate', 'color': 'white', 'text-align': "center", 'margin': '5px', 'padding': '5px'}),
                ],
            ),
            dbc.Row([
                dbc.Col(html.Div([
                    html.H4("Photoresistor"),
                    html.P(
                        "Measure the lighting of the room that your plant is in."),
                    html.P("Current light level: " + str(get_light())),
                    dcc.Link(dbc.Button("Photoresitor", color="primary", className="me-1",
                                        style={"background-color": '#000080', "border": "none"}), href='/dashboards/photoresistor',)
                ]), style={'backgroundColor': 'chocolate', 'color': 'white', 'text-align': "center", 'margin': '5px', 'padding': '5px'}),
                dbc.Col(html.Div([
                    html.H4("LED Button"),
                    html.P("Toggle an LED with the click of a button."),
                    html.P(id='led-status'),
                    dbc.Button("Toggle Button", id='submit-val', color="primary", className="me-1", n_clicks=0,
                               style={"background-color": 'chocolate', "border": "none"}),
                    html.Div(id='input-on-submit'),
                    html.Div(id='container-button-basic')

                ]), style={'backgroundColor': '#000080', 'color': 'white', 'text-align': "center", 'margin': '5px', 'padding': '5px'}),
            ]),
        ])

layout = html.Div(children = [
        html.H1("Unauthorized Person",id = "user_name"),
        html.Div(id = "layout_Div"),
        dcc.Interval(
            id="page_renderer", interval=1*1000, n_intervals=0)
    ])

@app.callback(
    Output('led-status', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value'))
def update_output(n_clicks, value):
    if (n_clicks % 2 == 1):
        print("ON")
        # GPIO.output(pin, True)
        return "Currently the LED is On"
    else:
        print("OFF")
        # GPIO.output(pin, False)
        return "Currently the LED is Off"

@app.callback(
    [Output('user_name', 'children'),
    Output('layout_Div', 'children')],
   [Input('page_renderer', 'n_intervals')])
def rerender_layout(v):
    if is_authenticated:
        return ["Hi Sevag u cutie", auth_layout]
    else:
        return ["Unauthorized Person", unauth_layout]
        
    






