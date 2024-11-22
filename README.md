# StateCraft: Automata Generator 🤖📐

## Overview
StateCraft is an innovative automata generation tool that leverages the power of Google's Gemini AI to create state machine diagrams based on natural language descriptions.

## Versions

### StateCraft V1 (Command-Line Version)
#### Features
- Generates automata diagrams using command-line input
- Uses Gemini API for code generation
- Saves automata as PNG files
- Manual execution of generated code

#### Requirements
- Python 3.8+
- Google Generative AI
- Graphviz
- python-dotenv

### StateCraft V2 (Streamlit UI Version)
#### Features
- Web-based user interface
- Real-time automata generation
- Code preview
- One-click PNG download
- Powered by Streamlit and Gemini API

#### Requirements
- Python 3.8+
- Streamlit
- Google Generative AI
- Graphviz
- python-dotenv
- Pillow

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/yourusername/statecraft.git
cd statecraft
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Configure API Key
Create a `.env` file in the project root:
```
GOOGLE_API_KEY=your_google_api_key_here
```

## Usage

### V1 (Command-Line)
```bash
python StateCraft_V1.py
```
Follow the prompt to enter your automata description.

### V2 (Streamlit)
```bash
streamlit run StateCraft_V2_ST.py
```
Open the generated local URL in your browser.

## Example Prompts
- "Create a DFA that accepts binary strings divisible by 3"
- "Generate an NFA that accepts strings starting with 'ab'"
- "Design an automata that checks for palindrome strings"

## Technology Stack
- 🤖 AI Generation: Google Gemini API
- 📊 Visualization: Graphviz
- 🖥️ UI Framework: Streamlit
- 🐍 Language: Python

## Limitations
- Requires a valid Google Generative AI API key
- Dependent on AI's ability to generate correct code
- Internet connection needed for API calls
