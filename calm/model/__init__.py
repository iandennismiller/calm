import os
from glob import glob

from llama_cpp import Llama as LlamaCpp


class Initialization:
    """
    An initialization consists of the values provided to the LLM engine.
    """

    def __init__(self, temperature):
        self.temperature = temperature

class Template:
    """
    The template describes the structure of the input a model release is trained on.
    By following the trained template when providing input to the model, the model will be able to generate more accurate output.
    """
    def __init__(self, prompt_input, prompt_no_input, response_split):
        self.prompt_input = prompt_input
        self.prompt_no_input = prompt_no_input
        self.response_split = response_split

class Prompt:
    """
    The prompt, or system prompt, provides the model with general instructions for how to handle input, context, and query to generate output.
    The prompt can influence a model to produce a summary, answer a question, generate a story, and so on.
    """
    def __init__(self, system_message):
        self.system_message = system_message

class Architecture:
    """
    Language models differ in their architecture.
    The architecture describes how the model is structured, including layers, connections, and activation functions.
    The architecture provides a foundation for varying its weights in order to learn different inputs.
    The architecture implies the context size, which is determined during training.
    """
    def __init__(self, kind, context_size):
        self.kind = kind # llama, llama2, mistral...
        self.context_size = context_size

class Release:
    """
    A Release is an architecture that has been trained with a specific set of inputs, or that is produced by combining weights from similar architectures.
    A release combines an architecture, the number of parameters, its trained/learned weights (as written to a file), and a compatible template.
    """
    def __init__(self, architecture, parameters, template, name, quant):
        self.architecture = architecture
        self.parameters = parameters
        self.template = template
        self.name = name
        self.quant = quant
    
    def resolve_path(self):
        self.root_path = os.path.expanduser("~/.ai/models/llama")
        model_filename = glob(f"{self.root_path}/{self.name}/*{self.quant}*")
        if model_filename:
            return model_filename[0]

class KnowledgeBase:
    """
    Knowledge is represented as a vectore store.
    A KnowledgeBase is a specific collection of knowledge.
    The KnowledgeBase could represent a set of documents or other information that a language model might use to generate output.
    """
    pass

class Instance:
    """
    An instance is a specific combination of a model release (which implies architecture and template), initialization, prompt, and optionally a knowledgebase.
    """
    def __init__(self, release, initialization, prompt, knowledgebase=None):
        self.release = release
        self.initialization = initialization
        self.prompt = prompt
        self.knowledgebase = knowledgebase
        self.llm = None

    def resolve_llm(self, num_threads, gpu_layers):
        self.num_threads = num_threads
        self.gpu_layers = gpu_layers

        if self.llm is None:
            self.llm = LlamaCpp(
                model_path=self.release.resolve_path(),
                n_ctx=self.release.architecture.context_size,
                n_threads=self.num_threads,
                n_gpu_layers=self.gpu_layers,
                verbose=False,
                seed=-1,
            )
        return self.llm


class Character:
    """
    A character is a prompt that is used to generate output in a specific style.
    """
    pass
