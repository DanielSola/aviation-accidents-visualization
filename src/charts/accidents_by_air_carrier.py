import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import numpy as np
import os

def accidents_by_air_carrier(data):
    # Drop missing values for the Air.Carrier column
    data = data.dropna(subset=["Air.carrier"])

    # Count the occurrences of each air carrier
    air_carrier_counts = data.groupby(["Air.carrier"]).size().reset_index(name="Accidents")
    air_carrier_counts = air_carrier_counts[air_carrier_counts["Accidents"] >= 10]
    air_carrier_counts = air_carrier_counts.nlargest(50, 'Accidents')

    # Create the treemap
    fig = px.treemap(air_carrier_counts, path=['Air.carrier'], values='Accidents', 
                     title='Accidents by Air Carrier', color='Accidents', color_continuous_scale='Blues')

    fig.update_traces(textinfo='label', textposition='middle center')

    # Display the treemap in Streamlit
    st.plotly_chart(fig)