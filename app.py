import pandas as pd
data_url = 'https://linked.aub.edu.lb/pkgcube/data/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv'

# Load the CSV file directly from the URL
df = pd.read_csv(data_url)  # Load the CSV file
print("Loaded data into DataFrame.")
print(df.head(50))
import streamlit as st
import pandas as pd
import numpy as np
st.title("Exploring Tourism and Accommodation Trends in Selected Lebanese Towns")
Tourism_Index_COLUMN = 'Tourism Index'
Number_of_Hotels_COLUMN = 'Total_number_of_hotels'
data_csv='551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv'
def load_data(nrows):
  data = pd.read_csv(data_csv, nrows=nrows)
  #lowercase = lambda x: str(x).lower()
  #data.rename(lowercase, axis='columns', inplace=True)
  #data[Tourism_Index_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
  return data
data_load_state = st.text('Loading data...')
data = load_data(50)
data_load_state.text("Done!")



