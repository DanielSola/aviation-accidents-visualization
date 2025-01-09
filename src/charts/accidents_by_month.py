import streamlit as st
import plotly.express as px
import pandas as pd

def accidents_by_month(data):
    # Drop rows with missing Event.Date
    data = data.dropna(subset=["Event.Date"])

    # Extract month from Event.Date
    data["Month"] = data["Event.Date"].dt.month

    # Count the number of accidents per month
    accidents_per_month = data["Month"].value_counts().sort_index().reset_index()
    accidents_per_month.columns = ["Month", "Accidents"]

    # Map month numbers to month names
    month_names = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
    accidents_per_month["Month"] = accidents_per_month["Month"].map(month_names)

    # Create the bar chart with color proportional to the number of accidents
    fig = px.bar(accidents_per_month, x="Month", y="Accidents", title="Accidents by Month of the Year", labels={"Month": "Month", "Accidents": "Number of Accidents"},
                 color="Accidents", color_continuous_scale="Reds")

    # Update layout to tilt x-axis labels by 45 degrees
    fig.update_layout(xaxis_tickangle=-45)

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)

    # Add a brief paragraph explaining the peak in July
    st.markdown("""
    The chart shows a peak in the number of aviation accidents in July, with more than 10,000 accidents. 
    This trend could be due to increased air traffic during the summer months, as more people travel for vacations and holidays.
    """)