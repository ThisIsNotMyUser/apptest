import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='SCoP', layout='centered')

# Define the custom HTML and CSS to use
html_string = """
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');

    body {
      display: flex;
      justify-content: center;
      align-items: center;
      height: 100vh;
      margin: 0;
      background-color: #414141ff;
    }

        .logo {
            font-family: 'Montserrat', sans-serif;
            font-size: 4em; /* 2 times larger */
            text-transform: uppercase;
            color: white; /* White text color for the logo */
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

        /* Change Streamlit components to the dark theme */
        .stTextInput .st-bb, .stTextInput .st-eb, .stTextInput .css-1cpxqw2 {
            background-color: #414141ff;
            color: white;
            border-color: white;
        }

        /* This targets all Streamlit text */
        .stTextInput, .st-bb, .st-da, .st-ea, .css-10trblm {
            font-family: 'Montserrat', sans-serif;
            color: white;
        }

        /* Override default Streamlit styling for other elements */
        .st-bv, .st-bw, .st-bx, .stButton>button {
            background-color: #414141ff;
            color: white;
            border-color: white;
        }
    </style>



<div class="logo">
  <span class="large">S</span>
  <span class="large">C</span>
  <span class="small">O</span>
  <span class="large">P</span>
  <span class="small hidden">i</span>
  <span class="small hidden">l</span>
  <span class="small hidden">o</span>
  <span class="small hidden">t</span>
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
