from .model import Release
from .architectures import MistralArchitecture, LlamaArchitecture
from .templates import MistralTemplate, LlamaTemplate, SamanthaTemplate, OrcaTemplate


class Mistral_7b(Release):
    def __init__(self):
        super().__init__(
            architecture=MistralArchitecture(),
            parameters="7b",
            template=MistralTemplate(),
            name="mistral-7b",
            hugging_id="iandennismiller/mistral-v0.1-7b-GGUF",
            hugging_url="https://huggingface.co/iandennismiller/mistral-v0.1-7b-GGUF/resolve/main/mistral-7b-v0.1.{quant}.gguf",
        )

class Mistral_7b_OpenOrca(Release):
    def __init__(self):
        super().__init__(
            architecture=MistralArchitecture(),
            parameters="7b",
            template=OrcaTemplate(),
            name="mistral-7b-openorca",
            hugging_id="TheBloke/Mistral-7B-OpenOrca-GGUF",
            hugging_url="https://huggingface.co/TheBloke/Mistral-7B-OpenOrca-GGUF/resolve/main/mistral-7b-openorca.{quant}.gguf",
        )

class TinyLlama(Release):
    def __init__(self):
        super().__init__(
            architecture=LlamaArchitecture(),
            parameters="1b",
            template=LlamaTemplate(),
            name="tiny-llama-1.1b-chat",
            hugging_id="TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF",
            hugging_url="https://huggingface.co/TheBloke/TinyLlama-1.1B-Chat-v0.3-GGUF/resolve/main/tinyllama-1.1b-chat-v0.3.{quant}.gguf",
        )

class Samantha_33b(Release):
    def __init__(self):
        super().__init__(
            architecture=LlamaArchitecture(),
            parameters="33b",
            template=SamanthaTemplate(),
            name="samantha-33b",
            hugging_id="iandennismiller/samantha-1.1-llama-33b-GGUF",
            hugging_url="https://huggingface.co/iandennismiller/samantha-1.1-llama-33b-GGUF/resolve/main/samantha-1.1-llama-33b.{quant}.gguf",
        )
