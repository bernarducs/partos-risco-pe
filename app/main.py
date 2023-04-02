import dash_bootstrap_components as dbc
from calls import callbacks
from componentes.filtros import comp_filtros
from componentes.footer import footer
from componentes.header import header
from dash import Dash, dcc, html

external_stylesheets = [dbc.themes.LUMEN, '/app/assets/style.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(
    [
        header,
        comp_filtros,
        html.Div(
            [
                dbc.Row(
                    [
                        dbc.Col(dcc.Graph(id='mapa'), sm=12, md=8, lg=8),
                        dbc.Col(
                            [
                                dbc.Row(
                                    html.P('Município de residência'),
                                    style={'font-weight': 'bold'},
                                ),
                                dbc.Row(id='tabela'),
                            ],
                            sm=12,
                            md=4,
                            lg=4,
                        ),
                    ],
                    style={'margin-bottom': '2rem'},
                    justify='between',
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.P(
                                ['GERES de Ocorrência x Residência'],
                                style={
                                    'margin-bottom': '0rem',
                                    'font-weight': 'bold',
                                },
                            )
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(
                            html.P(
                                'A tabela abaixo mostra a relação entre as regionais onde acontecem os partos (linhas) e as regionais demandantes (colunas)'
                            )
                        ),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(id='tabela-geres'),
                    ]
                ),
                dbc.Row(
                    [
                        dbc.Col(id='foo'),
                    ]
                ),
            ],
            style={'margin-left': '2rem', 'margin-right': '2rem'},
        ),
        footer,
    ],
    className='comps'
)

callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
