import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

header = html.Header(
    html.H1(['Mapa de partos em Pernambuco']),
    style={
        'text-align':'center', 
        'padding': '2rem',
        'color': 'white',
        'background-color': '#0f3057'
        }
    )