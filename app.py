import streamlit as st

# Set the page config to widen the app, and set a title and icon
st.set_page_config(page_title='SCoP', layout='centered')
left_column, center_column, right_column = st.columns([1, 50, 1])

# Use the center column for your content
with center_column:
    # Define the custom HTML and CSS to use
    html_string = """
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@400;700&display=swap');
    
    
     
        .logo {
          font-family: 'Montserrat', sans-serif;
          justify-content: center;
           align-items: center;
          font-size: 2em;
          text-transform: uppercase;
          position: relative;
          color: #ffffff;
        }
    
        .logo span {
          display: inline-block;
          transition: transform 0.3s ease-in-out;
        }
    
        .logo span.large {
          font-size: 1.5em; /* Adjust the size as needed */
          font-weight: 700;
        }
    
        .logo span.small {
          font-size: 1em; /* Adjust the size as needed */
        }
    
        .logo span.hidden {
          opacity: 0;
          transition: opacity 0.5s ease-in-out; /* Adjust the duration as needed */
        }
    
    
        .logo:hover .small {
          opacity: 1;
          transition: opacity 1s ease-in-out; /* Adjust the duration as needed */
        }
    
        .magnifyspan {
          animation: magnify 0.5s ease-in-out infinite;
        }
    
        .logo span.animated {
          animation: moveMagnify 5s linear alternate;
        }
        
        .logo span:hover {
          transform: scale(1.2); /* Magnifying effect on hover */
        }    
    
        @keyframes magnify {
          0% {
            transform: scale(1);
          }
          50% {
            transform: scale(1.2);
          }
          100% {
            transform: scale(1);
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
      <div>
      <span class="large">S</span>
      <span class="large">C</span>
      <span class="small">O</span>
      <span class="large">P</span>
      <span class="small hidden">i</span>
      <span class="small hidden">l</span>
      <span class="small hidden">o</span>
      <span class="small hidden">t</span>
      </div><div style='text-align: left'>
      <img style='width: 15px;' src='https://upload.wikimedia.org/wikipedia/commons/2/2b/Valeo_Logo.svg'>
      </div>
    </div>
    
    
    """
    
    # Use the HTML string with markdown to create the logo with the hover effect
    st.markdown(html_string, unsafe_allow_html=True)
    
    # Inject the Montserrat font into the Streamlit app
    st.markdown(
        """
        <style>
            body {
                background-image: url('https://drive.google.com/file/d/1U8fZSvR-8pvsSs4AtiknBkZAu0SSVzeR/download')
                font-family: 'Montserrat', sans-serif;
                background-color: #414141ff;
                color: white;
            }
            
            html, [class*="st-"], .stTextInput, .st-bb, .st-da, .st-ea, .css-10trblm {
                font-family: 'Montserrat', sans-serif;
                background-color: #414141ff;
                color: white;
                  display: flex;
                  justify-content: center;
                  align-items: center;
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
            input::placeholder {
                opacity: 1;
                color: #FFFFFF !important;
            }
            


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
