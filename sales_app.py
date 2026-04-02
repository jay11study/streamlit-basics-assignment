import streamlit as st
import pandas as pd

# Title and subheader
st.title("Sales Summary App")
st.subheader("Simple interactive sales summary with category filter")

# Hardcoded DataFrame
data = {
    "Product": ["Laptop", "Mouse", "Keyboard", "Monitor", "Printer", "Tablet"],
    "Category": ["Electronics", "Electronics", "Electronics", "Electronics", "Office", "Electronics"],
    "Sales": [50000, 15000, 20000, 30000, 25000, 40000]
}

df = pd.DataFrame(data)

# Sidebar filter
st.sidebar.header("Filter Options")
category = st.sidebar.selectbox("Select Category", df["Category"].unique())

# Filter DataFrame
filtered_df = df[df["Category"] == category]

# Display filtered data
st.dataframe(filtered_df)

# Line chart
st.line_chart(filtered_df["Sales"])
