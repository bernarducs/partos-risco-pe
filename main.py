import dash_bootstrap_components as dbc
from app.callbacks import callbacks
from app.componentes.filtros import filtros
from app.componentes.footer import footer
from app.componentes.header import header
from app.componentes.mapa import mapa
from app.componentes.tab_geres import tab_geres
from dash import Dash, html

external_stylesheets = [dbc.themes.LUMEN, '/app/assets/style.css']

app = Dash(__name__, external_stylesheets=external_stylesheets)

server = app.server
app.layout = html.Div(
    [
        header,
        filtros,
        mapa,
        tab_geres,
        footer,
    ],
    className='comps'
)

callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
