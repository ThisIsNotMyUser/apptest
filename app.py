# app.py
import streamlit as st

# Use columns to center the content
# Create three columns with the middle one being the main one
col1, col2, col3 = st.columns([1, 2, 1])

# Use the middle column to display the title, instruction, and input box
with col2:
    st.title('SCoP')

    # Instruction for the user on how to use the tool
    st.write('Please enter your prompt in the text box below and press Enter.')

    # Text box for user input
    user_input = st.text_input("Enter your prompt here...", key="input")

# Check if there's input and display the output above everything else
if user_input:
    # Display the output in a container at the top of the page
    with st.container():
        st.write(f'You entered: {user_input}')

    # Clear the input box after displaying the output
    st.session_state.input = ""



