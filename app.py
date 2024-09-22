import streamlit as st
import pandas as pd
import plotly.express as px

# Title of the app
st.title("Exploring Tourism and Accommodation Trends in Selected Lebanese Towns")

# Define your column names
Tourism_Index_COLUMN = 'Tourism Index'
Number_of_Hotels_COLUMN = 'Total_number_of_hotels'

# URL of the CSV file hosted on GitHub (Replace with your actual GitHub URL)
data_url = 'https://raw.githubusercontent.com/your-username/your-repo/main/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv'

# Function to load data from the GitHub URL
@st.cache_data  
def load_data(nrows):
    data = pd.read_csv(data_url, nrows=nrows)
    return data

# Loading data
data_load_state = st.text('Loading data...')
data = load_data(50)  # Load first 50 rows
data_load_state.text("Done! (using st.cache_data)")

# Option to show raw data
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data)

# Markdown descriptions
st.markdown("In this interactive dashboard, we explore two important aspects of tourism in Lebanon.")
st.markdown("**Tourism Index**: Measures a town's attractiveness to tourists...")
st.markdown("**Number of Hotels**: Reflects accommodation capacity...")

# Bar chart: Number of hotels by town
st.subheader('Number of hotels By Town')
Hotels_to_filter = st.slider('Number of Hotels', 0, 4, 0)
filtered_data = data[data[Number_of_Hotels_COLUMN] == Hotels_to_filter]

chart_data = pd.DataFrame({
    "Town": data['Town'],
    "Hotels": data[Number_of_Hotels_COLUMN][data[Number_of_Hotels_COLUMN] == Hotels_to_filter]
})
st.bar_chart(chart_data, x='Town', y='Hotels')

# Pie chart: Towns by selected index
pie_data = pd.DataFrame({
    "Town": data['Town'],
    "Tourism_Index": data[Tourism_Index_COLUMN],
    "Hotels_Index": data[Number_of_Hotels_COLUMN][data[Number_of_Hotels_COLUMN] == Hotels_to_filter]
})

Index = st.selectbox('Index', ['Tourism_Index', 'Hotels_Index'])
fig = px.pie(pie_data, values=Index, names='Town', height=300, width=200, title=f"{Index}")
st.plotly_chart(fig, use_container_width=True)
