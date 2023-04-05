import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

# Set page title
st.title("Data Explorer")

# Upload file
uploaded_file = st.file_uploader("Choose a file", type=["xlsx", "csv", "parquet"])

# If file is uploaded
if uploaded_file is not None:
    # Read file
    try:
        df = pd.read_excel(uploaded_file)  # Use pd.read_csv for CSV files or pd.read_parquet for Parquet files
    except:
        st.error("Failed to read file")
    
    # Show first 5 rows of data
    st.write("First 5 rows of data:")
    st.write(df.head())

    # Generate graphs
    st.write("Graphs:")
    
    # Graph 1: Bar chart of column 1
    plt.bar(df.index, df.iloc[:, 0])
    plt.title("Column 1")
    st.pyplot()
    
    # Graph 2: Line chart of column 2
    plt.plot(df.index, df.iloc[:, 1])
    plt.title("Column 2")
    st.pyplot()
