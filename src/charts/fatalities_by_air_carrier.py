import streamlit as st
import plotly.express as px
import pandas as pd

def fatalities_by_air_carrier(data):
    # Drop missing values for the Air.carrier and Total.Fatal.Injuries columns
    data = data.dropna(subset=["Air.carrier", "Total.Fatal.Injuries"])

    # Group by Air.carrier and sum the Total.Fatal.Injuries
    air_carrier_fatalities = data.groupby("Air.carrier")["Total.Fatal.Injuries"].sum().reset_index()

    # Filter out air carriers with fewer than 100 fatalities
    air_carrier_fatalities = air_carrier_fatalities[air_carrier_fatalities["Total.Fatal.Injuries"] >= 100]

    # Sort air carriers by the number of fatalities in descending order
    air_carrier_fatalities = air_carrier_fatalities.sort_values(by="Total.Fatal.Injuries", ascending=False)

    # Create the treemap
    fig = px.treemap(air_carrier_fatalities, path=['Air.carrier'], values='Total.Fatal.Injuries', 
                     title='Fatalities by Air Carrier', color='Total.Fatal.Injuries', color_continuous_scale='Reds',
                     width=2000, height=600, range_color=[0, 500])
    
    fig.update_layout(margin=dict(t=50, l=25, r=25, b=25))
    fig.update_traces(textinfo='label+value')

    # Display the treemap in Streamlit
    st.plotly_chart(fig, use_container_width=True)

    st.subheader('Select Air Carrier')

    # Add a selector for Air carrier, sorted by most fatalities
    air_carriers = air_carrier_fatalities["Air.carrier"].unique()
    selected_carrier = st.selectbox("", air_carriers)

    # Filter data for the selected air carrier
    carrier_data = data[(data["Air.carrier"] == selected_carrier) & (data["Total.Fatal.Injuries"] > 0)]

    # Get the top 5 accidents with the most fatalities for the selected air carrier
    top_accidents = carrier_data.nlargest(5, 'Total.Fatal.Injuries')[["Accident.Number", "Event.Date", "Location", "Country", "Aircraft.damage", "Make", "Model", "Total.Fatal.Injuries", "Total.Serious.Injuries", "Total.Minor.Injuries", "Total.Uninjured"]]

    # Convert Event.Date to DD/MM/YYYY format
    top_accidents["Event.Date"] = pd.to_datetime(top_accidents["Event.Date"]).dt.strftime('%d/%m/%Y')

    # Fill NA values with 0 and round injury columns to integers
    top_accidents["Total.Fatal.Injuries"] = top_accidents["Total.Fatal.Injuries"].fillna(0).astype(int)
    top_accidents["Total.Serious.Injuries"] = top_accidents["Total.Serious.Injuries"].fillna(0).astype(int)
    top_accidents["Total.Minor.Injuries"] = top_accidents["Total.Minor.Injuries"].fillna(0).astype(int)
    top_accidents["Total.Uninjured"] = top_accidents["Total.Uninjured"].fillna(0).astype(int)

    # Rename columns to be more reader-friendly and concise
    top_accidents.columns = ["Accident No.", "Date", "Location", "Country", "Damage", "Make", "Model", "Fatal Injuries", "Serious Injuries", "Minor Injuries", "Uninjured"]

    # Reset the index and make it start at 1
    top_accidents = top_accidents.reset_index(drop=True)
    top_accidents.index = top_accidents.index + 1

    # Display the table with full page width
    st.write(f"Top Accidents with Most Fatalities for {selected_carrier}:")
    st.table(top_accidents)


    st.markdown("""
    These charts allow visualizing the total number of fatalities associated with various air carriers and accidents. The data highlights the air carriers with the highest number of fatalities, providing insights into the safety records of these airlines.
    """)