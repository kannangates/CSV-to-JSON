import streamlit as st
import json
import csv
import pandas as pd
import os
from setuptools import setup, find_packages


@st.cache
# IMPORTANT: Cache the conversion to prevent computation on every rerun
def convert_df(file):
    return file.to_csv().encode('utf-8')


st.title("Conversion assistance")


def load_data(file):
    df = pd.read_csv(file)
    return df


def download_button(csv):
    st.download_button(
        label="Download revised file as CSV",
        data=csv,
        file_name='df1_new.csv',
        mime='text/csv'
    )


with st.form('my_form1'):
    col1, col2 = st.columns((1, 1))
    with col1:
        is_raido = st.radio("Whats do you want to convert",
                            ("CSV 2 JSON", "JSON 2 CSV"))

    if is_raido == "CSV 2 JSON":
        uploaded_file = st.text_input('Enter CSV file path')
        st.cache(allow_output_mutation=False)
        if uploaded_file is not None:
            submit3 = st.form_submit_button("Submit")

        if submit3:
            st.write("Converted CSV File to JSON")
            data = []
            with open(uploaded_file, encoding='utf-8') as csvFile:
                csvReader = csv.DictReader(csvFile)
                for row in csvReader:
                    data.append(row)
                jsonString = json.dumps(data, indent=4)
                st.json(jsonString)

    if is_raido == "JSON 2 CSV":
        uploaded_file = st.text_input('Enter JSON file path')
        st.cache(allow_output_mutation=False)

        if uploaded_file is not None:
            submit3 = st.form_submit_button("Submit")

        if submit3:
            with open(uploaded_file, 'r') as jf:
                st.write("Converted JSON File to CSV")
                data = json.load(jf)
                df = pd.json_normalize(data)
                st.dataframe(df)
                generate_csv = df.to_csv('filename.csv')
                open('df.csv', 'w').write(df.to_csv())
            # download_button(df)
            # df.to_csv('output_u.csv', index=False)
