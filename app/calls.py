from dash import Input, Output, dash_table
from data import partos_munic_df, partos_geres_df, GERES, geres_lista
from mapas import mapa_municipio

df_partos_munic = partos_munic_df()
df_partos_geres = partos_geres_df()
lista_geres = geres_lista()

def callbacks(app):
    @app.callback(
        Output("mapa", "figure"),
        Output("tabela", "children"),
        Input("drop-geres", "value"),
        Input("drop-tipo-parto", "value")
    )
    def mapa(geres, tipo):
        if len(geres) == 0:
            series_valor = df_partos_munic[lista_geres].sum(numeric_only=True, axis=1)
        elif len(geres) == 1:
            series_valor = df_partos_munic[geres[0]].fillna(0)
        else:
            series_valor = df_partos_munic[geres].sum(numeric_only=True, axis=1)
        
        df_partos_munic['valor'] = series_valor.astype('int32')
        
        df = df_partos_munic[
            ['cd_munic', 'municipio', 'geresnome', 'TIPO_PARTO', 'valor']
        ]

        if tipo in ['Normal/Cesário', 'De Risco']:
            df.query('TIPO_PARTO == @tipo', inplace=True)     
        else:
            df = df.groupby(
                ['cd_munic', 'municipio', 'geresnome'], 
                as_index=False
                )['valor'].sum()
         
        # df.rename(columns={geres: 'valor'}, inplace=True)

        # TABELA
        df_tab = df[['municipio', 'geresnome', 'valor']]
        df_tab.columns = ['Município', 'GERES', 'Partos']
        df_tab.sort_values('Partos', ascending=False, inplace=True)
        
        data_table = dash_table.DataTable(
            id='table-municipios',
            columns=[{"name": i, "id": i} for i in df_tab.columns],
            data=df_tab.to_dict("records"),
            fixed_rows={"headers": True},
            page_size=9,
            style_table={"overflowX": "auto", "overflowY": "auto"},
            style_header={
                "backgroundColor": "rgb(230, 230, 230)",
                "fontWeight": "bold"
            },
            style_cell={
                "font_family": "sans-serif",
                "textAlign": "left",
                "padding": "7px",
                "font-size": "12px",
                "height": "auto",
                "whiteSpace": "normal",
                "minWidth": 30, 
                "maxWidth": 40, 
                "width": 35
            }
        )

        return (mapa_municipio(df, tipo), data_table)
    
    @app.callback(
        Output("tabela-geres", "children"),
        Input("drop-geres", "value"),
        Input("drop-tipo-parto", "value")
    )
    def mapa(geres, tipo):
        if tipo in ['Normal/Cesário', 'De Risco']:
            df = df_partos_geres.query('TIPO_PARTO == @tipo')     
        else:
            df = df_partos_geres.groupby('geres_internacao', as_index=False).sum()
        
        df = df[['geres_internacao'] + lista_geres]
        df.rename(columns={'geres_internacao': 'GERES Internação'}, inplace=True)

        data_table = dash_table.DataTable(
            id='table-geres',
            columns=[{"name": i, "id": i} for i in df.columns],
            data=df.to_dict("records"),
            fixed_rows={"headers": True},
            style_table={"overflowX": "auto", "overflowY": "auto"},
            style_header={
                "backgroundColor": "rgb(230, 230, 230)",
                "fontWeight": "bold"
            },
            style_data={
                'color': 'black',
                'backgroundColor': 'white'
            },
            style_data_conditional=[
                {
                    'if': {'row_index': 'odd'},
                    'backgroundColor': 'rgb(220, 220, 220)',
                }
        ],
            style_cell={
                "font_family": "sans-serif",
                "textAlign": "left",
                "padding": "7px",
                "font-size": "12px",
                "height": "auto",
                "whiteSpace": "normal",
                "minWidth": 30, 
                "maxWidth": 40, 
                "width": 35
            },
            style_cell_conditional=[
                {
                    'if': {'column_id': c},
                    'textAlign': 'right'
                } for c in lista_geres
            ],
        )

        return data_table
        
