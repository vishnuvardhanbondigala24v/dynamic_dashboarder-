import streamlit as st
from app import upload, filters, summary, dashboard
from utils import preprocessing

# Page setup
st.set_page_config(page_title="📊 Dynamic Dashboarder", layout="wide")
st.title("📊 Dynamic Dashboarder")
st.markdown("Upload your dataset and explore an auto-generated dashboard with filters, charts, and insights.")

# Upload section
uploaded_file = upload.upload_data()

if uploaded_file:
    df = upload.load_data(uploaded_file)
    if df is not None:
        st.success("✅ File uploaded successfully!")

        # Preprocess data
        df = preprocessing.clean_data(df)
        df = preprocessing.fill_missing(df)

        # Apply filters
        df = filters.apply_filters(df)

        # Show summary cards
        summary.show_summary_cards(df)

        # Show dashboard
        dashboard.show_dashboard(df)
    else:
        st.error("❌ Failed to load the file. Please check the format.")
else:
    st.info("📁 Please upload a CSV, Excel, or JSON file to begin.")
