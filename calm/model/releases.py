from . import Release
from .architectures import Mistral as mistral_architecture
from .templates import Mistral as mistral_template


class Mistral_7b(Release):
    def __init__(self):
        super().__init__(
            architecture=mistral_architecture(),
            parameters="7b",
            template=mistral_template(),
            name="TheBloke/Mistral-7B-OpenOrca-GGUF",
            quant="Q6_K"
        )
