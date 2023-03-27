import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

from calls import callbacks
from comps.header import header
from comps.footer import footer
from comps.filtros import comp_filtros



app = Dash(__name__, external_stylesheets=[dbc.themes.LUMEN])

app.layout = html.Div([
    header,
    comp_filtros,
    html.Div(
        dbc.Row([
            dbc.Col(dcc.Graph(id='mapa')),
            dbc.Col(id='tabela')
        ], style={'margin-bottom': '2rem'}),
        style={'margin-left': '3rem', 'margin-right': '3rem'}
    ),
    # dbc.Row([
    #     dbc.Col(id='tabela')
    # ]),
    footer
])

callbacks(app)

if __name__ == '__main__':
    app.run_server(debug=True)
