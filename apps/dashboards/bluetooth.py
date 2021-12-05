# import RPi.GPIO as GPIO
import time
import constants
from dash import Dash, dcc, html, Input, Output, State
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
from utils.helper_functions import get_information

from app import app
pin = 32

# GPIO.setmode(GPIO.BOARD)
# GPIO.setwarnings(False)
# GPIO.setup(pin, GPIO.OUT)
# GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)


threshold_value = -100


table_header = [
    html.Thead(html.Tr(
        [html.Th("Devices", style={"color": constants.SECONDARY_COLOR})]))
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
            dcc.Input(id='bluetooth-threshold', type='number'),
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
