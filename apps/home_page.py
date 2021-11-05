import dash_bootstrap_components as dbc

from app import app
from dash import dcc, html
from dash.dependencies import Input, Output

from utils.helper_functions import get_humidity, get_temperature

layout = html.Div([
    html.H3('Plant Monitoring System Home Page'),
    html.H5("Latest Humidity is: " + str(get_humidity())),
    dcc.Link(dbc.Button("Humidity Dashboard", color="primary", className="me-1"), href='/dashboards/humidity'),
    html.Br(),
    html.H5("Latest Temperature is: " + str(get_temperature())),
    dcc.Link(dbc.Button("Temperature Dashboard", color="primary", className="me-1"), href='/dashboards/temperature'),
    html.Br(),
    dcc.Link(dbc.Button("Dashboard Button", color="primary", className="me-1"), href='/utils/dashboard-button')
])