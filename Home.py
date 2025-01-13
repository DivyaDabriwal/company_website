import streamlit as st
import pandas

st.set_page_config(layout='wide')

st.title('The Best Company')
st.write("""Lorem ipsum dolor sit amet, consectetur adipiscing elit. 
Mauris varius metus dapibus felis viverra efficitur. Proin sollicitudin 
est non leo scelerisque, interdum pharetra odio cursus. Duis id massa sem. 
Cras a est eu ante bibendum ultrices. Proin laoreet dui augue, id bibendum
 nunc faucibus quis. Nullam neque mauris, placerat at ante vel, gravida
  consectetur nulla. Suspendisse lacus purus, tristique at odio tempus, 
  vestibulum mollis erat. Ut in consectetur erat. Nam tincidunt lobortis 
  suscipit. Ut quis rutrum lorem. Morbi ante nisi, mattis eget pretium ut, 
  luctus tincidunt massa. Aenean fringilla mauris ante, at tempor erat 
  sagittis nec. Aenean porttitor accumsan convallis. Curabitur ac gravida dui.
   Nulla facilisi.""")

st.header('Our Team')

col1, col2, col3 = st.columns(3)

df = pandas.read_csv('data.csv')

with col1:
    for index, row in df[:4].iterrows():
        full_name = f"{row['first name']} {row['last name']}".title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for index, row in df[4:8].iterrows():
        full_name = f"{row['first name']} {row['last name']}".title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for index, row in df[8:].iterrows():
        full_name = f"{row['first name']} {row['last name']}".title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])