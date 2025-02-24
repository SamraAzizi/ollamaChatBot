from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
Answer the question below.

Here is the conversation history: {context}

Question: {question}

Answer:
"""

model = OllamaLLM(model="llama3")  # Ensure "llama3" is passed as a string
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversational():
    context = ""
    print("Welcome To The AI Chatbot! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            break

        result = chain.invoke({"context": context, "question": user_input})
        response_text = result.get("output", "")  # Extracting the response properly

        print(f"AI: {response_text}")
        context += f"\nUser: {user_input}\nAI: {response_text}"  # Update context with response

if __name__ == "__main__":
    handle_conversational()
