import streamlit as st
import plotly.express as px
import pandas as pd

def show_dashboard(df):
    st.header("📊 Interactive Dashboard")

    numeric_cols = df.select_dtypes(include=['int64', 'float64']).columns.tolist()
    cat_cols = df.select_dtypes(include=['object', 'category']).columns.tolist()

    # 📦 Bar Chart
    st.subheader("📦 Bar Chart")
    bar_x = st.selectbox("Select categorical column (X-axis)", cat_cols)
    bar_y = st.selectbox("Select numeric column (Y-axis)", numeric_cols)
    if bar_x and bar_y:
        bar_data = df.groupby(bar_x)[bar_y].sum().reset_index()
        fig = px.bar(bar_data, x=bar_x, y=bar_y, color=bar_x, title=f"{bar_y} by {bar_x}")
        st.plotly_chart(fig, use_container_width=True)

    # 📈 Line Chart
    st.subheader("📈 Line Chart")
    line_x = st.selectbox("Select X-axis column", numeric_cols, key="line_x")
    line_y = st.selectbox("Select Y-axis column", numeric_cols, key="line_y")
    if line_x and line_y:
        fig = px.line(df, x=line_x, y=line_y, title=f"{line_y} over {line_x}")
        st.plotly_chart(fig, use_container_width=True)

    # 🥧 Pie Chart
    st.subheader("🥧 Pie Chart")
    pie_col = st.selectbox("Select categorical column for pie chart", cat_cols, key="pie")
    if pie_col:
        pie_data = df[pie_col].value_counts().reset_index()
        pie_data.columns = [pie_col, "Count"]
        fig = px.pie(pie_data, names=pie_col, values="Count", title=f"Distribution of {pie_col}")
        st.plotly_chart(fig, use_container_width=True)

    # 📆 Time Series Chart
    st.subheader("📆 Time Series Chart")
    if "Order Date" in df.columns and "Sales" in df.columns:
        df["Order Date"] = pd.to_datetime(df["Order Date"], errors="coerce")
        time_data = df.groupby(df["Order Date"].dt.to_period("M"))["Sales"].sum().reset_index()
        time_data["Order Date"] = time_data["Order Date"].dt.to_timestamp()
        fig = px.line(time_data, x="Order Date", y="Sales", title="Monthly Sales Trend")
        st.plotly_chart(fig, use_container_width=True)

    # 📚 Histogram
    st.subheader("📚 Histogram")
    hist_col = st.selectbox("Select column for histogram", numeric_cols, key="hist")
    bins = st.slider("Number of bins", min_value=5, max_value=100, value=30)
    fig = px.histogram(df, x=hist_col, nbins=bins, title=f"Distribution of {hist_col}")
    st.plotly_chart(fig, use_container_width=True)

    # 🔘 Scatter Plot
    st.subheader("🔘 Scatter Plot")
    scatter_x = st.selectbox("X-axis", numeric_cols, key="scatter_x")
    scatter_y = st.selectbox("Y-axis", numeric_cols, key="scatter_y")
    fig = px.scatter(df, x=scatter_x, y=scatter_y, title=f"{scatter_y} vs {scatter_x}")
    st.plotly_chart(fig, use_container_width=True)
