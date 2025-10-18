import pandas as pd
import streamlit as st

def apply_filters(df):
    st.sidebar.header("🔍 Filter Your Data")

    # Detect actual date columns by trying to parse them
    candidate_cols = df.select_dtypes(include=["object"]).columns
    date_cols = []
    for col in candidate_cols:
        try:
            parsed = pd.to_datetime(df[col], errors='coerce')
            if parsed.notna().sum() > 0:  # At least some valid dates
                df[col] = parsed
                date_cols.append(col)
        except Exception:
            continue

    # Date filter
    if date_cols:
        date_col = st.sidebar.selectbox("Select a date column", date_cols)
        min_date = df[date_col].min()
        max_date = df[date_col].max()
        date_range = st.sidebar.date_input("Select date range", [min_date, max_date])
        if len(date_range) == 2:
            df = df[(df[date_col] >= pd.to_datetime(date_range[0])) & (df[date_col] <= pd.to_datetime(date_range[1]))]
    else:
        st.sidebar.warning("No valid date columns found.")

    # Categorical filters
    cat_cols = df.select_dtypes(include=["object", "category"]).columns
    for col in cat_cols:
        unique_vals = df[col].dropna().unique()
        if len(unique_vals) < 50:
            selected = st.sidebar.multiselect(f"Filter by {col}", unique_vals)
            if selected:
                df = df[df[col].isin(selected)]

    return df
