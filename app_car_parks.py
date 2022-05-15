import streamlit as st
import def_car_parks
from streamlit_folium import st_folium
from time import sleep


def rerun(x):
    sleep(x)
    st.experimental_rerun()


def show_car_parks():
    with st.sidebar:
        with st.form("Automatic updates"):
            updating = st.checkbox("Keep updating?", value=False)
            pause = st.number_input("Update frequency in seconds", value=1800, format='%d')

            st.form_submit_button("Submit")

    st.write("""# Cork car parks""")

    m = def_car_parks.make_map()
    st_folium(m, height=400, width=800)

    if updating:
        rerun(pause)
