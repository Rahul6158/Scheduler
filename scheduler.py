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
very_urgent_notes = st.beta_container()
urgent_notes = st.beta_container()
have_time_notes = st.beta_container()
no_due_notes = st.beta_container()

def show_notes(notes_container):
    for note in notes_container:
        st.write(note)

st.text("")
st.text("Drag your notes here:")
notes_dragged = st.text_area("")

if st.button("Add Note"):
    st.write(notes_dragged)

# Display the columns with the notes
with very_urgent_notes:
    st.subheader("Very Urgent")
    show_notes([])  # Add your very urgent notes here

with urgent_notes:
    st.subheader("Urgent")
    show_notes([])  # Add your urgent notes here

with have_time_notes:
    st.subheader("Have Time")
    show_notes([])  # Add your have time notes here

with no_due_notes:
    st.subheader("No Due")
    show_notes([])  # Add your no due notes here
