import dash_bootstrap_components as dbc
from dash import Dash, html

from app.callbacks import callbacks
from app.componentes import filtros, footer, header, mapa, tab_geres

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
    className='comps',
)

callbacks(app)


if __name__ == '__main__':
    app.run_server(debug=True)
