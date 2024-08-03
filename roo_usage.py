import streamlit as st
from dejan import roo

# Streamlit app title
st.title("Roo Data Demo")

# Sidebar for search engine selection
st.sidebar.header("Search Engine Selection")
search_engine = st.sidebar.selectbox(
    "Select a Search Engine:",
    options={
        1: "Google.com (Desktop)",
        2: "Google.com.au (Desktop)",
        3: "Google.com (Mobile)",
        4: "Google.com.au (Mobile)"
    }
)

# Fetch data as a pandas DataFrame
st.header("Data as Pandas DataFrame")
try:
    data_df = roo.get_roo(search_engine, as_dataframe=True)
    st.dataframe(data_df)  # Display the DataFrame
except Exception as e:
    st.error(f"An error occurred while fetching the DataFrame: {e}")

# Fetch raw JSON data
st.header("Raw JSON Data")
try:
    data_json = roo.get_roo(search_engine, as_dataframe=False)
    st.json(data_json)  # Display the raw JSON data
except Exception as e:
    st.error(f"An error occurred while fetching the raw JSON data: {e}")

