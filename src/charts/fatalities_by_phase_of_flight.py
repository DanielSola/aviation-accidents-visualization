import streamlit as st
import plotly.express as px
import pandas as pd

def fatalities_by_phase_of_flight(data):
    # Drop missing values for the Broad.phase.of.flight and Total.Fatal.Injuries columns
    data = data.dropna(subset=["Broad.phase.of.flight", "Total.Fatal.Injuries"])

    # Group by Broad.phase.of.flight and sum the Total.Fatal.Injuries
    phase_fatalities = data.groupby("Broad.phase.of.flight")["Total.Fatal.Injuries"].sum().reset_index()

    # Filter out phases with zero fatalities
    phase_fatalities = phase_fatalities[phase_fatalities["Total.Fatal.Injuries"] > 0]

    # Calculate the total number of fatalities
    total_fatalities = phase_fatalities["Total.Fatal.Injuries"].sum()

    # Calculate the percentage of fatalities for each phase
    phase_fatalities["Percentage"] = (phase_fatalities["Total.Fatal.Injuries"] / total_fatalities) * 100

    # Round the percentages to one decimal place
    phase_fatalities["Percentage"] = phase_fatalities["Percentage"].round(1)

    # Sort the phases by percentage of fatalities in descending order
    phase_fatalities = phase_fatalities.sort_values(by="Percentage", ascending=False)

    # Create the bar chart
    fig = px.bar(phase_fatalities, x='Broad.phase.of.flight', y='Percentage', 
                 title='Fatalities by Phase of Flight (Percentage)', labels={'Broad.phase.of.flight': 'Phase of Flight', 'Percentage': 'Percentage of Fatalities'},
                 color='Percentage', color_continuous_scale='Reds')

    # Update layout to tilt x-axis labels by 45 degrees
    fig.update_layout(xaxis_tickangle=-45)

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)

    st.markdown(
    """
    As the chart shows, landing accidents are more frequent but less severe in terms of fatality rates.
    In contrast, cruise represents the highest percentage of fatalities. Accidents during this phase are more likely to result in fatalities, likely due to higher altitudes or operational risks. 
    """
    )


