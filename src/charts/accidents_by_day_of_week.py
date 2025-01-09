from pprint import pp
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import circlify

def accidents_by_day_of_week(data):
    # Convert Event.Date to datetime format
    data["Event.Date"] = pd.to_datetime(data["Event.Date"], errors='coerce')

    # Drop rows with missing Event.Date
    data = data.dropna(subset=["Event.Date"])

    # Extract day of the week from Event.Date
    data["DayOfWeek"] = data["Event.Date"].dt.day_name()

    # Count the number of accidents per day of the week
    accidents_per_day = data["DayOfWeek"].value_counts().reset_index()
    accidents_per_day.columns = ["DayOfWeek", "Accidents"]

    # Calculate the percentage of accidents for each day
    total_accidents = accidents_per_day["Accidents"].sum()
    accidents_per_day["Percentage"] = (accidents_per_day["Accidents"] / total_accidents) * 100

    # Sort the data by percentage in descending order to place larger values in the middle
    accidents_per_day = accidents_per_day.sort_values("Percentage", ascending=False)

    # Prepare data for circlify
    colours = ['#8dd3c7', 'burlywood', '#bebada', '#fb8072', '#80b1d3', '#fdb462', '#b3de69']
    plot_labels = [f'{i} \n({j:.1f}%)' for i, j in zip(accidents_per_day["DayOfWeek"], accidents_per_day["Percentage"])]
    circle_plot = circlify.circlify(accidents_per_day["Percentage"].tolist(), target_enclosure=circlify.Circle(x=0, y=0))

    # Create the plot
    fig, axs = plt.subplots(figsize=(15, 15), facecolor='none')
    # Find axis boundaries
    lim = max(max(abs(circle.x) + circle.r, abs(circle.y) + circle.r) for circle in circle_plot)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    # Display circles
    for circle, colour, label in zip(circle_plot, reversed(colours), reversed(plot_labels)):
        x, y, r = circle
        axs.add_patch(plt.Circle((x, y), r, linewidth=2, facecolor=colour, edgecolor='grey'))
        plt.annotate(label, (x, y), va='center', ha='center', fontweight='bold', fontsize=14)  # Adjust fontsize here
    plt.axis('off')

    # Set the background of the plot to be transparent
    fig.patch.set_alpha(0.0)
    axs.patch.set_alpha(0.0)

    # Add a title to the plot
    st.markdown(
        """
        <text class="gtitle" x="4" y="50" text-anchor="start" dy="0em" data-unformatted="<b><b>Accidents by Day of the Week</b></b>" data-math="N" style="opacity: 1; font-family: &quot;Source Sans Pro&quot;, sans-serif; font-size: 16px; fill: rgb(250, 250, 250); fill-opacity: 1; font-weight: normal; font-style: normal; font-variant: normal; white-space: pre;"><tspan style="font-weight:bold"><tspan style="font-weight:bold">Accidents by Day of the week</tspan></tspan></text>
        """
        , unsafe_allow_html=True
    )

    # Display the plot in Streamlit
    st.pyplot(fig)

    st.markdown("""
    The bubble chart shows that Sunday and Saturday have the most number of accidents, with 17.1% and 18.8% respectively. 
    More than a third of the accidents happen on weekends. This trend could be due to increased air traffic during weekends 
    as more people travel for leisure and vacations.
    """)