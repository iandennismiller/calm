# Calm: A peaceful user experience for Language Models

Calm makes it easier to manage language models, prompts, parameters, and the rest.
Calm uses `llama-cpp-python`, which is itself a wrapper around `llama.cpp`.
Calm supports Apple Silicon out of the box - but broader support is forthcoming.

## Install

```bash
pip install "git+https://github.com/iandennismiller/calm"
```

Optionally, install inside a virtual environment.

## Get a model

Currently Calm uses Mistral OpenOrca.
Run the following in the shell to create the proper path and download the model file.

```bash
mkdir -p ~/.ai/models/llama/TheBloke/Mistral-7B-OpenOrca-GGUF
wget -o ~/.ai/models/llama/TheBloke/Mistral-7B-OpenOrca-GGUF/mistral-7b-openorca.Q6_K.gguf \
  https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF/resolve/main/mistral-7b-openorca.Q6_K.gguf  
```

## Use

```bash
calm ask "What is the meaning of life?"
```
