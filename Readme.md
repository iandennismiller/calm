# Calm: A peaceful user experience for Large Language Models

Calm makes it easier to manage large language models, templates, prompts, parameters, and the rest.

Calm supports Apple Silicon out of the box. Windows and Linux are coming.

Calm uses `llama-cpp-python`, which is itself a wrapper around `llama.cpp`.

## Quick Start

Install the python package, download the default language model, and ask a question.

```bash
pip install "git+https://github.com/iandennismiller/calm"
calm download mistral-7b-openorca
calm ask "What is the meaning of life?"
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

The following downloads a model called Samantha v1.1 33b to a folder called `~/.ai/models/llama`.

```bash
calm download samantha-33b
```

```bash
Downloading...
```

## Ask a question

Ask a question on the command line:

```bash
calm ask "What is the meaning of life?"
```

> AI Assistant: The meaning of life is a complex and multifaceted concept that has been pondered by philosophers, scientists, and individuals throughout history. There isn't a single definitive answer to this question, as it depends on one's personal beliefs, values, and experiences. However, some common themes in the search for meaning include finding purpose, happiness, and fulfillment through relationships, personal growth, and contributing positively to society.

## Consult a "mixture of experts"

```bash
calm consult "How can we reduce traffic?"
```

```chatml
<|im_start|>system
You are a helpful and terse assistant.<|im_end|>

<|im_start|>user
I want a response to the following question:
How can we reduce traffic?
Name 3 world-class experts (past or present) who would be great at answering this?
Don't answer the question yet.<|im_end|>

<|im_start|>assistant
I understand that you want me to provide information without directly answering the question. Here are 3 world-class experts and their respective fields, who could potentially offer valuable insights on reducing traffic ...<|im_end|>
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

## Based on your RAM, which model sizes can you run?

When I run this on my MBP M1 with 32gb ram, I get the following output:

```bash
calm max
```

```bash
180b    too big
70b     too big
30b     Q4_K_S quant    2048 context
13b     Q6_K quant      8192 context
7b      Q6_K quant      8192 context
3b      Q6_K quant      8192 context
1b      Q6_K quant      8192 context
```

It is possible for your system to support a larger context than the model architecture provides.
