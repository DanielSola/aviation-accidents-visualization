# Accidentes por año. Stacked por fatal / non-fatal

import pandas as pd
import streamlit as st
import re

def get_accidents_by_year(data):
    # Convert 'Event.Date' to datetime
    data['Event.Date'] = pd.to_datetime(data['Event.Date'], errors='coerce')
    
    # Extract year from 'Event.Date'
    data['Year'] = data['Event.Date'].dt.year
    
    # Create a column to classify accidents as 'Fatal' or 'Non-Fatal'
    fatal_pattern = re.compile(r'Fatal\(\d+\)')

    data['Severity'] = data['Injury.Severity'].apply(lambda x: 'Fatal' if fatal_pattern.search(str(x)) or x == 'Fatal' else 'Non-Fatal')
    
    # Group by year and severity, then count the number of accidents
    accidents_by_year = data.groupby(['Year', 'Severity']).size().reset_index(name='Count')

    severity_counts = data['Injury.Severity'].value_counts().reset_index()
    severity_counts.columns = ['Injury Severity', 'Count']

    accidents_by_year = accidents_by_year[(accidents_by_year['Year'] >= 1982) & (accidents_by_year['Year'] <= 2022)]

    return accidents_by_year