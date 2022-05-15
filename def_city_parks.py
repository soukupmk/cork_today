import requests
import pandas as pd
import streamlit as st
import folium


@st.cache
def load_data():
    url = "https://data.corkcity.ie/api/3/action/datastore_search?resource_id=6fa2e95d-90a4-4a96-bf30-5d4756f6a777&limit=1000"
    r = requests.get(url)
    data0 = pd.DataFrame.from_dict(dict(r.json())['result']['records'])
    # data0.to_csv(f"city_parks_data/city_parks.csv")
    return data0


def make_map():
    df = load_data()

    m = folium.Map(location=df[['Latitude', 'Longitude']].mean().tolist(),
                   zoom_start=12)

    for idx, row in df.iterrows():
        popup_html = f"""
        <b> {row['Name']} </b> <br>
        Type: {row['Type']}
        """
        folium.Marker(row[['Latitude', 'Longitude']].values.tolist(),
                      popup=folium.Popup(popup_html, max_width=500),
                      icon=folium.Icon(icon='tree', prefix='fa', color='green')
                      ).add_to(m)
    return m