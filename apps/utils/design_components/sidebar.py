import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, dcc, html

from apps import home_page
from apps.dashboards import humidity_dashboard, temperature_dashboard, photoresistor_dashboard

from app import app

