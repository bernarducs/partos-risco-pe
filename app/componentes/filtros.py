import dash_bootstrap_components as dbc
from dash import dcc, html
from ..data_ import geres_nomes

geres = geres_nomes()

drop_geres = dcc.Dropdown(
    id='drop-geres',
    options=[{'label': g, 'value': g} for g in geres],
    placeholder='Escolha uma GERES',
    value=['I GERES - Recife'],
    clearable=False,
    multi=False,
)

drop_tipo_partos = dcc.Dropdown(
    id='drop-tipo-parto',
    options=[
        {'label': g, 'value': g}
        for g in ['Todos os partos', 'Normal/Cesário', 'De Risco']
    ],
    placeholder='Partos (tipo)',
    value='Todos os partos',
    clearable=False,
    multi=False,
)

drop_pontos_estab = dcc.Dropdown(
    id='drop-pontos-estab',
    options=[
        {'label': 'Todos os estabelecimentos plotados', 'value': 'todos'},
        {
            'label': 'Plotar apenas estab. COM leitos obstétricos',
            'value': 'com',
        },
        {
            'label': 'Plotar apenas estab. SEM leitos obstétricos',
            'value': 'sem',
        },
        {'label': 'Plotar nenhum estabelecimento', 'value': 'nenhum'},
    ],
    placeholder='Partos (tipo)',
    value='todos',
    clearable=False,
    multi=False,
)

instrucoes = 'O mapa abaixo traz a abragência de partos realizados de acordo com a \
    GERES selecionada ao lado. Os pontos são estabelecimentos (hospitais) \
        divididos entre aqueles que realizam partos ou não.  Utilize o \
            filtro ao lado para alternar entre partos normal/cesário \
                e de risco.'

filtros = html.Div(
    dbc.Row(
        [
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Row(
                                'Introdução:',
                                style={
                                    'margin-bottom': '0.2rem',
                                    'font-weight': 'bold',
                                },
                            ),
                            dbc.Row(instrucoes),
                        ]
                    )
                ],
                sm=12,
                md=12,
                lg=4,
            ),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Row(
                                [
                                    html.P(
                                        ['GERES:'],
                                        style={
                                            'margin-bottom': '0rem',
                                            'font-weight': 'bold',
                                        },
                                    ),
                                    drop_geres,
                                ],
                                style={'margin-bottom': '0.5rem'},
                            ),
                            dbc.Row(
                                [
                                    html.P(
                                        ['Partos:'],
                                        style={
                                            'margin-bottom': '0rem',
                                            'font-weight': 'bold',
                                        },
                                    ),
                                    drop_tipo_partos,
                                ],
                                style={'margin-bottom': '0.5rem'},
                            ),
                        ]
                    )
                ],
                sm=12,
                md=12,
                lg=4,
            ),
            dbc.Col(
                [
                    dbc.Row(
                        [
                            dbc.Row(
                                [
                                    html.P(
                                        ['Plotar estabelecimentos:'],
                                        style={
                                            'margin-bottom': '0rem',
                                            'font-weight': 'bold',
                                        },
                                    ),
                                    drop_pontos_estab,
                                ],
                                style={'margin-bottom': '0.5rem'},
                            )
                        ]
                    )
                ],
                sm=12,
                md=12,
                lg=4,
            ),
        ],
        justify='center',
        style={
            'margin': '2rem 8rem',
        },
    )
)
