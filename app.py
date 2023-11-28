import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='SCoP', layout='centered')

# URL of the background image (replace with the actual URL of your image in GitHub)
bg_image_url = "https://github.com/M-m-mBootz/apptest/blob/main/bg.png"

# Define the custom HTML and CSS to use
html_string = f"""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

        body {
            font-family: 'Montserrat', sans-serif;
            background-image: url({bg_image_url});
            background-size: cover;
            color: white; /* White text color */
        }

        /* ... rest of your CSS ... */

        /* Custom CSS to change the placeholder color */
        ::placeholder { /* Chrome, Firefox, Opera, Safari 10.1+ */
            color: white;
            opacity: 1; /* Firefox */
        }

        :-ms-input-placeholder { /* Internet Explorer 10-11 */
            color: white;
        }

        ::-ms-input-placeholder { /* Microsoft Edge */
            color: white;
        }
    </style>

    <div class="logo">
        <span>S</span><span>C</span><span>o</span><span>P</span><span>I</span>
        <span>L</span><span>O</span><span>T</span>
    </div>
"""

# Use the HTML string with markdown to create the logo with the hover effect
st.markdown(html_string, unsafe_allow_html=True)

# Inject the Montserrat font into the Streamlit app
st.markdown(
    """
    <style>
        html, body, [class*="st-"], .stTextInput, .st-bb, .st-da, .st-ea, .css-10trblm {
            font-family: 'Montserrat', sans-serif;
            color: white;
        }
        .stTextInput input, .stTextInput input::placeholder {
            color: white;
        }
        .stTextInput>div>div>input {
            border-color: white;
        }
        .css-1cpxqw2 {
            border-color: white;
        }
        /* Add other Streamlit components you wish to style */
    </style>
    """,
    unsafe_allow_html=True
)

# Text input box at the bottom with placeholder
user_input = st.text_input("", placeholder="Ask SCoP", key="prompt_input")

# Display something once the user enters a prompt
if user_input:
    st.write("You entered: ", user_input)

# The rest of your genAI tool logic will go here



