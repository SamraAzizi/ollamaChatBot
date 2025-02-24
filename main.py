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
result = model.invoke(input="hello world")
print(result)