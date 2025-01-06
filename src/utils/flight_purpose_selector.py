import streamlit as st
import plotly.express as px
import numpy as np
import os
import plotly.graph_objects as go

def get_image_path(make, model):
    # Construct the file path for the given make and model
    file_name = f"{make.lower()}_{model.lower()}.jpg".replace(" ", "_")
    file_path = os.path.join("./data/images", file_name)

    return file_path

def flight_purpose_selector(data):

    # Add a selector for flight purposes
    flight_purposes = [
        "Personal", "Commercial", "Instructional", "Business", "Other", "Crop Dusting", "Positioning",
        "Public Aircraft", "Flight Test", "Air Race/show", "Skydiving", "Banner Tow", "Helicopter Training",
        "Glider Tow", "Firefighting"
    ]

    selected_purpose = st.selectbox("Select Flight Purpose", flight_purposes)

    data = data[(data['Year'] >= 1982) & (data['Year'] <= 2023) & (data['Investigation.Type'] == "Accident")]

    # Filter data based on selected purpose
    filtered_data = data[data["Purpose.of.flight"] == selected_purpose]

    # Create a line chart of accidents by year for the selected purpose of flight
    accidents_by_year = filtered_data.groupby('Year').size().reset_index(name='Accidents')
    fig = px.line(accidents_by_year, x='Year', y='Accidents', title=f'Accidents by Year for {selected_purpose}', labels={'Year': 'Year', 'Accidents': 'Number of Accidents'})
    st.plotly_chart(fig)

    # Find the three most crashed airplanes by purpose
    most_crashed_airplanes = filtered_data.groupby(['Make', 'Model']).size().reset_index(name='Counts').sort_values(by='Counts', ascending=False).head(3)

    # Display the three most crashed airplanes with images side by side
    st.write(f"Three most crashed airplanes for {selected_purpose}:")
    cols = st.columns(3)

    for col, (_, row) in zip(cols, most_crashed_airplanes.iterrows()):
        image_path = get_image_path(row['Make'], row['Model'])

        if os.path.exists(image_path):
            col.image(image_path, caption=f"{row['Make']} {row['Model']} - {row['Counts']} accidents", width=150)
        else:
            col.write(f"Image not available for {row['Make']} {row['Model']}")


    summary = filtered_data.groupby("Purpose.of.flight").agg({
        "Total.Fatal.Injuries": "sum",
        "Total.Serious.Injuries": "sum",
        "Total.Minor.Injuries": "sum",
        "Total.Uninjured": "sum"
    }).reset_index()

    summary.columns = ["Purpose", "Fatalities", "Serious Injuries", "Minor Injuries", "Uninjured"]

    summary = filtered_data.groupby("Purpose.of.flight").agg({
        "Total.Fatal.Injuries": "sum",
        "Total.Serious.Injuries": "sum",
        "Total.Minor.Injuries": "sum",
        "Total.Uninjured": "sum"
    }).reset_index()

    summary.columns = ["Purpose", "Fatalities", "Serious Injuries", "Minor Injuries", "Uninjured"]
    summary["Total"] = summary["Fatalities"] + summary["Serious Injuries"] + summary["Minor Injuries"] + summary["Uninjured"]
    summary["Fatalities %"] = (summary["Fatalities"] / summary["Total"] * 100).round(0)
    summary["Serious Injuries %"] = (summary["Serious Injuries"] / summary["Total"] * 100).round(0)
    summary["Minor Injuries %"] = (summary["Minor Injuries"] / summary["Total"] * 100).round(0)
    summary["Uninjured %"] = (summary["Uninjured"] / summary["Total"] * 100).round(0)

    # Create a horizontal stacked bar chart for the summary with percentages
    fig = go.Figure()
    fig.add_trace(go.Bar(y=summary["Purpose"], x=summary["Fatalities %"], name="Fatalities", orientation='h', marker_color='red'))
    fig.add_trace(go.Bar(y=summary["Purpose"], x=summary["Serious Injuries %"], name="Serious Injuries", orientation='h', marker_color='orange'))
    fig.add_trace(go.Bar(y=summary["Purpose"], x=summary["Minor Injuries %"], name="Minor Injuries", orientation='h', marker_color='yellow'))
    fig.add_trace(go.Bar(y=summary["Purpose"], x=summary["Uninjured %"], name="Uninjured", orientation='h', marker_color='green'))

    fig.update_layout(
        barmode='stack',
        title="Summary of Fatalities, Injuries, and Uninjured by Flight Purpose (Percentage)",
        legend_title="Injury Type",
        xaxis=dict(showticklabels=False, ticksuffix='%')  # Remove x-axis labels
    )

    # Display the bar chart in Streamlit
    st.plotly_chart(fig)