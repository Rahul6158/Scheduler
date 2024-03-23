import streamlit as st
import pandas as pd

# Sample dataset
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 35, 40],
    'City': ['New York', 'Los Angeles', 'Chicago', 'Houston'],
    'Country': ['USA', 'USA', 'USA', 'USA']
}
df = pd.DataFrame(data)

# Display the dataset
st.write("## Original Dataset")
st.write(df)

# Modify the dataset
st.write("## Modify Dataset")
name = st.text_input("Enter name:")
age = st.number_input("Enter age:")
city = st.text_input("Enter city:")
country = st.text_input("Enter country:")

if st.button("Add Entry"):
    new_entry = {'Name': name, 'Age': age, 'City': city, 'Country': country}
    df = df.append(new_entry, ignore_index=True)
    st.write("### Updated Dataset")
    st.write(df)

# Save the modified dataset
if st.button("Save Changes"):
    df.to_csv("modified_dataset.csv", index=False)
    st.write("Changes saved successfully.")
