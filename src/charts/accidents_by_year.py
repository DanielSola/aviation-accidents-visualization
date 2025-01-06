import pandas as pd
import streamlit as st
import altair as alt
from utils.load_data import load_data
from utils.get_accidents_by_year import get_accidents_by_year

def accidents_by_year(accidents_data): 

    data = get_accidents_by_year(accidents_data)

    st.write("Accidents by Year (Stacked by Fatal/Non-Fatal):")

    chart = alt.Chart(data).mark_area().encode(
            x=alt.X('Year:O', scale=alt.Scale(domain=list(range(1982, 2023)))),
            y=alt.Y('Count:Q'),
            color=alt.Color('Severity:N', sort=['Fatal', 'Non-Fatal']),
            order=alt.Order('Severity', sort='ascending')
        ).properties(
            width=1000,
            height=400
        )
        
    st.altair_chart(chart)