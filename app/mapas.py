import plotly.graph_objects as go
from .data import hospitais_df, municipios_poligono

df_hosp_leitos = hospitais_df()
df_hosp_leitos_com_obst = df_hosp_leitos.query("proced_partos == 'SIM'")
df_hosp_leitos_sem_obst = df_hosp_leitos.query("proced_partos == 'NAO'")

munic_poligono = municipios_poligono()


def point_hover_template(df):
    cols_hover = [
        'estabelecimento',
        'municipio',
        'obst_cirurg',
        'obst_clinica',
        'uti_neo_i',
        'uti_neo_ii',
        'uti_neo_iii',
        'uci_neo_conv',
        'uci_neo_canguru',
    ]
    hover_text = [
        '<b>{}</b><br>{}<br><br><b>Leitos Obstetrícia</b><br>Cirúgicos: {} / Clínica: {}<br><br><b>UTI Neo</b><br>Tipo I: {} / Tipo II: {} / Tipo III: {}<br><br><b>UCI Neo</b><br>Convencional: {} / Caguru: {}'.format(
            txt[0],
            txt[1],
            txt[2],
            txt[3],
            txt[4],
            txt[5],
            txt[6],
            txt[7],
            txt[8],
        )
        for txt in df[cols_hover].values
    ]
    return hover_text


def mapa_municipio(df, tipo, plotar_pontos, mapa_visible):

    ver_estab_com_leitos, ver_estab_sem_leitos = True, True
    if plotar_pontos == 'nenhum':
        ver_estab_com_leitos, ver_estab_sem_leitos = False, False
    elif plotar_pontos == 'com':
        ver_estab_sem_leitos = False
    elif plotar_pontos == 'sem':
        ver_estab_com_leitos = False

    df_metricas = df[['Partos']].describe()

    fig = go.Figure(
        [
            go.Choroplethmapbox(
                visible=mapa_visible,
                name='',
                geojson=munic_poligono,
                featureidkey='properties.GEOCODIGO',
                locations=df['MUNIC_RES'],
                z=df['Partos'],
                # HOVER
                hovertext=[
                    '{}<br>{}'.format(txt_vals[0], txt_vals[1])
                    for txt_vals in df[['NM_MUNIC_RES', 'GERES_MOV']].values
                ],
                # hoverinfo="text+z",
                hovertemplate='Partos:  %{z:,.0d} <br>%{hovertext}',
                # COLOBAR
                colorscale='Sunsetdark',
                colorbar=dict(
                    title='<b>Partos<br></b>',
                    len=0.9,
                    thickness=10,
                    # orientation="h",
                    outlinewidth=0,
                    ticklabelposition='outside bottom',
                    tickvals=[0, 1000],
                    ticktext=[
                        df_metricas.loc['min'],
                        # df_metricas.loc['75%'],
                        df_metricas.loc['max'],
                    ],
                    separatethousands=True,
                    tickfont=dict(
                        family='Arial',
                        size=12,
                    ),
                    tickformat='%{:,.2f}',
                ),
                zmin=0,
                zmax=1000,
                marker_opacity=0.5,
                marker_line_width=0,
                legendrank=1,
            ),
            go.Scattermapbox(
                visible=ver_estab_sem_leitos,
                name='Estabelecimentos SEM leitos obst. em jan/2023',
                lat=df_hosp_leitos_sem_obst['lat'],
                lon=df_hosp_leitos_sem_obst['lng'],
                mode='markers',
                marker=dict(size=14, color='#95BDFF', opacity=0.7),
                hovertext=point_hover_template(df_hosp_leitos_sem_obst),
                hovertemplate='%{hovertext}',
                legendrank=3,
            ),
            go.Scattermapbox(
                visible=ver_estab_com_leitos,
                name='Estabelecimentos COM leitos obst. em jan/2023',
                lat=df_hosp_leitos_com_obst['lat'],
                lon=df_hosp_leitos_com_obst['lng'],
                mode='markers',
                marker=go.scattermapbox.Marker(
                    # size=df_hosp_leitos_com_obst['total_leitos_obstetricos'] / 2.5,
                    size=14,
                    color='#146C94',
                    opacity=0.7,
                ),
                hovertext=point_hover_template(df_hosp_leitos_com_obst),
                hovertemplate='%{hovertext}',
                legendrank=2,
            ),
        ]
    )

    fig.update_layout(
        title={
            'text': f'<b>Partos realizados pela GERES selecionada - {tipo} (2022)</b>',
            'font': {'size': 16, 'family': 'var(--bs-font-sans-serif)'},
        },
        margin={'r': 0, 't': 25, 'l': 0, 'b': 10},
        # height=500,
        mapbox_style='open-street-map',
        # mapbox_zoom=6.8, # quando só na coluna
        mapbox_zoom=6.2,
        mapbox_center={'lat': -8.3517, 'lon': -38.0073},
        hoverlabel=dict(
            font_size=14,
        ),
        legend=dict(
            orientation='h', yanchor='bottom', y=0.90, xanchor='right', x=1
        ),
    )

    return fig
