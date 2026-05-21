## Getting Started

### 1.Pull the model

Pull the model from Ollama Library

```
ollama pull phi3
```

See [ollama.com/library](https://ollama.com/library) for the full list.

### 2.Chat with the model

Run and chat with [Phi 3](https://ollama.com/library/phi3):

```
ollama run phi3
```

See the [quickstart guide](https://docs.ollama.com/quickstart) for more details.

### REST API

Ollama has a REST API for running and managing models.

```
curl http://localhost:11434/api/chat -d '{
  "model": "phi3",
  "messages": [{
    "role": "user",
    "content": "Why is the sky blue?"
  }],
  "stream": false
}'
```

See the [API documentation](https://docs.ollama.com/api) for all endpoints.

### Python

```
pip install ollama
```

```python
from ollama import chat

response = chat(model='phi3', messages=[
  {
    'role': 'user',
    'content': 'Why is the sky blue?',
  },
])
print(response.message.content)
```

create a python file[chat.py] and move the above contents into it to execute them

```shell
python chat.py
```