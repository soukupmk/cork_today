import requests
import numpy as np
import pandas as pd
from time import time
import folium
import streamlit as st


@st.cache
def load_data():
    url = 'https://data.corkcity.ie/api/3/action/datastore_search?resource_id=f4677dac-bb30-412e-95a8-d3c22134e3c0&limit=500'
    r = requests.get(url)
    data0 = pd.DataFrame.from_dict(dict(r.json())['result']['records']).astype({'date': 'datetime64'})
    data0.to_pickle(f"car_parks_data/parking_{str(int(time()))}.pickle")
    return data0


def make_map():
    df = load_data()

    m = folium.Map(location=df[['latitude', 'longitude']].mean().tolist(),
                   zoom_start=13)

    shares = np.array([0., 0.2, 0.4, 0.6, 0.8, 1.])
    colors = ['darkred', 'red', 'lightred', 'lightgreen', 'green', 'darkgreen']

    for idx, row in df.iterrows():
        popup_html = f"""
        <b> {row['name']} </b> <br>
        Total spaces: {row['spaces']} <br>
        Free spaces: {row['free_spaces']} <br>
        Occupied share: {100 - row['free_spaces'] / row['spaces'] * 100:.1f}% <br>
        Time of record: {row['date']}
        """
        share = row['free_spaces'] / row['spaces']
        folium.Marker(row[['latitude', 'longitude']].values.tolist(),
                      popup=folium.Popup(popup_html, max_width=500),
                      icon=folium.Icon(color=colors[np.argmin(np.abs(shares - share))])
                      ).add_to(m)
    return m
