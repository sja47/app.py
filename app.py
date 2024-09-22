import pandas as pd
from google.colab import files
uploaded = files.upload()
for filename in uploaded.keys():
    df = pd.read_csv(filename)  # Load the CSV file
    print(f"Loaded {filename} into DataFrame.")
