import json
import os

import pandas as pd

DATADIR = os.getcwd() + '/app/datasets/outputs'

GERES = {
    '2601 Recife': 'I GERES - Recife',
    '2602 Limoeiro': 'II GERES - Limoeiro',
    '2603 Palmares': 'III GERES - Palmares',
    '2604 Caruaru': 'IV GERES - Caruaru',
    '2605 Garanhuns': 'V GERES - Garanhuns',
    '2606 Arcoverde': 'VI GERES - Arcoverde',
    '2607 Salgueiro': 'VII GERES - Salgueiro',
    '2608 Petrolina': 'VIII GERES - Petrolina',
    '2609 Ouricuri': 'IX GERES - Ouricuri',
    '2610 Afogados da Ingazeira': 'X GERES - Afogados da Ingazeira',
    '2611 Serra Talhada': 'XI GERES - Serra Talhada',
    '2612 Goiana': 'XII GERES - Goiana',
}


def partos_munic_df():
    """
    Retorna o dataframe de partos normais e de risco por municipio
    """
    return pd.read_parquet(
        f'{DATADIR}/partos_por_municipio_2019_2022.parquet.gzip'
    )


def partos_geres_df():
    """
    Retorna o dataframe de partos normais e de risco por geres
    """
    return pd.read_parquet(
        f'{DATADIR}/partos_por_geres_2019_2022.parquet.gzip'
    )


def hospitais_df():
    """
    Retorna o dataframe de hospitais, leitos e pontos (lat, lng)
    """
    return pd.read_parquet(f'{DATADIR}/estabelecimentos.parquet.gzip')


def municipios_poligono():
    """
    Retorna o polígono (camada) dos municípios pernambucanos
    """
    with open(f'{DATADIR}//municipios.geojson') as json_file:
        municipios_geo = json.load(json_file)

    for munic_feat in municipios_geo.get('features'):
        geocod = munic_feat.get('properties')['GEOCODIGO']
        munic_feat.get('properties')['id'] = str(geocod)[:6]
        munic_feat.get('properties')['GEOCODIGO'] = str(geocod)[:6]

    return municipios_geo


def geres_lista():
    """
    Retorna a lista de GERES
    """
    df = partos_munic_df().sort_values('cod_geres')
    return df['geresnome'].drop_duplicates().dropna().tolist()
