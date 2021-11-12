from dash import dcc, html
from dash.dependencies import Input, Output

from app import app
from apps import home_page

from apps.dashboards import humidity_dashboard, temperature_dashboard, photoresistor_dashboard
#import utils.sending_receiving_email
# from apps.utils import dashboard_button


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
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
        }
    )
], style={"padding": '30px'})


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