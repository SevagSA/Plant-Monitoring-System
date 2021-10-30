import dash
import plotly.graph_objects as go
import dash_core_components as dcc
import dash_html_components as html

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H1(children='Health Monitoring DashBoard'),


    dcc.Graph(
        id='new-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'line', 'name': 'test1'},
            ],
            'layout': {
                'title': 'Plant Average Temperature per Day'
            }
        }
    )
])



if __name__ == '__main__':
    app.run_server(debug=True)