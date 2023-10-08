from . import Release
from .architectures import Llama, Llama2, Mistral
from .templates import Llama, Llama2, Mistral


class Mistral_7b(Release):
    def __init__(self):
        super().__init__(
            architecture=Mistral(),
            parameters="7b",
            template=Mistral(),
            name="TheBloke/Mistral-7B-OpenOrca-GGUF",
            quant="Q6_K"
        )
