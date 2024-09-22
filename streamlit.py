import pandas as pd
from google.colab import files
uploaded = files.upload()
for filename in uploaded.keys():
    df = pd.read_csv(filename)  # Load the CSV file
    print(f"Loaded {filename} into DataFrame.")
  print(df.head(50))
pip install streamlit
import streamlit as st
import pandas as pd
import numpy as np
%%writefile app.py
! wget -q -o - ipv4.icanhazip.com
!apt-get install nodejs
!npm install -g localtunnel@2.0.2
! streamlit run app.py & npx localtunnel --port 8501
