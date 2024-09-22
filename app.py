import pandas as pd
uploaded = files.upload()
for filename in uploaded.keys(https://linked.aub.edu.lb/pkgcube/data/551015b5649368dd2612f795c2a9c2d8_20240902_115953.csv):
    df = pd.read_csv(filename)  # Load the CSV file
    print(f"Loaded {filename} into DataFrame.")
