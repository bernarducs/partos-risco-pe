import json
import pandas as pd
import os

DATADIR = os.getcwd() + '/partos_risco_pe/datasets'

def partos_df():
    return pd.read_parquet(
        f'{DATADIR}/partos_por_municipio_2019_2022.parquet.gzip'
        )


def geres_lista():
    df = partos_df().sort_values('cod_geres')
    return df['geresnome'].drop_duplicates().dropna().tolist()


def municipios_poligono():
    with open(f'{DATADIR}//municipios.geojson') as json_file:
        municipios_geo = json.load(json_file)

    for munic_feat in municipios_geo.get('features'):
        geocod = munic_feat.get('properties')['GEOCODIGO']
        munic_feat.get('properties')['id'] = str(geocod)[:6]
        munic_feat.get('properties')['GEOCODIGO'] = str(geocod)[:6]
    
    return municipios_geo