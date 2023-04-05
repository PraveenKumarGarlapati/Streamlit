import streamlit as st
import pandas as pd
import yaml
from yaml.loader import SafeLoader
import pandas as pd
import numpy as np
from numpy import random
from st_aggrid import GridOptionsBuilder, AgGrid, GridUpdateMode, DataReturnMode
import standby_functions

with open('config.yml') as f:
    yaml_data = yaml.load(f, Loader=SafeLoader)

file_path = yaml_data['paths']['file_path']

df = pd.read_excel(file_path, nrows = 100)

st. set_page_config(layout="wide")
tab1, tab2, tab3, tab4 = st.tabs(['Anomalies','Analyze','Root Cause','Optimization Results'])

# Define the sidebar
st.sidebar.title('Apply Filters')
date_sb = st.sidebar.selectbox(
    'Select a Date',
    df['Date'].unique())

circle_sb = st.sidebar.selectbox('Select Circle',df['Circle'].unique())
city_sb = st.sidebar.selectbox('Select Circle',df['City'].unique())

with tab1:
    # Define the main content area
    st.title('Top Anomalies')
    st.write('This is the main content area of the app.')
    st.write('Here is a sample dataframe:')

    df1 = df[(df['Date'] == date_sb)\
        &(df['Circle'] == circle_sb)]
        
    AgGrid(df1)
    selected_indices = st.multiselect('Select a Component to analyze:', df1['Component'].unique())

with tab2:
    # Define the main content area
    st.title('Analyze the selected rows')
    st.write('Here is a sample dataframe:')

    si_length  = len(selected_indices)
    s1 = pd.DataFrame()
    
    s1['Component'] = selected_indices
    s1['total_sectors'] = random.randint(100, size=(si_length))
    s1['total_cells'] = random.randint(100, size=(si_length))
    s1['total_voice_affected'] = random.randint(5000, size=(si_length))
    s1['% Indoor Session'] = random.randint(100, size=(si_length))
    s1['rsrp'] = random.randint(100, size=(si_length))
    s1['ta_distance'] = random.randint(100, size=(si_length))
    s1['mean_pusch'] = random.randint(100, size=(si_length))
    

    st.dataframe(s1)
    selected_indices2 = st.selectbox('Pick a component to do cell-level analysis', s1['Component'].unique())


    # Define the form and inputs
    with st.form(key='my_form'):
        submit_button = st.form_submit_button(label='Submit')

    # Process the form when the 'Submit' button is clicked
    if submit_button:
        s2 = pd.DataFrame(np.random.randint(0,10, size=(8,1)))

        s2['Component'] = selected_indices2
        for i in ['Sector_ID','Cell_ID','Frequency','mean_rsrp','mean_ta_distance','total_customer','total_voice affected']:
            s2[i] = random.randint(100, size=(8))
        
        s2.drop(columns = 0, inplace=True)
        st.dataframe(s2)

        # Display the charts in 3 columns
        col1, col2, col3 = st.columns(3)
        with col1:
            st.plotly_chart(standby_functions.fig, use_container_width=True)
        with col2:  
            st.plotly_chart(standby_functions.fig, use_container_width=True)
        with col3:
            st.plotly_chart(standby_functions.fig, use_container_width=True)


with tab3:
    st.title('Loading...')



with tab4:
    st.write('No Optimization Results Available for the chosen')


