import dash_bootstrap_components as dbc

from app import app
from dash import dcc, html
from dash.dependencies import Input, Output

from utils.helper_functions import get_humidity, get_temperature, dc_motor_on
layout = html.Div([
 
   html.H3(
        children='Plant Monitoring System Home Page',
        style={
            'textAlign': 'center',
            'color': 'black',
            'margin-bottom': '20px',
            'font-weight': 'bold'
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
                        html.P("Track the temperature of the room that your plant is in."),
                        dcc.Link(dbc.Button("Temperature Dashboard", color="primary", className="me-1", 
                            style={"background-color":'chocolate', "border": "none"}), href='/dashboards/temperature'),
                    ]),
                    style={'backgroundColor':'#000080', 'color': 'white', 'text-align':"center", 'margin': '5px', 'padding': '5px'}),
                dbc.Col(html.Div([
                        html.H4("Humidity Dashboard"),
                        html.P("Track the humidity of the room that your plant is in."),
                        dcc.Link(dbc.Button("Humidity Dashboard", color="primary", className="me-1", 
                            style={"background-color":'#000080', "border": "none"}), href='/dashboards/humidity'),
                ]),  style={'backgroundColor':'chocolate', 'color': 'white', 'text-align':"center", 'margin': '5px','padding': '5px'}),
            ],
        ),
        dbc.Row([
                dbc.Col(html.Div([
                        html.H4("Photoresistor"),
                        html.P("Measure the lighting of the room that your plant is in."),
                        dcc.Link(dbc.Button("Photoresitor", color="primary", className="me-1",
                            style={"background-color":'#000080', "border": "none"}), href='/dashboards/photoresistor',)
                ]), style={'backgroundColor':'chocolate', 'color': 'white', 'text-align':"center", 'margin': '5px','padding': '5px'}),
                dbc.Col(html.Div([
                        html.H4("LED Button"),
                        html.P("Toggle an LED with the click of a button."),
                        dcc.Link(dbc.Button("Dashboard Button", color="primary", className="me-1",
                            style={"background-color":'chocolate', "border": "none"}), href='/utils/dashboard-button',)
                ]), style={'backgroundColor':'#000080', 'color': 'white', 'text-align':"center", 'margin': '5px','padding': '5px'}),
        ]),
], style={"padding": '30px'})