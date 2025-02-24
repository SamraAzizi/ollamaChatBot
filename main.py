from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """

answer the question below.

Here is the conversation hisotry : {context}

Question: {question}

Answer: 

"""

model = OllamaLLM(model=llama3)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model

def handle_conversational():
    context = ""
    print("Welcome To The AI Chatbot! Type 'exit' to quit.")
    while True:
        

result = chain.invoke({"context": "", "question": "what is the capital of france?"})
print(result)