import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='SCoP', layout='centered')

# Define the custom HTML and CSS to use
html_string = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
        
        /* Add padding to the bottom of the page to lift the content up */
        .reportview-container .main .block-container {
            padding-bottom: 5rem;
        }

        /* Style the logo and input box container */
        .bottom-container {
            position: fixed;
            bottom: 0;
            left: 0;
            width: 100%;
            padding: 1rem;
            background-color: #414141ff;
        }

        .logo {
            font-family: 'Montserrat', sans-serif;
            font-size: 4em; /* 2 times larger */
            text-transform: uppercase;
            color: white;
            display: flex;
            justify-content: center;
        }

        .stTextInput input {
            font-family: 'Montserrat', sans-serif;
            background-color: #414141ff;
            color: white;
            border-color: white;
        }

        /* Style focused input box */
        .stTextInput input:focus {
            border-color: white;
            box-shadow: none;
        }

        /* Style the placeholder */
        .stTextInput input::placeholder {
            color: white;
            opacity: 0.5;
        }
        
        /* Adjust the style of the input container */
        .stTextInput {
            width: 100%;
            padding: 0 1rem;
        }
        
        /* Add custom styles for Streamlit components */
        .css-1cpxqw2 {
            border-color: white;
        }
    </style>

    <div class="bottom-container">
        <div class="logo">SCoP</div>
        <!-- This input box will be moved to Streamlit component area -->
    </div>
"""

# Inject custom styles and logo into the Streamlit app
st.markdown(html_string, unsafe_allow_html=True)

# Create a placeholder to display the result above the input box
result_placeholder = st.empty()

# Text input box with placeholder
user_input = st.text_input("", placeholder="Ask SCoP", key="prompt_input")

# Display the result above the input box
if user_input:
    result_placeholder.markdown(f"You entered: {user_input}", unsafe_allow_html=True)

# The rest of your genAI tool logic will go here





