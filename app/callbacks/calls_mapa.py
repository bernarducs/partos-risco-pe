from dash import Input, Output, dash_table

from ..data import filter_dataset
from ..mapas import mapa_municipio


def mapa(app):
    @app.callback(
        Output('mapa', 'figure'),
        Output('tabela', 'children'),
        Input('drop-geres', 'value'),
        Input('drop-tipo-parto', 'value'),
        Input('drop-gestao', 'value'),
        Input('drop-pontos-estab', 'value'),
    )
    def call_function(geres, tipo, gestao, plotar_pontos):
        mapa_visible = True
        if len(geres) == 0:
            df = filter_dataset()
        else:
            df = filter_dataset(GERES_MOV=geres)

        if tipo in ['Normal/Cesário', 'De Risco']:
            df.query('TIPO_PARTO == @tipo', inplace=True)

        if gestao != 0:
            df.query('GESTAO == @gestao', inplace=True)

        # MAPA
        df_grp = (
            df.groupby(
                ['NM_MUNIC_RES', 'GERES_RES', 'MUNIC_RES'], as_index=False
            )['N_AIH']
            .count()
            .rename(columns={'N_AIH': 'Partos'})
        )

        # TABELA
        df_tab = df_grp[['NM_MUNIC_RES', 'GERES_RES', 'Partos']]
        df_tab.columns = ['Município', 'GERES', 'Partos']
        df_tab_sorted = df_tab.sort_values(by='Partos', ascending=False)

        data_table = dash_table.DataTable(
            id='table-municipios',
            columns=[{'name': i, 'id': i} for i in df_tab_sorted.columns],
            data=df_tab_sorted.to_dict('records'),
            filter_action='native',
            filter_options={'placeholder_text': 'Filtrar...'},
            fixed_rows={'headers': True},
            page_size=9,
            style_table={'overflowX': 'auto', 'overflowY': 'auto'},
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold',
            },
            style_cell={
                'font_family': 'sans-serif',
                'textAlign': 'left',
                'padding': '7px',
                'font-size': '12px',
                'height': 'auto',
                'whiteSpace': 'normal',
                'minWidth': 30,
                'maxWidth': 40,
                'width': 35,
            },
        )

        return (
            mapa_municipio(df_grp, tipo, plotar_pontos), 
            data_table
            )
