import streamlit as st
import plotly.express as px
import plotly.graph_objects as go

def accidents_by_phase(data):
    # Filter out unwanted values
    filtered_data = data[~data['Broad.phase.of.flight'].isin(['Unknown', 'Other'])]

    # Count the occurrences of each phase
    phases = filtered_data['Broad.phase.of.flight'].value_counts().reset_index()
    phases.columns = ['Phase', 'Accidents']

    # Add a column with a short description for each phase
    descriptions = {
        'Landing': 'The aircraft descends to the runway, touches down, and slows to a stop or taxi speed.',
        'Takeoff': 'The aircraft accelerates on the runway, lifts off, and begins its climb to cruising altitude.',
        'Cruise': 'The aircraft flies at a steady altitude and speed, covering most of the journey between takeoff and landing.',
        'Maneuvering': 'The aircraft changes direction, altitude, or speed, usually during turns, climbs, or descents, to follow a specific flight path.',
        'Approach': 'The aircraft descends and lines up with the runway for landing. Pilots reduce speed, lower the landing gear, and prepare for a safe touchdown.',
        'Climb': 'The period during which the aircraft climbs to a predetermined cruising altitude after take-off.',
        'Taxi': 'The pilots navigate the aircraft from the terminal to the runway.',
        'Descent': 'The aircraft decreases altitude in preparation for landing.',
        'Go-around': 'The landing is aborted and the aircraft is taken back into the air to make another approach or divert to an alternative airport.',
        'Standing': 'Phase of flight prior to pushback or taxi, or after arrival, at the gate, ramp, or parking area, while the aircraft is stationary.'
    }

    phases['Description'] = phases['Phase'].map(descriptions)

    # Calculate the total number of accidents
    total_accidents = phases['Accidents'].sum()

    # Create the donut chart using Plotly
    fig = px.pie(phases, values='Accidents', names='Phase', title='Accidents by Phase of Flight', 
                 color_discrete_sequence=px.colors.qualitative.Pastel, hole=0.4, width=700, height=700)

    # Add custom data for tooltips
    fig.update_traces(customdata=phases[['Description']].values)

    # Update the textinfo to show the number of accidents and the percentage
    fig.update_traces(
        textinfo='label+value+percent',
        texttemplate='%{label}<br>%{value} accidents<br>%{percent}',
        hovertemplate='<b>%{customdata[0]}</b>'
    )

    # Add the total number of accidents in the center
    fig.add_annotation(dict(text=f'Total<br>{total_accidents}', x=0.5, y=0.5, font_size=20, showarrow=False))

    # Remove the legend
    fig.update_layout(showlegend=False)

    # Display the donut chart in Streamlit
    st.plotly_chart(fig)

# Example usage
# data = load_data()  # Assuming you have a function to load your data
# accidents_by_phase(data)