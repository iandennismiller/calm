from . import Instance
from .releases import Mistral_7b
from .initializations import Factual
from .prompts import Chat, Instruct


class Answerer(Instance):
    """
    An Answerer is an instance that can answer questions.
    """
    def __init__(self):
        super().__init__(
            release=Mistral_7b(),
            initialization=Factual(),
            prompt=Chat()
        )

class Assistant(Instance):
    """
    An Assistant is an instance that can follow instructions.
    """
    def __init__(self):
        super().__init__(
            release=Mistral_7b(),
            initialization=Factual(),
            prompt=Instruct()
        )
