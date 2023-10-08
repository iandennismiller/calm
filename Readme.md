# Calm: A peaceful user experience for Large Language Models

Calm makes it easier to manage large language models, templates, prompts, parameters, and the rest.

Calm supports Apple Silicon out of the box. Windows and Linux are coming.

Calm uses `llama-cpp-python`, which is itself a wrapper around `llama.cpp`.

## Install

```bash
pip install "git+https://github.com/iandennismiller/calm"
```

Optionally, install inside a virtual environment.

## List available model releases

```bash
calm list
```

```bash
mistral-7b-openorca
tiny-llama-1.1b-chat
samantha-33b
```

## Get a model

The following downloads a model called Mistral OpenOrca to a folder called `~/.ai/models/llama`.

```bash
calm download mistral-7b-openorca
```

```bash
Downloading...
```

## Ask a question

Ask a question on the command line:

```bash
calm ask "What is the meaning of life?"
```

```bash
AI Assistant: The meaning of life is a complex and multifaceted concept that has been pondered by philosophers, scientists, and individuals throughout history. There isn't a single definitive answer to this question, as it depends on one's personal beliefs, values, and experiences. However, some common themes in the search for meaning include finding purpose, happiness, and fulfillment through relationships, personal growth, and contributing positively to society.
```

## Launch API server

Run the OpenAI-compatible API on localhost:

```bash
calm api
```

```bash
INFO:     Started server process [99517]
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://localhost:8000 (Press CTRL+C to quit)
```
