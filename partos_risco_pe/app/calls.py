from dash import Input, Output, dash_table
from data import partos_df
from mapas import mapa_municipio

df_partos = partos_df()

def callbacks(app):
    @app.callback(
        Output("mapa", "figure"),
        Output("tabela", "children"),
        Input("drop-geres", "value"),
        Input("drop-tipo-parto", "value")
    )
    def mapa(geres, tipo):
        nome_geres = geres.split(' - ')[1]
        col = [col for col in df_partos.columns if nome_geres in col][0]
        df = df_partos[['cd_munic', 'municipio', 'geresnome', 'TIPO_PARTO', col]]

        if tipo in ['Normal', 'De Risco']:
            df.query('TIPO_PARTO == @tipo', inplace=True)     
        else:
            df = df.groupby(
                ['cd_munic', 'municipio', 'geresnome'], 
                as_index=False
                )[col].sum()
         
        df.rename(columns={col: 'valor'}, inplace=True)

        print(df.head())

        # TABELA
        df_tab = df[['municipio', 'geresnome', 'valor']]
        df_tab.columns = ['Município', 'GERES', 'Partos']
        df_tab.sort_values('Partos', ascending=False, inplace=True)
        
        data_table = dash_table.DataTable(
            id='table',
            columns=[{"name": i, "id": i} for i in df_tab.columns],
            data=df_tab.to_dict("records"),
            fixed_rows={"headers": True},
            style_table={"overflowX": "auto", "overflowY": "auto"},
            style_header={
                "backgroundColor": "rgb(230, 230, 230)",
                "fontWeight": "bold"
            },
            style_cell={
                "font_family": "sans-serif",
                "textAlign": "left",
                "padding": "7px",
                "height": "auto",
                "whiteSpace": "normal",
                "minWidth": 35, 
                "width": 135
            }
        )

        return (mapa_municipio(df, tipo), data_table)
