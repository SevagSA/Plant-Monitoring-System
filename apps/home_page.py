import dash_bootstrap_components as dbc

from app import app
from dash import dcc, html
from dash.dependencies import Input, Output

# from utils.helper_functions import get_humidity, get_temperature

layout = html.Div([
    html.H3('Plant Monitoring System Home Page'),
    html.Br(),
        dbc.Row(
            [
                dbc.Col(html.Div([
                        html.H4("Temperature Dashboard"),
                        html.P("Track the temperature of the room that your plant is in."),
                        dcc.Link(dbc.Button("Temperature Dashboard", color="primary", className="me-1", 
                            style={"background-color":'chocolate', "border": "none"}), href='/dashboards/temperature'),
                    ]),
                    style={'backgroundColor':'#000080', 'color': 'white', 'text-align':"center", 'margin': '5px', 'padding': '5px'}),
                dbc.Col(html.Div([
                        html.H4("Humidity Dashboard"),
                        html.P("Track the humidity of the room that your plant is in."),
                        dcc.Link(dbc.Button("Humidity Dashboard", color="primary", className="me-1", 
                            style={"background-color":'#000080', "border": "none"}), href='/dashboards/temperature'),
                ]),  style={'backgroundColor':'chocolate', 'color': 'white', 'text-align':"center", 'margin': '5px','padding': '5px'}),
            ],
        ),
        dbc.Row([
                dbc.Col(html.Div([
                        html.H4("Photoresistor"),
                        html.P("Measure the lighting of the room that your plant is in."),
                        dcc.Link(dbc.Button("Photoresitor", color="primary", className="me-1",
                            style={"background-color":'#000080', "border": "none"}), href='/utils/dashboard-button',)
                ]), style={'backgroundColor':'chocolate', 'color': 'white', 'text-align':"center", 'margin': '5px','padding': '5px'}),
                dbc.Col(html.Div([
                        html.H4("LED Button"),
                        html.P("Toggle an LED with the click of a button."),
                        dcc.Link(dbc.Button("Dashboard Button", color="primary", className="me-1",
                            style={"background-color":'chocolate', "border": "none"}), href='/utils/dashboard-button',)
                ]), style={'backgroundColor':'#000080', 'color': 'white', 'text-align':"center", 'margin': '5px','padding': '5px'}),
        ]),
], style={"padding": '30px'})