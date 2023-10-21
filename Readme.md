# Calm: A peaceful user experience for Large Language Models

Calm is a python 3.9+ package that makes it easier to work with large language models, including downloading the model and talking to it.

Calm automatically uses the right template for each model, supports multiple prompting styles, and chooses parameters based on your CPU, GPU and RAM.

Calm also provides advanced LLM features like Retrieval-Augmented Generation (RAG) with [chromadb](https://github.com/chroma-core/chroma), multi-turn prompting with [Guidance](https://github.com/guidance-ai/guidance), and an OpenAI-compatible API to support external clients.

Calm is accelerated on Apple Silicon out of the box thanks to [llama.cpp](https://github.com/ggerganov/llama.cpp/).
Windows and Linux should generally work without GPU acceleration.

## Quick Start

### Installation

```bash
pip install "git+https://github.com/iandennismiller/calm"
```

### Usage

1. download a language model
2. ask a question
3. add to knowledge
4. ask a question using knowledge

```bash
calm download
calm say "What is the meaning of life?"
calm learn "My name is Gilgamesh."
calm say --kb "What is my name?"
```

## Usage

### List available models

```bash
calm list
```

```bash
mistral
samantha
mistral-openorca
```

### Ask a question

Ask a question on the command line.
Calm will create a model Instance to answer the question.

```bash
calm say "What is the meaning of life?"
```

> AI Assistant: The meaning of life is a complex and multifaceted concept that has been pondered by philosophers, scientists, and individuals throughout history. There isn't a single definitive answer to this question, as it depends on one's personal beliefs, values, and experiences. However, some common themes in the search for meaning include finding purpose, happiness, and fulfillment through relationships, personal growth, and contributing positively to society.

Be sure to put quotes around the question so it is treated as a single argument.

To talk to a specific model, use the `-m` flag:

```bash
calm say -m samantha "How are you today?"
```

To talk to a specific character, use the `-c` flag:

```bash
calm say -c mixture-of-experts "How can we reduce traffic?"
```

### Download a model

Downloads a model called Samantha to a folder called `~/.local/share/calm/models`.

Calm will choose the right quant automatically by examining system RAM.

```bash
calm download samantha
```

### Retrieval-Augmented Generation

`calm` can learn and recall facts in a knowledgebase.
By default, the storage path is `~/.local/share/calm/kb`.

```bash
calm learn "I use github"
calm learn "I write code"
calm learn "I store my code on github"
calm learn "My name is Gilgamesh"
calm recall "name"
```

`calm` can retrieve knowledge to provide context for LLM response generation.
Provide the `-k` flag to tell `calm` to use knowledge:

```bash
calm say -k "Where does Gilgamesh store their code?"
```

```txt
Gilgamesh stores their code on GitHub
```

Store each knowledgebase in a separate path.

```bash
calm learn --path /tmp/kb1 "Facts about client 1"
calm learn --path /tmp/kb2 "Facts about client 17"
calm say --path /tmp/kb1 "Which client do I know facts about?"
```

### Consult a simulated Mixture of Experts

Using multi-turn prompting with [Guidance](https://github.com/guidance-ai/guidance), simulate a [Mixture of Experts](https://en.wikipedia.org/wiki/Mixture_of_experts) and ask them a question.
This uses the character flag `-c` to select [mixture-of-experts](https://github.com/iandennismiller/calm/blob/main/calm_data/characters/mixture-of-experts.yaml).

```bash
calm say -c mixture-of-experts "How can we reduce traffic?"
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

Use the mixture-of-experts character with the samantha model:

```bash
calm say -c mixture-of-experts -m samantha "How can we reduce traffic?"
```

### Launch API server

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

Run API with a specific model:

```bash
calm api -m samantha
```

### Based on your RAM, which model sizes can you run?

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

## Adding models and characters

To add a new model or character, create a new YAML description file in [the descriptions folder](https://github.com/iandennismiller/calm/tree/main/calm/descriptions):

- [model descriptions](https://github.com/iandennismiller/calm/tree/main/calm/descriptions/models)
- [characters descriptions](https://github.com/iandennismiller/calm/tree/main/calm/descriptions/characters)

Use these templates to get started:

- [blank_model.yaml](https://github.com/iandennismiller/calm/blob/main/calm/descriptions/blank_model.yaml)
- [blank_character.yaml](https://github.com/iandennismiller/calm/blob/main/calm/descriptions/blank_character.yaml)

Finally, please submit a pull request with your new YAML files in the descriptions folder.

## Models used by calm

`calm` automatically chooses the most sensible model size based on your system resources.
I've made opinionated choices in this regard and I believe the vast majority of use cases are supported by just three model sizes:

- `f16`: unquantized, largest size, slowest computation, and best results
- `Q6_k`: smaller and faster than unquantized, good results, often better than q8_0
- `Q4_K_S`: smallest quant that still produces acceptable results

The following models described as YAML for calm:

- [mistral](https://huggingface.co/iandennismiller/mistral-v0.1-7b-GGUF)
- [mistral-openorca](https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF)
- [tinyllama-chat](https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF)
- [medtext](https://huggingface.co/iandennismiller/LLama-2-MedText-13b-GGUF)
- [samantha](https://huggingface.co/iandennismiller/samantha-1.1-llama-33b-GGUF)

I would be remiss if I didn't mention the important contributions of [TheBloke](https://huggingface.co/TheBloke), who has provided great coverage of model quants.
In some cases, I am directly re-hosting models they have quantized - but in most cases, I've performed my own conversions and quantizations to meet the specific goals of `calm`.

### Rational for quants

I refer to the [llama.cpp quantize example](https://github.com/ggerganov/llama.cpp/tree/master/examples/quantize) to examine the impact of quantization upon perplexity.

```txt
   2  or  Q4_0   :  3.56G, +0.2166 ppl @ LLaMA-v1-7B
   3  or  Q4_1   :  3.90G, +0.1585 ppl @ LLaMA-v1-7B
   8  or  Q5_0   :  4.33G, +0.0683 ppl @ LLaMA-v1-7B
   9  or  Q5_1   :  4.70G, +0.0349 ppl @ LLaMA-v1-7B
  10  or  Q2_K   :  2.63G, +0.6717 ppl @ LLaMA-v1-7B
  12  or  Q3_K   : alias for Q3_K_M
  11  or  Q3_K_S :  2.75G, +0.5551 ppl @ LLaMA-v1-7B
  12  or  Q3_K_M :  3.07G, +0.2496 ppl @ LLaMA-v1-7B
  13  or  Q3_K_L :  3.35G, +0.1764 ppl @ LLaMA-v1-7B
  15  or  Q4_K   : alias for Q4_K_M
  14  or  Q4_K_S :  3.59G, +0.0992 ppl @ LLaMA-v1-7B
  15  or  Q4_K_M :  3.80G, +0.0532 ppl @ LLaMA-v1-7B
  17  or  Q5_K   : alias for Q5_K_M
  16  or  Q5_K_S :  4.33G, +0.0400 ppl @ LLaMA-v1-7B
  17  or  Q5_K_M :  4.45G, +0.0122 ppl @ LLaMA-v1-7B
  18  or  Q6_K   :  5.15G, -0.0008 ppl @ LLaMA-v1-7B
   7  or  Q8_0   :  6.70G, +0.0004 ppl @ LLaMA-v1-7B
   1  or  F16    : 13.00G              @ 7B
   0  or  F32    : 26.00G              @ 7B
```

According to these results, Q8_0 is a little worse than Q6_K despite being larger.
Therefore, I've opted for Q6_K in all cases.
I selected Q4_K_S for smaller systems as a compromise; perplexity is severely impacted below that size.

## Libraries used by calm

The following projects are used by `calm` to support large language models.

- [llama.cpp](https://github.com/ggerganov/llama.cpp)
- [llama-cpp-python](https://github.com/abetlen/llama-cpp-python)
- [llama-cpp-guidance](https://github.com/nicholasyager/llama-cpp-guidance)
- [guidance](https://github.com/guidance-ai/guidance)
- [chromadb](https://github.com/chroma-core/chroma)
