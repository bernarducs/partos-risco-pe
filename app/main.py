import dash_bootstrap_components as dbc
from dash import Dash, dcc, html

from calls import callbacks
from componentes.header import header
from componentes.footer import footer
from componentes.filtros import comp_filtros


external_stylesheets=[
    dbc.themes.LUMEN,
    '/app/assets/style.css' 
    ]

app = Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div([
    header,
    comp_filtros,
    html.Div([
        dbc.Row([
            dbc.Col(dcc.Graph(id='mapa'), width=8),
            dbc.Col([
                dbc.Row(html.P("Município de residência")),
                dbc.Row(id='tabela')
            ], width=4)
        ], style={'margin-bottom': '2rem'}, justify='between'),
        dbc.Row([
            dbc.Col(html.H4("GERES de Ocorrência x Residência")),
        ]),
        dbc.Row([
            dbc.Col(html.P("A tabela abaixo mostra a relação entre as regionais onde acontecem os partos (linhas) e as regionais demandantes (colunas)")),
        ]),
        dbc.Row([
            dbc.Col(id='tabela-geres'),
        ]),
    ],
        style={'margin-left': '2rem', 'margin-right': '2rem'}),
    footer
], className='comps')

callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=False)
