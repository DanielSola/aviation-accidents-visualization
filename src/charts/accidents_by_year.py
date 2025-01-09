import pandas as pd
import streamlit as st
import altair as alt
from utils.load_data import load_data
from utils.get_accidents_by_year import get_accidents_by_year

def accidents_by_year(accidents_data): 

    data = get_accidents_by_year(accidents_data)


    chart = alt.Chart(data).mark_area().encode(
            x=alt.X('Year:O', scale=alt.Scale(domain=list(range(1982, 2023))), axis=alt.Axis(labelAngle=-45)),
            y=alt.Y('Count:Q'),
            color=alt.Color('Severity:N', sort=['Non-Fatal', 'Fatal']),
            order=alt.Order('Severity', sort='descending')
        ).properties(
            width=1000,
            height=400,
            title="Accidents by Year (Fatal/Non-Fatal)"
        )
        
    st.altair_chart(chart)

    # Add a text explanation
    st.markdown("""
    The graph shows a decline in the number of aviation accidents from about 3500 yearly in 1982 to about 1500 in 2022. 
    This trend indicates improvements in aviation safety over the years, likely due to advancements in technology, 
    better training, and stricter regulations.
    """)