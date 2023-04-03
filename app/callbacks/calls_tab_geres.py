from dash import Input, Output, dash_table

from ..data import GRUPO_PROCED, filter_dataset, geres_nomes

geres_nomes = geres_nomes()


def tab_geres_partos(app):
    @app.callback(
        Output('tabela-geres', 'children'),
        Input('drop-geres', 'value'),
        Input('drop-tipo-parto', 'value'),
        Input('drop-gestao', 'value'),
    )
    def call_function(geres, tipo, gestao):
        if tipo in ['Normal/Cesário', 'De Risco']:
            df = filter_dataset(TIPO_PARTO=tipo)
        else:
            df = filter_dataset()

        if gestao != 0:
            df.query('GESTAO == @gestao', inplace=True)

        df_pivot = (
            df.groupby(['GERES_MOV', 'GERES_RES'], as_index=False)['N_AIH']
            .count()
            .pivot_table(
                index='GERES_MOV',
                columns='GERES_RES',
                values='N_AIH',
                aggfunc='sum',
                fill_value=0,
                margins=True,
                margins_name='Total',
            )
            .reset_index()
        )

        df_pivot.rename(
            columns={'GERES_MOV': 'GERES Intern. (linhas) / Resid. (colunas)'},
            inplace=True,
        )

        data_table = dash_table.DataTable(
            id='table-geres',
            columns=[{'name': i, 'id': i} for i in df_pivot.columns],
            data=df_pivot.to_dict('records'),
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
                for c in df_pivot.columns[1:]
            ],
        )
        return data_table
