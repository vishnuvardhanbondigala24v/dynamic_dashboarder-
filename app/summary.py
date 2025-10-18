import streamlit as st
import pandas as pd

def show_summary_cards(df):
    st.header("📋 Summary Metrics")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()

    # Total rows
    total_rows = df.shape[0]
    st.metric(label="Total Records", value=f"{total_rows:,}")

    # Total sales (if column exists)
    if "Sales" in df.columns:
        total_sales = df["Sales"].sum()
        st.metric(label="Total Sales", value=f"${total_sales:,.2f}")

    # Average sales
    if "Sales" in df.columns:
        avg_sales = df["Sales"].mean()
        st.metric(label="Average Sale", value=f"${avg_sales:,.2f}")

    # Unique customers
    if "Customer ID" in df.columns:
        unique_customers = df["Customer ID"].nunique()
        st.metric(label="Unique Customers", value=f"{unique_customers:,}")
