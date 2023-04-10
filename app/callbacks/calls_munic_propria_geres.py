from dash import Input, Output

from ..data import filter_dataset

def munic_propria_geres(app):
    @app.callback(
        Output('kpi-munic-propria-geres', 'children'),
        Input('drop-geres', 'value'),
        Input('drop-tipo-parto', 'value'),
        Input('drop-gestao', 'value'),
        Input('drop-pontos-estab', 'value'),
    )
    def call_function(geres, tipo, gestao, plotar_pontos):
        if len(geres) == 0:
            return ''
        else:
            df = filter_dataset(GERES_RES=geres)

        if tipo in ['Normal/Cesário', 'De Risco']:
            df.query('TIPO_PARTO == @tipo', inplace=True)

        if gestao != 0:
            df.query('GESTAO == @gestao', inplace=True)
        
        partos_geres_total = df.\
            groupby(['GERES_RES'], as_index=False)['N_AIH'].\
            count()

        partos_munic_propria_geres = df.\
            groupby(['GERES_MOV', 'GERES_RES'], as_index=False)['N_AIH'].\
            count().\
            assign(MESMA_GERES=(lambda x: x['GERES_MOV'] == x['GERES_RES'])).\
            query('MESMA_GERES == True').\
            drop(['MESMA_GERES', 'GERES_MOV'], axis=1)

        
        razao_munic_propria_geres = \
            partos_munic_propria_geres.sum(numeric_only=True).div(
                partos_geres_total.sum(numeric_only=True)
            )
        
        txt = 'Total: {:,.0f} | Residentes da mesma regional: {:,.0f} ({:.2%}) '.format(
            partos_geres_total.sum(numeric_only=True).values[0],
            partos_munic_propria_geres.sum(numeric_only=True).values[0],
            razao_munic_propria_geres.values[0]
        )
        return txt
