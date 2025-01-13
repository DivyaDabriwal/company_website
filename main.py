import streamlit as st
import csv

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

csv_dict_list = []
with open('data.csv') as file:
    csv_data = csv.DictReader(file, delimiter=',')
    for i in csv_data:
        csv_dict_list.append(i)

with col1:
    for row in csv_dict_list[:4]:
        full_name = f"{row['first name']} {row['last name']}".title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])

with col2:
    for row in csv_dict_list[4:8]:
        full_name = f"{row['first name']} {row['last name']}".title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])

with col3:
    for row in csv_dict_list[8:]:
        full_name = f"{row['first name']} {row['last name']}".title()
        st.subheader(full_name)
        st.write(row['role'])
        st.image('images/' + row['image'])