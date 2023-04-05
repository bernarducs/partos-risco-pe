import dash_bootstrap_components as dbc
from dash import dcc, html

mapa = html.Div(
    [
        dbc.Row(
            [
                dbc.Col(dcc.Loading(dcc.Graph(id='mapa')), sm=12, md=8, lg=8),
                dbc.Col(
                    [
                        dbc.Row(
                            html.P('Município de residência'),
                            style={'font-weight': 'bold'},
                        ),
                        dcc.Loading(dbc.Row(id='tabela')),
                    ],
                    sm=12,
                    md=4,
                    lg=4,
                ),
            ],
            style={'margin-bottom': '2rem'},
            justify='between',
        ),
    ],
    style={'margin-left': '2rem', 'margin-right': '2rem'},
)
