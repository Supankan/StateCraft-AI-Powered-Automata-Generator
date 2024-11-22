import streamlit as st
import pathlib
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
import os
import re
import glob

# Load environment variables
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure Gemini API
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize session state
if 'generated_code' not in st.session_state:
    st.session_state.generated_code = None
if 'png_file' not in st.session_state:
    st.session_state.png_file = None

# Page configuration
st.set_page_config(
    page_title="Automata Generator",
    page_icon="🤖",
    layout="centered"
)

# Title and description
st.title("🤖 Automata Generator")
st.markdown("""
This application generates automata (DFA, NFA, or ε-NFA) based on your description using the Gemini API.
Simply enter your requirements, and the app will generate the corresponding automata visualization.
""")


# Function to send a prompt to Gemini API
def prompt(input_user):
    input_test = (f"Give me the Python code to generate the following automata. "
                  f"It could be DFA, NFA, or epsilon NFA. Use graphviz library for this. Save it as a PNG file only. "
                  f"The states should be named q0, q1, q2 (or A, B, C) without any descriptive labels. "
                  f"You must specify the start state with an arrow as well {input_user}")
    try:
        response = model.generate_content(input_test)
        return response.text
    except Exception as e:
        st.error(f"Error generating response: {str(e)}")
        return None


# Extract pure Python code from the response
def extract_python_code(response_text):
    match = re.search(r'```python(.*?)```', response_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


# Function to find the most recent PNG file
def find_latest_png():
    png_files = glob.glob("*.png")
    if png_files:
        return max(png_files, key=os.path.getctime)
    return None


# Clean up old PNG files
def cleanup_old_files():
    png_files = glob.glob("*.png")
    for file in png_files:
        try:
            os.remove(file)
        except Exception as e:
            print(f"Error removing file {file}: {e}")


# Input section
user_prompt = st.text_area(
    "Enter your automata description:",
    height=100,
    placeholder="Example: Generate an automata that accepts strings containing 'ab' as a substring"
)

if st.button("Generate Automata", type="primary"):
    if user_prompt:
        with st.spinner("Generating automata..."):
            cleanup_old_files()
            generated_response = prompt(user_prompt)

            if generated_response:
                generated_code = extract_python_code(generated_response)

                if generated_code:
                    # Save to session state
                    st.session_state.generated_code = generated_code

                    try:
                        exec(generated_code)
                        png_file = find_latest_png()

                        if png_file and os.path.exists(png_file):
                            # Save to session state
                            with open(png_file, "rb") as file:
                                st.session_state.png_file = file.read()
                        else:
                            st.error("Image file was not generated successfully.")
                            st.session_state.png_file = None

                    except Exception as e:
                        st.error(f"Error executing the generated code: {str(e)}")
                        st.session_state.png_file = None
                else:
                    st.error("No valid Python code found in the response.")
            else:
                st.error("Failed to generate response from API.")
    else:
        st.warning("Please enter a prompt first.")

# Display code and download button if available
if st.session_state.generated_code:
    with st.expander("View Generated Code", expanded=False):
        st.code(st.session_state.generated_code, language='python')

if st.session_state.png_file:
    st.download_button(
        label="Download Automata Image",
        data=st.session_state.png_file,
        file_name="automata.png",
        mime="image/png"
    )

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>Built with ❤️ using Streamlit and Google's Gemini API</p>
    </div>
""", unsafe_allow_html=True)