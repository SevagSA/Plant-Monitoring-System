from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import home_page

from apps.dashboards import humidity_dashboard, temperature_dashboard, photoresistor_dashboard
#import utils.sending_receiving_email
# from apps.utils import dashboard_button

CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

content = html.Div([
    html.Div(id='page-content'),
    html.P(
        children='Plant Monitoring System',
        style={
            'display':'flex',
            'justify-content':'center',
            'align-items': 'center',
            'height': '20vh',
            'margin-top':'2.4%',
            'textAlign': 'center',
            'color': 'white',
            'background-color' : '#000080'
        })
], style=CONTENT_STYLE)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "color": "white",
    "background-color": "#000080",
}


sidebar = html.Div(
    [
        html.H4("Welcome User", className="display-6"),
        html.Hr(),
        html.P("Plant Monitoring System", className="lead"),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Temperature Dashboard", href='/dashboards/temperature', active="exact"),
                dbc.NavLink("Humidity Dashboard", href='/dashboards/humidity', active="exact"),
                dbc.NavLink("Photoresistor", href='/dashboards/photoresistor', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home_page.layout
    elif pathname == '/dashboards/humidity':
        return humidity_dashboard.layout
    elif pathname == '/dashboards/temperature':
        return temperature_dashboard.layout
    elif pathname == '/dashboards/photoresistor':
        return photoresistor_dashboard.layout
    # elif pathname == '/utils/dashboard-button':
    #     return dashboard_button.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=False)