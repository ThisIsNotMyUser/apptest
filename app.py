# app.py
import streamlit as st

# Center the title, instructions, and input box using columns
# Adjust the ratio to make the center column wider
col1, col2, col3 = st.columns([1, 6, 1])

# Use the middle column to place the title, instructions, and text input
with col2:
    st.title('SCoP')
    st.write('Please enter your prompt in the text box below and press Enter.')
    user_input = st.text_input("Enter your prompt here...", key="input")

# Check if there's input and display the output at the top of the page
if user_input:
    # Display the output in a container at the top of the page
    with st.container():
        st.write(f'You entered: {user_input}')
