import streamlit as st
import altair as alt

def normalize_air_carrier(name):
    mapping = {
        'PRIVATE INDIVIDUAL': 'PRIVATE',
        'PILOT': 'PILOT',
        'PRIVATE': 'PRIVATE',
    }

    clean_name = str(name).strip().upper()

    if 'DELTA' in clean_name: return 'Delta Airlines'
    if 'AMERICAN AIRLINES' in clean_name: return 'American Airlines'
    if 'UNITED AIRLINES' in clean_name or 'UNITED AIR LINES' in clean_name: return 'United Airlines'
    if 'CONTINENTAL' in clean_name: return 'Continental Airlines'
    if 'US AIRWAYS' in clean_name or 'USAIR' in clean_name: return 'US Airways'
    if 'SKYWEST' in clean_name: return 'Skywest Airlines'
    if 'AIR METHODS' in clean_name: return 'Air Methods'
    if 'SOUTHWEST' in clean_name: return 'Southwest Airlines'
    if 'CIVIL' in clean_name: return 'Civil Air Patrol'
    if 'EAGLE' in clean_name: return 'American Eagle'
    if 'NORTHWEST' in clean_name: return 'Northwest Airlines'
    if 'EMS' in clean_name: return 'Air Evac Emergency Services'
    if 'HILLSBORO' in clean_name: return 'Hillsboro Aviation'
    if 'UNITED EXPRESS' in clean_name: return 'United Express'
    if 'ERA' in clean_name: return 'Era Aviation'
    if 'AMERICA WEST' in clean_name: return 'America West'
    if 'BRITISH' in clean_name: return 'British Airways'

    return mapping.get(clean_name, name)

def accidents_by_carrier(data):
    # Fill NaN values with an empty string
    data['Air.carrier'] = data['Air.carrier'].fillna('')
    
    # Normalize 'Air.carrier' names
    data['Air.carrier'] = data['Air.carrier'].apply(normalize_air_carrier)
    
    # Filter out unwanted values
    filtered_data = data[~data['Air.carrier'].isin(['ON FILE', 'On File', 'PILOT', 'UNKNOWN', 'Unknown', 'PRIVATE', 'Not Provided by Authority'])]
    
    # Group by normalized 'Air.carrier' and count the number of accidents
    company_accidents = filtered_data['Air.carrier'].value_counts().reset_index()
    company_accidents.columns = ['Carrier', 'Accidents']
    
    # Select top 20 companies
    top_20_companies = company_accidents.iloc[1:21]
    
    # Display the table
    row_chart = alt.Chart(top_20_companies).mark_bar().encode(
        x=alt.X('Accidents:Q', title='Total Accidents'),
        y=alt.Y('Carrier:N', sort='-x', title='Air Carrier', axis=alt.Axis(labelLimit=200)),
        color=alt.Color('Carrier:N', legend=None),
        tooltip=['Carrier', 'Accidents']
    ).properties(
        width=800,
        height=800,  # Increase height to show all 20 rows
        title='Top 20 Companies by Total Number of Accidents'
    )

    st.altair_chart(row_chart)