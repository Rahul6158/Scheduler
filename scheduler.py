import streamlit as st
from datetime import datetime

# Header
st.image("logo.jpg", width=100)
st.title("Our Time Saver")

# Left frame
st.sidebar.title("Sticky Notes")
notes = st.sidebar.text_area("Enter your note")
time_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
st.sidebar.text(f"Current Time: {time_date}")
if st.sidebar.button("Add Note"):
    st.sidebar.markdown(f"- {notes} (Created on: {time_date})")

# Right frame
st.header("Sticky Notes Board")
st.write("Drag and drop notes to the columns below:")

# Display the columns with the notes
col1, col2, col3, col4 = st.beta_columns(4)

with col1:
    st.subheader("Very Urgent")
    st.write("Note 1")
    st.write("Note 2")

with col2:
    st.subheader("Urgent")
    st.write("Note 3")

with col3:
    st.subheader("Have Time")
    st.write("Note 4")
    st.write("Note 5")

with col4:
    st.subheader("No Due")
    st.write("Note 6")
