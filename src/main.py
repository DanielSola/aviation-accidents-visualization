import pandas as pd
import streamlit as st
import altair as alt
from utils.load_data import load_data
from charts.accidents_by_year import accidents_by_year
from charts.accidents_by_carrier import accidents_by_carrier
from charts.accidents_by_phase_donut import accidents_by_phase
from charts.accidents_by_air_carrier import accidents_by_air_carrier
from charts.accidents_by_purpose_of_flight import accidents_by_purpose_of_flight
from charts.fatalities_by_air_carrier import fatalities_by_air_carrier
from charts.fatalities_by_phase_of_flight import fatalities_by_phase_of_flight
from charts.accidents_by_month import accidents_by_month
from charts.accidents_by_day_of_week import accidents_by_day_of_week
from charts.accidents_by_phase_bubbles import accidents_by_phase_bubbles

def main():
    st.title("Aviation Accidents Dashboard")

    st.write('Select a perspective to analyze aviation accidents')

    data = load_data()

    # Create tabs for different sections of the dashboard
    tab1, tab2, tab3, tab4 = st.tabs(["By Time", "By Carrier", "By Phase", "By Purpose of Flight"])

    with tab1:
        accidents_by_year(data)
        accidents_by_month(data)
        accidents_by_day_of_week(data)

    with tab2:
        #st.header("Accidents by Carrier")
        accidents_by_carrier(data)
        fatalities_by_air_carrier(data)

    with tab3:
        #st.header("Accidents by Phase")
        accidents_by_phase(data)
        fatalities_by_phase_of_flight(data)

    with tab4:
        #st.header("Accidents by Purpose of Flight")
        accidents_by_purpose_of_flight(data)

if __name__ == "__main__":
    main()