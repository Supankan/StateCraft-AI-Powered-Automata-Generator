import pathlib
import textwrap
from dotenv import load_dotenv
import google.generativeai as genai
import os
import re

# Load environment variables
load_dotenv()
API_KEY = os.getenv('GOOGLE_API_KEY')

# Configure Gemini API
model = genai.GenerativeModel('gemini-1.5-flash')
genai.configure(api_key=API_KEY)


# Function to send a prompt to Gemini API
def prompt(input_user):
    input_test = (f"Give me the Python code to generate the following automata. "
                  f"It could be DFA, NFA, or epsilon NFA. Use graphviz library for this. Save it as a PNG file only."
                  f"The states should be named q0, q1, q2 (or A, B, C) without any descriptive labels. "
                  f"You must specify the start state with an arrow as well {input_user}")
    response = model.generate_content(input_test)
    return response.text  # Extract the generated text directly


# Extract pure Python code from the response
def extract_python_code(response_text):
    # Use regex to capture text within Python code block
    match = re.search(r'```python(.*?)```', response_text, re.DOTALL)
    if match:
        return match.group(1).strip()  # Extract and clean the code block
    else:
        print("No valid Python code block found in the response.")
        return None


if __name__ == '__main__':
    input_user = str(input("Enter the Prompt: "))
    generated_response = prompt(input_user)

    # Save the raw response for debugging
    with open('raw_response.txt', 'w') as file:
        file.write(generated_response)

    # Extract Python code
    generated_code = extract_python_code(generated_response)

    if generated_code:
        # Save the extracted code to a file for inspection
        with open('generated_automata.py', 'w') as file:
            file.write(generated_code)

        print("Generated code saved to 'generated_automata.py'.")

        # Execute the extracted code
        print("\nExecuting the generated code...\n")
        try:
            exec(generated_code)  # Execute the extracted Python code
            print("Execution completed.")
        except Exception as e:
            print(f"Error in executing the generated code: {e}")
    else:
        print("No executable Python code generated.")
