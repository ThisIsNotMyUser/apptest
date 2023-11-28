import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='GenAI Tool', layout='centered')

# URL of the background image (replace with the actual URL of your image in GitHub)
bg_image_url = "https://github.com/M-m-mBootz/apptest/blob/main/bg.png"

# Define the custom HTML and CSS to use
html_string = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

        body {
            font-family: 'Montserrat', sans-serif;
            background-image: url('""" + bg_image_url + """'); /* URL is added here */
            background-size: cover;
            color: white; /* White text color */
        }

        /* ... rest of your CSS ... */

        /* Unfortunately, Streamlit does not support changing the placeholder color via CSS */
    </style>

    <div class="logo">
        <span>G</span><span>e</span><span>n</span><span>A</span><span>I</span>
        <span>T</span><span>o</span><span>o</span><span>l</span>
    </div>
"""

# Use the HTML string with markdown to create the logo with the hover effect
st.markdown(html_string, unsafe_allow_html=True)

# Text input box at the bottom with placeholder
user_input = st.text_input("", placeholder="Ask SCoP", key="prompt_input")

# Display something once the user enters a prompt
if user_input:
    st.write("You entered: ", user_input)

# The rest of your genAI tool logic will go here




