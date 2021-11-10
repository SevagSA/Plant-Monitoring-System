from dash import dcc, html
from dash.dependencies import Input, Output

from app import app
from apps import home_page

from apps.dashboards import humidity_dashboard, temperature_dashboard
# from apps.utils import dashboard_button


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])


@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == '/':
        return home_page.layout
    elif pathname == '/dashboards/humidity':
        return humidity_dashboard.layout
    elif pathname == '/dashboards/temperature':
        return temperature_dashboard.layout
    # elif pathname == '/utils/dashboard-button':
    #     return dashboard_button.layout
    else:
        return '404'

if __name__ == '__main__':
    app.run_server(debug=True)