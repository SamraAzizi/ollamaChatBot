# AI Chatbot using LangChain and Ollama

This project implements a conversational AI chatbot using the `langchain_ollama` library, specifically leveraging the `OllamaLLM` model. The chatbot is designed to maintain context throughout the conversation, allowing for more coherent and relevant responses.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
- [Code Explanation](#code-explanation)
- [Contributing](#contributing)
- [License](#license)

## Features

- Conversational AI that maintains context.
- Simple command-line interface.
- Easy to extend and modify for additional functionality.

## Requirements

- Python 3.7 or higher
- `langchain_ollama` library
- `langchain_core` library

## Installation

To install the required libraries, you can use pip:

```bash
pip install langchain_ollama langchain_core

```

# Usage
1. Clone the repository or download the script.
2. Run the script using python:

```bash
python chatbot.py
```

3. Interact with the chatbot through the command line. Type your questions and receive answers from the AI. Type 'exit' to quit the conversation.

# Code Explanation

The main components of the code are as follows:

- Imports: The necessary classes are imported from the langchain_ollama and langchain_core libraries.

- Template: A string template is defined to format the conversation history and the user's question.

- Model Initialization: The OllamaLLM model is initialized with the model name "llama3".

- Prompt Template: A ChatPromptTemplate is created from the defined template.

- Chain Creation: A chain is created by combining the prompt template and the model.

- Conversational Function: The handle_conversational function manages the user interaction:

- It initializes an empty context.
- It enters a loop to accept user input until 'exit' is typed.
- It invokes the chain with the current context and user question, retrieves the AI's response, and updates the context accordingly.