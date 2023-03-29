import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

footer = html.Footer(
    [
        html.P(
            ['Secretaria de Planejamento, Gestão e Desenvolvimento Regional']
        ),
        html.P(['SEPLAG-PE']),
    ],
    style={
        'text-align': 'center',
        'padding': '2rem',
        'margin-top': '10rem',
        'background-color': '#eee',
    },
)
