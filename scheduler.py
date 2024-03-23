import streamlit as st
import pandas as pd

# Load the "works" dataset
works = pd.read_csv("path_to_works_dataset.csv")

# Display the dataset
st.write("## Works Dataset")
st.write(works)

# Modify the dataset
st.write("## Modify Dataset")
name = st.text_input("Enter name:")
age = st.number_input("Enter age:")
city = st.text_input("Enter city:")
country = st.text_input("Enter country:")

if st.button("Add Entry"):
    new_entry = {'Name': name, 'Age': age, 'City': city, 'Country': country}
    works = works.append(new_entry, ignore_index=True)
    st.write("### Updated Dataset")
    st.write(works)

# Save the modified dataset
if st.button("Save Changes"):
    works.to_csv("modified_works_dataset.csv", index=False)
    st.write("Changes saved successfully.")
