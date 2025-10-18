import streamlit as st
import pandas as pd

def upload_data():
    return st.file_uploader("Upload your dataset", type=["csv", "xlsx", "json"])

def load_data(file):
    if file.name.endswith(".csv"):
        return pd.read_csv(file)
    elif file.name.endswith(".xlsx"):
        return pd.read_excel(file)
    elif file.name.endswith(".json"):
        return pd.read_json(file)
    else:
        st.error("Unsupported file format")
        return None
