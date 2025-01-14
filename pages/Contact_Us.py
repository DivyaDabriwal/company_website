import pandas
import streamlit as st
from send_email import send_email

st.title('Contact Us')

df = pandas.read_csv('topics.csv')

with st.form('form'):
    email_address = st.text_input('Your Email Address', key='email_address')
    contact_reason = st.selectbox(
        "What topic do you want to discuss?",
        df['topic'], key='contact_reason'
    )
    text = st.text_area('Text', key='text')
    submit_button = st.form_submit_button('Submit')

if submit_button:
    with (st.spinner('In Progress.....')):
        message = f"""Subject: Mail from Company Website\n

Contact Reason: {contact_reason}
Message: {text}\n
From: {email_address}
"""
        result = send_email(message)
        if result:
            st.success('Email sent successfully.', icon="📨")
            st.balloons()
        else:
            st.error("An error occurred", icon="😵‍💫")