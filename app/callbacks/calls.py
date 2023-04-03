from .calls_mapa import mapa
from .calls_tab_geres import tab_geres_partos


def callbacks(app):
    mapa(app)
    tab_geres_partos(app)

    # @app.callback(
    #     Output('foo', 'children'),
    #     Input('drop-pontos-estab', 'value'),
    # )
    # def mapa(pontos_estab_leitos):
    #     return pontos_estab_leitos