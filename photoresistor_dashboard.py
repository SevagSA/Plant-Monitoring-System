from dash import Dash, dcc, html, Input, Output, State

app = Dash(__name__)

app.layout = html.Div([
    html.H1(id='heading2', children='The Photoresistor (...and 2 LEDs)'),
    html.P(id='informationHeading', children='Functionality:'),
    html.P(id='information', children='IF (Light Intensity < threshold) THEN (turn ON LEDs) AND (Send Email that LEDs are ON)'),
    html.Br(),
    html.Br(),
    html.Br(),
    html.P(id='container-button-basic',
             children='Please enter a photoresistor threshold.'),
    html.Div(dcc.Input(id='input-on-submit', type='number')),
    html.Button('Apply Threshold', id='submit-val', n_clicks=0)
])


@app.callback(
    Output('container-button-basic', 'children'),
    Input('submit-val', 'n_clicks'),
    State('input-on-submit', 'value')
)
def update_output(n_clicks, value):
    return 'Current Photoresistor threshold: [{}].'.format(
        value,
        n_clicks
    )


if __name__ == '__main__':
    app.run_server(debug=True)
