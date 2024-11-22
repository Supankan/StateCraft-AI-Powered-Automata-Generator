# Automata Generator

Welcome to the **Automata Generator** project! This repository contains two versions of an application that generates automata (DFA, NFA, or ε-NFA) based on user input. The automata are visualized using the `graphviz` library and saved as PNG images. The project utilizes the Gemini API to generate Python code for the automata creation process.

## Features

- **Two Versions**: 
  - **Base Version**: A command-line version that generates and saves the automata as an image file.
  - **Streamlit Version**: A user-friendly web application that allows you to input automata descriptions and visualize the results in your browser.
  
- **Automata Types**: You can generate DFA (Deterministic Finite Automaton), NFA (Nondeterministic Finite Automaton), or ε-NFA (epsilon Nondeterministic Finite Automaton).
  
- **Easy Visualization**: The generated automata are displayed as images, and you can download them directly from the Streamlit app.

## Setup

To run this project, you need to set up the required dependencies and the environment for the Gemini API.

### Prerequisites

- Python 3.7 or higher
- Streamlit (for the Streamlit version)
- Graphviz (for generating automata visuals)
- Google Gemini API key
