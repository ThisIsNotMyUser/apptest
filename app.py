import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='GenAI Tool', layout='centered')

# Define the custom HTML and CSS to use
html_string = """
    <style>
        .logo {
            font-family: 'Arial', sans-serif;
            font-size: 2em;
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
    </style>

    <div class="logo">
        <span>S</span><span>C</span><span>O</span><span>P</span><span>I</span><span>L</span><span>O</span><span>T</span>
    </div>
"""

# Use the HTML string with markdown to create the logo with the hover effect
st.markdown(html_string, unsafe_allow_html=True)

# Instructions
st.write("Enter your prompt in the text box below and hit enter to see the magic.")

# Text input box at the bottom
user_input = st.text_input("Prompt", key="prompt_input")

# You can now use the user_input variable to pass to your genAI tool
# For example:
# if user_input:
#    response = your_genai_function(user_input)
#    st.write(response)

# Display something once the user enters a prompt
if user_input:
    st.write("You entered: ", user_input)

# The rest of your genAI tool logic will go here


