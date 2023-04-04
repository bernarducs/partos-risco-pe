import json

import pandas as pd

DATASETS = 'app/datasets/outputs'
PROCED_ID = {
    '0310010039': ['Normal', 'PARTO NORMAL'],
    '0310010055': ['Normal', 'PARTO NORMAL EM CENTRO DE PARTO NORMAL (CPN)'],
    '0411010034': ['Cesário', 'PARTO CESARIANO'],
    '0411010042': ['Cesário', 'PARTO CESARIANO C/ LAQUEADURA TUBARIA'],
    '0310010047': ['De Risco', 'PARTO NORMAL EM GESTACAO DE ALTO RISCO'],
    '0411010026': ['De Risco', 'PARTO CESARIANO EM GESTACAO ALTO RISCO'],
}
GRUPO_PROCED = {
    'Normal/Cesário': ['0310010039', '0310010055', '0411010034', '0411010042'],
    'De Risco': ['0310010047', '0411010026'],
}


def geres_df():
    return pd.read_parquet(f'{DATASETS}/localidade_pe.parquet.gzip')


def geres_nomes():
    df = geres_df()
    return df['geresnome'].unique().tolist()


def tipo_parto_df():
    return (
        pd.DataFrame.from_dict(GRUPO_PROCED, orient='index')
        .T.stack()
        .reset_index()
        .rename(columns={'level_1': 'TIPO_PARTO', 0: 'PROC_REA'})
        .drop('level_0', axis=1)
    )
    

def estabelecimentos_df():
    """
    Retorna o dataframe de hospitais, leitos e pontos (lat, lng)
    """
    return pd.read_parquet(f'{DATASETS}/estabelecimentos_leitos_pontos.parquet.gzip')


def municipios_poligono():
    """
    Retorna o polígono (camada) dos municípios pernambucanos
    """
    with open(f'{DATASETS}/municipios.geojson') as json_file:
        municipios_geo = json.load(json_file)

    for munic_feat in municipios_geo.get('features'):
        geocod = munic_feat.get('properties')['GEOCODIGO']
        munic_feat.get('properties')['id'] = str(geocod)[:6]
        munic_feat.get('properties')['GEOCODIGO'] = str(geocod)[:6]

    return municipios_geo


def dataset():
    return pd.read_parquet(f'{DATASETS}/partos_pe_reduz.parquet.gzip')
    # df_geres = geres_df()
    # df_tipo_parto = tipo_parto_df()

    # df_partos = (
    #     df.reset_index()
    #     .merge(
    #         df_geres[['codmunres', 'municipio', 'geresnome']],
    #         how='left',
    #         left_on='MUNIC_RES',
    #         right_on='codmunres',
    #     )
    #     .drop('codmunres', axis=1)
    #     .rename(
    #         columns={'geresnome': 'GERES_RES', 'municipio': 'NM_MUNIC_RES'}
    #     )
    #     .merge(
    #         df_geres[['codmunres', 'geresnome']],
    #         how='left',
    #         left_on='MUNIC_MOV',
    #         right_on='codmunres',
    #     )
    #     .drop('codmunres', axis=1)
    #     .rename(
    #         columns={'geresnome': 'GERES_MOV', 'municipio': 'NM_MUNIC_MOV'}
    #     )
    #     .merge(df_tipo_parto, how='left', on='PROC_REA')
    # )

    # return df_partos[
    #     [
    #         'N_AIH', 
    #         'GESTAO', 
    #         'MUNIC_RES', 
    #         'MUNIC_MOV', 
    #         'PROC_REA', 
    #         'NM_MUNIC_RES', 
    #         'GERES_RES', 
    #         'GERES_MOV', 
    #         'TIPO_PARTO'
    #         ]
    #     ]


def _queries_concat(queries):
    q = [
        f'{k} == {v if type(v) == list else [str(v)]}'
        for k, v in queries.items()
    ]
    query = ' & '.join(q)
    return query


def filter_dataset(**kwargs):
    df = dataset()
    query = _queries_concat(kwargs)
    if query:
        return df.query(query)
    return df
