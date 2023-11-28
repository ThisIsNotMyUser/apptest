import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='GenAI Tool', layout='centered')

# Define the custom HTML and CSS to use
html_string = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

        body {
            font-family: 'Montserrat', sans-serif;
        }

        .logo {
            font-family: 'Montserrat', sans-serif;
            font-size: 4em; /* 2 times larger */
            text-transform: uppercase;
            color: #3498db;
            cursor: pointer;
        }

        .logo span {
            display: inline-block;
        }

        .logo span:hover {
            animation: distort 0.5s ease-in-out infinite;
        }

        @keyframes distort {
            0% {
                transform: skewX(0deg) skewY(0deg);
            }
            25% {
                transform: skewX(10deg) skewY(10deg);
            }
            50% {
                transform: skewX(-10deg) skewY(-10deg);
            }
            75% {
                transform: skewX(5deg) skewY(5deg);
            }
            100% {
                transform: skewX(0deg) skewY(0deg);
            }
        }

        /* This ensures that all text uses the Montserrat font */
        .stTextInput, .st-bb, .st-da, .st-ea, .css-10trblm, .stButton>button {
            font-family: 'Montserrat', sans-serif;
        }
    </style>

    <div class="logo">
        <span>G</span><span>e</span><span>n</span><span>A</span><span>I</span>
        <span>T</span><span>o</span><span>o</span><span>l</span>
    </div>
"""

# Use the HTML string with markdown to create the logo with the hover effect
st.markdown(html_string, unsafe_allow_html=True)

# Inject the Montserrat font into the Streamlit app
st.markdown(
    """
    <style>
        html, body, [class*="st-"] {
            font-family: 'Montserrat', sans-serif;
        }
    </style>
    """,
    unsafe_allow_html=True
)

# Instructions
st.write("Enter your prompt in the text box below and press the arrow button to see the magic.")

# Text input box with a submit button
user_input = st.text_input("Prompt", key="prompt_input")
submit_button = st.button("🔼")

# You can now use the user_input variable to pass to your genAI tool
# For example:
# if submit_button:
#    response = your_genai_function(user_input)
#    st.write(response)

# Display something once the user enters a prompt and clicks the submit button
if submit_button:
    st.write("You entered: ", user_input)

# The rest of your genAI tool logic will go here


