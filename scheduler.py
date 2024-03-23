import streamlit as st
import pandas as pd

# Load the "works" dataset
works = pd.read_csv("works.csv")

# Display the dataset
st.write("## Works Dataset")
st.write(works)

# Modify the dataset
st.write("## Modify Dataset")
very_urgent = st.text_input("Very Urgent:")
urgent = st.text_input("Urgent:")
have_time = st.text_input("Have time:")
no_due = st.text_input("No Due:")

if st.button("Add Entry"):
    new_entry = {'Very-Urgent': very_urgent, 'Urgent': urgent, 'Have time': have_time, 'No-Due': no_due}
    works = works.append(new_entry, ignore_index=True)
    st.write("### Updated Dataset")
    st.write(works)

# Save the modified dataset
if st.button("Save Changes"):
    works.to_csv("modified_works_dataset.csv", index=False)
    st.write("Changes saved successfully.")
