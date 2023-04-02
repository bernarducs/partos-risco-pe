from dash import html
import dash_bootstrap_components as dbc


descricao_tabela = 'A tabela abaixo mostra a relação entre as regionais ' \
    'onde acontecem os partos (linhas) e as regionais demandantes (colunas)'

tab_geres = html.Div([
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
                    descricao_tabela
                )
            ),
        ]
    ),
    dbc.Row(
        [
            dbc.Col(id='tabela-geres'),
        ]
    ),
], style={'margin-left': '2rem', 'margin-right': '2rem'})