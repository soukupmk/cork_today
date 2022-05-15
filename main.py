import streamlit as st
import app_car_parks
import app_city_parks


##################
# MAIN APP ####
##################

with st.sidebar:
    app_choice = st.radio("Choose what you want to explore", ["Car parks", "City parks"])


if app_choice == "Car parks":
    app_car_parks.show_car_parks()
elif app_choice == 'City parks':
    app_city_parks.show_city_parks()
