# Accidentes por año. Stacked por fatal / non-fatal

import pandas as pd

def get_accidents_by_year(data):
    # Convert 'Event.Date' to datetime
    data['Event.Date'] = pd.to_datetime(data['Event.Date'], errors='coerce')
    
    # Extract year from 'Event.Date'
    data['Year'] = data['Event.Date'].dt.year
    
    # Create a column to classify accidents as 'Fatal' or 'Non-Fatal'
    data['Severity'] = data['Injury.Severity'].apply(lambda x: 'Fatal' if 'Fatal' in str(x) else 'Non-Fatal')
    
    # Group by year and severity, then count the number of accidents
    accidents_by_year = data.groupby(['Year', 'Severity']).size().reset_index(name='Count')

    accidents_by_year = accidents_by_year[(accidents_by_year['Year'] >= 1982) & (accidents_by_year['Year'] <= 2022)]

    return accidents_by_year