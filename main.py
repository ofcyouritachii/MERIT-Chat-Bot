from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import PromptTemplate

model = OllamaLLM(
    model="tinyllama",
    base_url="http://localhost:11434"
)

template = """
You are a helpful tutor.
Explain {topic} in simple Hinglish.
"""

prompt = PromptTemplate(
    input_variables=["topic"],
    template=template
)

chain = prompt | model

response = chain.invoke({"topic": "API"})
print(response)
