import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='SCoP', layout='centered')

# Define the custom HTML and CSS to use
html_string = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

        body {
            font-family: 'Montserrat', sans-serif;
            background-color: #414141ff; /* Dark background */
            color: #ffffff; /* White text color */
        }

        .logo {
            font-family: 'Montserrat', sans-serif;
            font-size: 2em;
            text-transform: uppercase;
            color: #ffffff;
        }

        .logo span.large {
            font-size: 1.5em; /* Larger size */
            font-weight: 700;
        }

        .logo span.small {
            font-size: 1em; /* Smaller size */
        }

        .stTextInput input {
            font-family: 'Montserrat', sans-serif;
            background-color: #414141ff;
            color: white;
            border-color: white;
        }

        .stTextInput>div>div>input {
            border-color: white;
        }
        .css-1cpxqw2 {
            border-color: white;
        }
        /* Add other Streamlit components you wish to style */
    </style>

    <div class="logo">
        <span class="large">S</span>
        <span class="large">C</span>
        <span class="small">O</span>
        <span class="large">P</span>
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
            background-color: #414141ff;
            color: white;
        }
        .stTextInput input {
            color: white;
        }
        .stTextInput>div>div>input {
            border-color: white;
        }
        .css-1cpxqw2 {
            border-color: white;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Text input box with placeholder
user_input = st.text_input("", placeholder="Ask SCoP", key="prompt_input")

# Display something once the user enters a prompt
if user_input:
    st.write("You entered: ", user_input)

# The rest of your genAI tool logic will go here






