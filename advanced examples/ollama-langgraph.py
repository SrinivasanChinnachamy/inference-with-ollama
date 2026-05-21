import warnings
warnings.filterwarnings("ignore")

from langchain_ollama import ChatOllama
from langgraph.prebuilt import create_react_agent

# Connect to Ollama
llm = ChatOllama(model="phi3")

# Create an agent
agent = create_react_agent(model=llm, tools=[])

# Ask a question
response = agent.invoke({
    "messages": [{"role": "user", "content": "Tell me a joke!"}]
})

# Print the reply
print(response["messages"][-1].content)
