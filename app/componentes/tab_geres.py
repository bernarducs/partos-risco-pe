import dash_bootstrap_components as dbc
from dash import html

descricao_tabela = (
    'A tabela abaixo mostra a relação entre as regionais '
    'onde acontecem os partos (linhas) e as regionais demandantes (colunas). '
    'É reativa apenas aos filtros "Partos" e "Gestão."'
)

tab_geres = html.Div(
    [
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
        dbc.Row([dbc.Col(html.P(descricao_tabela), width=4)]),
        dbc.Row(
            [
                dbc.Col(id='tabela-geres'),
            ]
        ),
    ],
    style={'margin-left': '2rem', 'margin-right': '2rem'},
)
