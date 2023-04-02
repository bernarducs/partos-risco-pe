from ..data import geres_lista, partos_geres_df, partos_munic_df
from ..mapas import mapa_municipio

from .calls_mapa import mapa
from .calls_tab_geres import tab_geres_partos


df_partos_munic = partos_munic_df()
df_partos_geres = partos_geres_df()
lista_geres = geres_lista()


def callbacks(app):
    mapa(app, mapa_municipio, lista_geres, df_partos_munic)
    tab_geres_partos(app, lista_geres, df_partos_geres)

    # @app.callback(
    #     Output('foo', 'children'),
    #     Input('drop-pontos-estab', 'value'),
    # )
    # def mapa(pontos_estab_leitos):
    #     return pontos_estab_leitos