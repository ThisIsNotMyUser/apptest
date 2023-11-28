# app.py
import streamlit as st

# Define the HTML and CSS
html_content = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <style>
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
      font-size: 1.5em;
      font-weight: 700;
    }
    .logo span.small {
      font-size: 1em;
    }
    .logo span.hidden {
      opacity: 0;
      transition: opacity 0.5s ease-in-out;
    }
    .logo:hover .small {
      opacity: 1;
      transition: opacity 1s ease-in-out;
    }
    .magnifyspan {
      animation: magnify 0.5s ease-in-out infinite;
    }
    .logo span.animated {
      animation: moveMagnify 5s linear alternate;
    }
    .logo span:hover {
      transform: scale(1.2);
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
  </style>
</head>
<body>

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

</body>
</html>
'''

# Using st.markdown to render HTML content
st.markdown(html_content, unsafe_allow_html=True)

# Continue with the rest of your Streamlit content
# ...

