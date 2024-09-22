import pandas as pd
data_url = 'https://linked.aub.edu.lb/pkgcube/data/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv'

# Load the CSV file directly from the URL
df = pd.read_csv(data_url)  # Load the CSV file
print("Loaded data into DataFrame.")
print(df.head(50))
pip install streamlit
