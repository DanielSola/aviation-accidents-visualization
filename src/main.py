import pandas as pd
import streamlit as st
import altair as alt
from utils.load_data import load_data
from charts.accidents_by_year import accidents_by_year
from charts.accidents_by_carrier import accidents_by_carrier
from charts.accidents_by_phase import accidents_by_phase
from charts.accidents_by_air_carrier import accidents_by_air_carrier
from charts.accidents_by_purpose_of_flight import accidents_by_purpose_of_flight

def main():
    st.title("Aviation Accidents Dashboard")

    data = load_data()

    # Create tabs for different sections of the dashboard
    tab1, tab2, tab3, tab4, tab5 = st.tabs(["Accidents by Year", "Accidents by Carrier", "Accidents by Phase", "Accidents by Air Carrier", "Accidents by Purpose of Flight"])

    with tab1:
        st.header("Accidents by Year")
        accidents_by_year(data)

    with tab2:
        st.header("Accidents by Carrier")
        accidents_by_carrier(data)

    with tab3:
        st.header("Accidents by Phase")
        accidents_by_phase(data)

    with tab4:
        st.header("Accidents by Air Carrier")
        accidents_by_air_carrier(data)

    with tab5:
        st.header("Accidents by Purpose of Flight")
        accidents_by_purpose_of_flight(data)

if __name__ == "__main__":
    main()