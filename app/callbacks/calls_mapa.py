from dash import Input, Output, dash_table


def mapa(app, mapa_municipio, lista_geres, df_partos_munic):
    @app.callback(
        Output('mapa', 'figure'),
        Output('tabela', 'children'),
        Input('drop-geres', 'value'),
        Input('drop-tipo-parto', 'value'),
        Input('drop-pontos-estab', 'value'),
    )
    def call_function(geres, tipo, plotar_pontos):
        if len(geres) == 0:
            series_valor = df_partos_munic[lista_geres].sum(
                numeric_only=True, axis=1
            )
        elif len(geres) == 1:
            series_valor = df_partos_munic[geres[0]].fillna(0)
        else:
            series_valor = df_partos_munic[geres].sum(
                numeric_only=True, axis=1
            )

        df_partos_munic['valor'] = series_valor.astype('int32')

        df = df_partos_munic[
            ['cd_munic', 'municipio', 'geresnome', 'TIPO_PARTO', 'valor']
        ]

        if tipo in ['Normal/Cesário', 'De Risco']:
            df.query('TIPO_PARTO == @tipo', inplace=True)
        else:
            df = df.groupby(
                ['cd_munic', 'municipio', 'geresnome'], as_index=False
            )['valor'].sum()

        # df.rename(columns={geres: 'valor'}, inplace=True)

        # TABELA
        df_tab = df[['municipio', 'geresnome', 'valor']]
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

        return (mapa_municipio(df, tipo, plotar_pontos), data_table)
