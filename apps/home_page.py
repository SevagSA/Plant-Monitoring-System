# import RPi.GPIO as GPIO
import plotly.graph_objects as go
import dash_bootstrap_components as dbc

from app import app
from dash.dependencies import Input, Output
from dash import dcc, html, Input, Output, State
from utils.helper_functions import get_humidity, get_temperature, dc_motor_on, get_light

# For LED
pin = 40
# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(pin, GPIO.OUT)

layout = html.Div([
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


@app.callback(
    Output('led-status', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    if (n_clicks % 2 == 1):
        print("ON")
        # GPIO.output(pin, True)
        return "Currently the LED is On"
    else:
        print("OFF")
        # GPIO.output(pin, False)
        return "Currently the LED is Off"
