import plotly.graph_objects as go

from data import partos_df, municipios_poligono

munic_poligono = municipios_poligono()


def mapa_municipio(df, tipo):
    df_metricas = df[['valor']].describe()

    fig = go.Figure(
        go.Choroplethmapbox(
            name="",
            geojson=munic_poligono, 
            featureidkey="properties.GEOCODIGO", 
            locations=df["cd_munic"],
            z=df['valor'],

            # HOVER    
            hovertext=[
                '{}<br>{}'.format(txt_vals[0], txt_vals[1]) 
                for txt_vals in df[
                    ['municipio', 'geresnome']
                    ].values
            ],
            # hoverinfo="text+z",
            hovertemplate="Partos:  %{z:,.0d} <br>%{hovertext}",
            
            # COLOBAR
            colorscale='Sunsetdark',
            colorbar=dict(
                # title="Partos de Risco",
                # orientation="h",
                outlinewidth=0,
                tickvals=[0, 1000],
                ticktext=[
                    df_metricas.loc['min'], 
                    # df_metricas.loc['75%'], 
                    df_metricas.loc['max'], 
                ],
                # separatethousands=True,
                tickfont=dict(
                    family='Arial',
                    size=12,
                ),
                tickformat="%{:,.2f}"
            ), 
            zmin=0, 
            zmax=1000,
            marker_opacity=0.5, 
            marker_line_width=0,
            )
        )

    fig.update_layout(
        title=f"Partos - {tipo} (2019-2022)",
        margin={"r":0,"t":25,"l":0,"b":0},
        height=500,
        mapbox_style="carto-positron",
        mapbox_zoom=6, 
        mapbox_center = {"lat": -8.5517, "lon": -37.7073},
        hoverlabel=dict(
            font_size=16,
            )
        )

    return fig