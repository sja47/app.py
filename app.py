import pandas as pd
import streamlit as st
import plotly.express as px
import numpy as np

# Load the CSV file directly from the URL
data_url = 'https://linked.aub.edu.lb/pkgcube/data/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv'
data = pd.read_csv(data_url)  # Load the CSV file

st.title("Exploring Tourism and Accommodation Trends in Selected Lebanese Towns")

# Define column names
Tourism_Index_COLUMN = 'Tourism Index'
Number_of_Hotels_COLUMN = 'Total_number_of_hotels'

# Show raw data option
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

st.markdown("In this interactive dashboard, we explore two important aspects of tourism in Lebanon.")

st.subheader('Number of hotels By Town')
Hotels_to_filter = st.slider('Number of Hotels', 0, 4, 0)

# Filtered Data
filtered_data = data[data[Number_of_Hotels_COLUMN] == Hotels_to_filter]

# Create chart_data DataFrame
chart_data = pd.DataFrame({
    "Town": data['Town'],
    "Hotels": data[Number_of_Hotels_COLUMN]
})
chart_data = chart_data[chart_data["Hotels"] == Hotels_to_filter]

# Bar chart
st.bar_chart(chart_data.set_index('Town'))

# Creating pie chart data
pie_data = pd.DataFrame({
    "Town": data['Town'],
    "Tourism_Index": data[Tourism_Index_COLUMN],
    "Hotels_Index": data[Number_of_Hotels_COLUMN]
})

# Select index for pie chart
Index = st.selectbox('Index', ['Tourism_Index', 'Hotels_Index'])

# Create pie chart
fig = px.pie(pie_data, values=Index, names='Town', height=300, width=400, title=f"{Index}")
st.plotly_chart(fig, use_container_width=True)






