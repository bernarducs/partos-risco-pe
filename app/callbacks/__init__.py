from .calls_mapa import mapa
from .calls_tab_geres import tab_geres_partos
from .calls_munic_propria_geres import munic_propria_geres


def callbacks(app):
    mapa(app)
    tab_geres_partos(app)
    munic_propria_geres(app)

    # @app.callback(
    #     Output('foo', 'children'),
    #     Input('drop-pontos-estab', 'value'),
    # )
    # def mapa(pontos_estab_leitos):
    #     return pontos_estab_leitos
