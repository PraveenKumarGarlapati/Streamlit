import streamlit as st
import pandas as pd
import yaml
from yaml.loader import SafeLoader
import pandas as pd
# Open the file and load the file
with open('config.yml') as f:
    yaml_data = yaml.load(f, Loader=SafeLoader)

file_path = yaml_data['paths']['file_path']

df = pd.read_excel(file_path)

df.columns

# 'Circle', 'City', 'Component', 'Date', 'Hour', 'Total Customers',
#        'Anomaly', 'Ratio Data', 'Ratio Voice', 'Ratio HSI', 'cluster_issue',
#        'Data Volume', 'Data Volume Formula', 'Data Volume mean',
#        'Data Volume std', 'Voice Affected Users',
#        'Voice Affected Users Formula', 'Voice Affected Users mean',
#        'Voice Affected Users std', 'HSI Affected Users',
#        'HSI Affected Users Formula', 'HSI Affected Users mean',
#        'HSI Affected Users std', 'Data % Change', 'Voice % Change',
#        'HSI % Change', 'num_grids', 'num_cells', 'num_sectors',
#        'Indoor Freqency % 850', 'Indoor Freqency % 1800',
#        'Indoor Freqency % 2300', 'prb_20', 'prb_70_90', 'prb_90', 'prb_20_per',
#        'prb_70_90_per', 'prb_90_per', 'area', 'Total_User/Area',
#        'Total_Voice/Area', 'Total_Hsi/Area', 'month', 'week',
#        'total_users_data_complaints', 'total_users_vvm_complaints',
#        'total_users_covergae_complaints', 'total_users_other_complaints',
#        'totla_upc_generated'

# Define the sidebar
st.sidebar.title('Filter Data')
option = st.sidebar.selectbox('Select a Filter', ['Filter 1', 'Filter 2', 'Filter 3'])

# # Load the dataset
# url = 'https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv'
# df = pd.read_csv(url)

# Apply the filter based on user selection
if option == 'Filter 1':
    filtered_df = df[df['Age'] > 30]
elif option == 'Filter 2':
    filtered_df = df[df['Sex'] == 'female']
else:
    filtered_df = df[df['Pclass'] == 1]

# Display the filtered dataset
st.dataframe(filtered_df)

# Define the About Me tab
st.sidebar.title('About Me')
st.sidebar.write('This is the about me section.')

# Define the other tabs
tabs = ['Data', 'About Me']
page = st.sidebar.radio('Navigation', tabs)

if page == 'Data':
    st.title('Public Dataset')
    st.write('This is the data tab.')
else:
    st.title('About Me')
    st.write('This is the about me tab.')
