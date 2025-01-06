import streamlit as st
import matplotlib.pyplot as plt
import squarify

def accidents_by_phase(data):
    # Filter out unwanted values
    filtered_data = data[~data['Broad.phase.of.flight'].isin(['Unknown', 'Other'])]

    # Count the occurrences of each phase
    phases = filtered_data['Broad.phase.of.flight'].value_counts().reset_index()
    phases.columns = ['Phase', 'Accidents']

    # Prepare data for the treemap
    volume = phases['Accidents'].tolist()
    labels = [f'{phase}\nAccidents: {count}' for phase, count in zip(phases['Phase'], phases['Accidents'])]
    color_list = plt.cm.tab20.colors  # Use a colormap for colors

    # Set font and background color
    plt.rcParams['font.family'] = 'sans-serif'
    plt.rcParams['font.weight'] = 'bold'  # Set the font weight to bold
    plt.rcParams['font.size'] = 16  # Set the font weight to bold

    plt.rcParams['axes.facecolor'] = (15/255, 17/255, 22/255)  # Set the background color to RGB (15, 17, 22)
    plt.rcParams['savefig.facecolor'] = (15/255, 17/255, 22/255)  # Set the background color to RGB (15, 17, 22) for saved figures

    st.write('Accidents by phase of flight')

    # Create the treemap
    plt.figure(figsize=(22, 10))
    squarify.plot(sizes=volume, label=labels, color=color_list, alpha=1)
    plt.axis('off')

    # Display the treemap in Streamlit
    st.pyplot(plt)