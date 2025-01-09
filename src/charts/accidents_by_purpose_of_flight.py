import streamlit as st
import plotly.express as px
import numpy as np
from utils.flight_purpose_selector import flight_purpose_selector

def accidents_by_purpose_of_flight(data):
    # Drop missing values for the Purpose.of.flight column
    data = data.dropna(subset=["Purpose.of.flight"])

    # Replace "Aerial Application" with "Crop Dusting"
    other = ('PUBS', 'PUBL', 'ASHO', 'Air Drop', 'Unknown', 'Aerial Observation')

    data["Purpose.of.flight"] = data["Purpose.of.flight"].replace(other, "Other")


    # Count the occurrences of each purpose of flight
    purpose_counts = data['Purpose.of.flight'].value_counts().reset_index()
    purpose_counts.columns = ['Purpose', 'Accidents']

    # Calculate the percentage of each purpose of flight
    total_accidents = purpose_counts['Accidents'].sum()
    purpose_counts['Percentage'] = (purpose_counts['Accidents'] / total_accidents) * 100

    # Format the Percentage column to remove decimals and add % symbol
    purpose_counts['Percentage'] = purpose_counts['Percentage'].map(lambda x: f"{int(x)}%")

    # Create the bar chart
    fig = px.bar(purpose_counts, x='Purpose', y='Accidents', title='Accidents by Purpose of Flight', labels={'Purpose': 'Purpose of Flight', 'Accidents': 'Number of Accidents'})

    # Update layout to tilt x-axis labels by 45 degrees
    fig.update_layout(xaxis_tickangle=-45)

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)

    st.markdown(
        """
        This chart shows that the majority of accidents occur during personal flights, significantly outnumbering other flight purposes. Instructional, business, and crop-dusting flights follow, while specialized activities like firefighting and glider towing have relatively few accidents.
        """
    )

    flight_purpose_selector(data)
    

