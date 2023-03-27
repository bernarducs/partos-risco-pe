from dash import html, dcc
import dash_bootstrap_components as dbc

from data import geres_lista

geres = geres_lista()

drop_geres = dcc.Dropdown(
    id="drop-geres",
    options=[
        {"label": g, "value": g} for g in geres
    ],
    placeholder="GERES",
    value='I GERES - Recife',
    multi=False
)

drop_tipo_partos = dcc.Dropdown(
    id="drop-tipo-parto",
    options=[
        {"label": g, "value": g} for g in ['Normal', 'De Risco', 'Total']
    ],
    placeholder="Partos (tipo)",
    value='Total',
    multi=False
)

comp_filtros = html.Div(dbc.Row(
    [
        dbc.Col([drop_geres]),
        dbc.Col([drop_tipo_partos])
    ], 
    style={
        'width': '800px', 
        'margin': '2rem',
        }
    ), style={'display': 'inline', 'align-items': 'center'})