from strands import Agent
from strands.models.ollama import OllamaModel

# Point to your local Ollama instance
model = OllamaModel(
    model_id="phi3",          # must match the name shown in `ollama list`
    host="http://localhost:11434"  # default Ollama port
)

# Initialize agent with local model
agent = Agent(
    model=model,
    system_prompt="You are a helpful assistant that provides concise responses."
)

# Same usage as the AWS example
response = agent("Hello! Tell me a joke.")
print(response)
