import streamlit as st
import pandas as pd
import pickle
import os
uploaded_file = st.file_uploader("Upload file")
# Save file
if uploaded_file is not None:
    path = "dataset/"
    with open(path + "train_data.csv", "wb") as f:
        f.write(uploaded_file.getbuffer())