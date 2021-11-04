import dash_bootstrap_components as dbc

from app import app
from dash import dcc, html
from dash.dependencies import Input, Output

layout = html.Div([
    html.H3('Home Page'),
    
    dcc.Link(dbc.Button("Humidity Dashboard", color="primary", className="btn-1"), href='/dashboards/humidity'),
    html.Br(),
    dcc.Link(dbc.Button("Temperature Dashboard", color="primary", className="btn-2"), href='/dashboards/temperature')
])