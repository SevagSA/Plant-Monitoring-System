import constants
import RPi.GPIO as GPIO
from dash import dcc, html
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc

from app import app
from apps import home_page

from apps.dashboards import humidity_dashboard, temperature_dashboard, photoresistor_dashboard, bluetooth
from rfid_config import get_user_name, get_auth_user


CONTENT_STYLE = {
    "margin-left": "18rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
}

# For LED
pin = 40
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
GPIO.setup(pin, GPIO.OUT)

content = html.Div([html.Div(id='page-content'), ], style=CONTENT_STYLE)

SIDEBAR_STYLE = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "16rem",
    "padding": "2rem 1rem",
    "color": "white",
    "background-color": "#171C1E",
}


sidebar = html.Div(
    [
        html.Div([
            html.Img(
                src="https://i.ibb.co/cc9mPXb/b.png",
                style={
                    'max-width': '50%',
                    'height': "70px",
                    'display': 'block',
                    'margin-left': 'auto',
                    'margin-right': 'auto'
                },
                className="lead"
            ),
            html.H4(f"Sage System", className="display-6", style={"font-size": 20})],
            style={
                "display": "flex",
                "align-items": "center",
        }
        ),
        html.Hr(),
        dbc.Nav(
            [
                dbc.NavLink("Home", href="/", active="exact"),
                dbc.NavLink("Temperature Dashboard",
                            href='/dashboards/temperature', active="exact"),
                dbc.NavLink("Humidity Dashboard",
                            href='/dashboards/humidity', active="exact"),
                dbc.NavLink("Photoresistor",
                            href='/dashboards/photoresistor', active="exact"),
                dbc.NavLink(
                    "Bluetooth", href='/dashboards/bluetooth', active="exact"),
            ],
            vertical=True,
            pills=True,
        ),
         html.Button("Toggle LED", id="led-btn", n_clicks=0, style={
                        "width": "90%",
                        "border": "none",
                        "height": "40px",
                        "background": constants.THIRD_COLOR,
                        "color": constants.TEXT_COLOR,
                    }),
    ],
    style=SIDEBAR_STYLE,
)


app.layout = html.Div([dcc.Location(id="url"), sidebar, content], style={
                      "background-color": constants.PRIMARY_COLOR, "min-height": "100vh"})



@app.callback(
    Output('led-btn', 'children'),
    Input('led-btn', 'n_clicks'),)
def update_output(n_clicks):
    if (n_clicks % 2 == 1):
        print("ON")
        GPIO.output(pin, True)
        return "Currently the LED is On"
        
    else:
        print("OFF")
        GPIO.output(pin, False)
        return "Currently the LED is Off"



@ app.callback(Output('page-content', 'children'),
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
    elif pathname == '/dashboards/bluetooth':
        return bluetooth.layout
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=False)
