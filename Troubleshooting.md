## Basic Troubleshooting

By default, Ollama runs on:

http://localhost:11434

You can check whether Ollama is running on Windows using these methods.

### Method 1 — Simple Browser Check

Open browser:

http://localhost:11434

If Ollama is running, you’ll see something like:

```json
Ollama is running
```

### Method 2 — Git Bash / Terminal

Run:

curl http://localhost:11434

Expected response:

```shell
Ollama is running
```

### Method 3 — Check Listening Port in Windows

Open CMD or PowerShell:

```pwsh
netstat -ano | findstr 11434
```

If running, you’ll see:

```shell
TCP    127.0.0.1:11434    LISTENING
```

### Method 4 — Check Running Models/API

Run:
```shell
curl http://localhost:11434/api/tags
```

You’ll get installed models list.

Example:
```json
{
  "models": [
    {
      "name": "phi3"
    }
  ]
}
```

### Method 5 — Start Ollama Manually

If not running:

```shell
ollama serve
```

Then open another terminal:
```shell
ollama list
```