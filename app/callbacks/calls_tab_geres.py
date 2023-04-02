from dash import Input, Output, dash_table


def tab_geres_partos(app, lista_geres, df_partos_geres):
    @app.callback(
        Output('tabela-geres', 'children'),
        Input('drop-geres', 'value'),
        Input('drop-tipo-parto', 'value'),
    )
    def mapa(geres, tipo):
        if tipo in ['Normal/Cesário', 'De Risco']:
            df = df_partos_geres.query('TIPO_PARTO == @tipo')
        else:
            df = df_partos_geres.groupby(
                'geres_internacao', as_index=False
            ).sum(numeric_only=True)

        df = df[['geres_internacao'] + lista_geres]
        df.rename(
            columns={'geres_internacao': 'GERES Internação'}, inplace=True
        )

        data_table = dash_table.DataTable(
            id='table-geres',
            columns=[{'name': i, 'id': i} for i in df.columns],
            data=df.to_dict('records'),
            fixed_rows={'headers': True},
            style_table={'overflowX': 'auto', 'overflowY': 'auto'},
            style_header={
                'backgroundColor': 'rgb(230, 230, 230)',
                'fontWeight': 'bold',
            },
            style_data={'color': 'black', 'backgroundColor': 'white'},
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(220, 220, 220)',
                }
            ],
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
            style_cell_conditional=[
                {'if': {'column_id': c}, 'textAlign': 'right'}
                for c in lista_geres
            ],
        )
        return data_table
