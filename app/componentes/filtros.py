from dash import html, dcc
import dash_bootstrap_components as dbc

from data import geres_lista

geres = geres_lista()

drop_geres = dcc.Dropdown(
    id="drop-geres",
    options=[
        {"label": g, "value": g} for g in geres
    ],
    placeholder="Escolha uma GERES",
    value=['I GERES - Recife'],
    clearable=False,
    multi=True
)

drop_tipo_partos = dcc.Dropdown(
    id="drop-tipo-parto",
    options=[
        {"label": g, "value": g} for g in ['Normal/Cesário', 'De Risco', 'Total']
    ],
    placeholder="Partos (tipo)",
    value='Total',
    clearable=False,
    multi=False
)

instrucoes = "O mapa abaixo traz a abragência de partos realizados de acordo com a \
    GERES selecionada ao lado. Os círculos são estabelecimentos (hospitais) \
        divididos entre aqueles que realizam partos ou não.  Utilize o \
            filtro ao lado para alternar entre partos normais+cesário \
                e aqueles que foram de risco."

comp_filtros = html.Div(dbc.Row(
    [
        dbc.Col([html.P(instrucoes)]),
        dbc.Col([dbc.Stack([dbc.Row(drop_geres), dbc.Row(drop_tipo_partos)], gap=2)])
    ], 
    style={
        'width': '1000px', 
        'margin': '2rem 1rem ',
        }
    ), style={
        'display': 'inline', 
        'align-items': 'center', 
        'font-size': '14px',
        }
    )