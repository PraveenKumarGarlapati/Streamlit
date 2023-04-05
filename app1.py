import pandas as pd
import streamlit as st
import base64
import pyperclip
import tabulate

def main():
    st.title("Display Top 5 Rows of Excel File")
    st.write("")

    # File upload
    uploaded_file = st.file_uploader("Choose an Excel file", type=["xls", "xlsx"])

    if uploaded_file is not None:
        try:
            # Load the first sheet of the Excel file into a Pandas dataframe
            df = pd.read_excel(uploaded_file, sheet_name=0)

            # Display the top 5 rows of the dataframe
            st.write(df.head(5))

            # Download link
            csv = df.head(5).to_csv(index=False)
            b64 = base64.b64encode(csv.encode()).decode()
            st.markdown('### Download Output')
            href = f'<a href="data:file/csv;base64,{b64}" download="output.csv">Download CSV File</a>'
            st.markdown(href, unsafe_allow_html=True)

            # Copy table to clipboard
            st.markdown('### Copy Table')
            if st.button("Copy table to clipboard"):
                pyperclip.copy(df.head(5).to_clipboard(index=False, sep = '\t'))
                st.success("Table copied to clipboard!")
        except Exception as e:
            st.write("Error: {}".format(str(e)))

if __name__ == "__main__":
    main()
