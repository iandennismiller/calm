# Calm: A peaceful user experience for Language Models

Calm makes it easier to manage language models, prompts, parameters, and the rest.
Calm uses `llama-cpp-python`, which is itself a wrapper around `llama.cpp`.
Calm supports Apple Silicon out of the box - but broader support is forthcoming.

## Install

```bash
pip install "git+https://github.com/iandennismiller/calm"
```

Optionally, install inside a virtual environment.

## List available model releases

```bash
calm list
```

## Get a model

The following downloads a model called Mistral OpenOrca to a folder called `~/.ai/models/llama`.

```bash
calm download mistral-7b-openorca
```

## Ask a question

Ask a question on the command line:

```bash
calm ask "What is the meaning of life?"
```

## Launch API server

Run the OpenAI-compatible API on localhost:

```bash
calm api
```
