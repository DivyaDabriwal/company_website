import pandas
import streamlit as st

st.title('Contact Us')

df = pandas.read_csv('topics.csv')

topic_data = [(row['topic']) for index, row in df.iterrows()]

with st.form('form'):
    st.text_input('Your Email Address')
    option = st.selectbox(
        "How would you like to be contacted?",
        topic_data
    )
    st.text_area('Text')
    st.form_submit_button('Submit')