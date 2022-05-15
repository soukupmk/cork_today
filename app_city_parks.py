import streamlit as st
import def_city_parks
from streamlit_folium import st_folium


def show_city_parks():

    st.write("""# Cork city parks""")

    m = def_city_parks.make_map()
    st_folium(m, height=400, width=800)
