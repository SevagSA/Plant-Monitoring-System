import constants
import dash_bootstrap_components as dbc
import plotly.graph_objects as go
import RPi.GPIO as GPIO
from app import app
from dash import Input, Output, State, dcc, html
from utils.helper_functions import get_information

pin = 32

# Set GPIO pins
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


threshold_value = -100


table_header = [
    html.Thead(html.Tr(
        [html.Th("Devices", style={"color": constants.SECONDARY_COLOR})]))
]


# Table that will display the bluetooth devices
table_body = [html.Tbody(id='table-body', children=[])]
table = dbc.Table(table_header + table_body,
                  style={"color": "white", "margin-bottom": "60px"})


layout = html.Div([
    html.H3('Bluetooth Devices',
            style={
                'textAlign': 'center',
                'color': 'white',
                'padding': '10px',
                'margin-bottom': '20px',
                'background-color': constants.THIRD_COLOR
            }),

    table,


    html.Div([
        html.Div([
            # threshold
            dcc.Input(id='bluetooth-threshold',
                      type='number', value=threshold_value),
            dbc.Button('Submit Threshold', id='submit-bluetooth-threshold', type='submit', n_clicks=0,
                       style={'background-color': constants.THIRD_COLOR, 'border': 'none', 'height': '45px', 'margin': '10px 0px'}, className="me-1"),
            html.P(id='bluetooth-threshold-text',
                   children='Please enter a bluetooth threshold.', style={'color': constants.TEXT_COLOR}),
        ], style={'display': 'flex', 'flex-direction': 'column', 'align-items': 'center', 'align-items': 'center', 'padding': '10px'}),
        dbc.Button("Scan Devices", id='submit-val', n_clicks=0,
                   style={'background-color': 'chocolate', 'border': 'none', 'height': '45px'}, className="me-1"),
    ], style={'display': 'flex', 'justify-content': 'space-between', 'align-items': 'center'}),
])


@ app.callback(Output('bluetooth-threshold-text', 'children'), [Input('submit-bluetooth-threshold', 'n_clicks')], [State('bluetooth-threshold', 'value')],)
def update_output(n_clicks, input_value):
    """
    Update the threshold value of the bluetooth.
    """
    global threshold_value
    threshold_value = input_value
    if n_clicks is not None:
        return u'''
        The current threshold is {}.
    '''.format(input_value)


@app.callback(
    Output('table-body', 'children'),
    Input('submit-val', 'n_clicks')
)
def update_bluetooth(n_clicks):
    """
    Get all bluetooth devices in proximity and display their information in a row of a table.
    """
    count = 0
    rows = []
    devices = get_information()
    for idx, device in enumerate(devices):
        if devices.get(device) > threshold_value:
            count += 1
            rows.append(
                html.Tr([html.Td(count, style={
                    "color": constants.SECONDARY_TEXT_COLOR, "width": "160px"}), html.Td(device), html.Td(devices.get(device))])
            )
    return rows
