import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import circlify

def accidents_by_phase_bubbles(data):
    # Drop rows with missing Broad.phase.of.flight
    data = data.dropna(subset=["Broad.phase.of.flight"])

    # Count the number of accidents per phase of flight
    accidents_per_phase = data["Broad.phase.of.flight"].value_counts().reset_index()
    accidents_per_phase.columns = ["PhaseOfFlight", "Accidents"]

    # Calculate the percentage of accidents for each phase
    total_accidents = accidents_per_phase["Accidents"].sum()
    accidents_per_phase["Percentage"] = (accidents_per_phase["Accidents"] / total_accidents) * 100

    # Prepare data for circlify
    colours = ['#ff9999','#66b3ff','#99ff99','#ffcc99','#c2c2f0','#ffb3e6','#c4e17f']
    plot_labels = [f'{i} \n({j:.1f}%)' for i, j in zip(accidents_per_phase["PhaseOfFlight"], accidents_per_phase["Percentage"])]
    circle_plot = circlify.circlify(accidents_per_phase["Percentage"].tolist(), target_enclosure=circlify.Circle(x=0, y=0))

    # Note that circle_plot starts from the smallest to the largest, so we have to reverse the list
    circle_plot.reverse()

    # Create the plot
    fig, axs = plt.subplots(figsize=(15, 15), facecolor='none')
    # Find axis boundaries
    lim = max(max(abs(circle.x) + circle.r, abs(circle.y) + circle.r) for circle in circle_plot)
    plt.xlim(-lim, lim)
    plt.ylim(-lim, lim)
    # Display circles
    for circle, colour, label in zip(circle_plot, colours, plot_labels):
        x, y, r = circle
        axs.add_patch(plt.Circle((x, y), r, linewidth=1, facecolor=colour, edgecolor='grey'))
        plt.annotate(label, (x, y), va='center', ha='center', fontweight='bold', fontsize=14)  # Adjust fontsize here
    plt.axis('off')

    # Set the background of the plot to be transparent
    fig.patch.set_alpha(0.0)
    axs.patch.set_alpha(0.0)

    # Display the plot in Streamlit
    st.pyplot(fig)

# Example usage
# data = load_data()  # Assuming you have a function to load your data
# accidents_by_phase_bubbles(data)