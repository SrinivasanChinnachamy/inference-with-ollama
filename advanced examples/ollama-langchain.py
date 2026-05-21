from langchain_ollama import ChatOllama

# Connect to Ollama
llm = ChatOllama(model="phi3")

# Ask a question
response = llm.invoke("Tell me a joke!")

# Print the reply
print(response.content)
