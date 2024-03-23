import streamlit as st
from datetime import datetime

# Streamlit header
st.title("Our Time Saver")
st.image("logo.jpg")

# Streamlit left frame
st.sidebar.title("Sticky Notes")
notes = st.sidebar.text_area("Enter your note")

# Streamlit right frame
st.header("Notes")
columns = st.columns([1, 1, 1, 1])

# Handle notes drag and drop
for column in columns:
    with column:
        st.subheader(column.title())
        st.write("Drag your notes here")

        # Display notes dropped in the column
        if st.session_state.get(column.title(), None):
            for note in st.session_state[column.title()]:
                st.write(f"- {note['text']} (Created on: {note['time']})")
    
    # Drop zone for notes
    if st.session_state.get(column.title(), None) is None:
        st.session_state[column.title()] = []

    if st.sidebar.button(f"Add to {column.title()}"):
        if notes:
            st.session_state[column.title()].append({"text": notes, "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")})
