from .model import Instance
from .releases import Mistral_7b, TinyLlama, Samantha_33b
from .initializations import Factual
from .prompts import ChatPrompt, InstructPrompt, CouncilPrompt


class Answerer(Instance):
    """
    An Answerer is an instance that can answer questions.
    """
    def __init__(self):
        super().__init__(
            release=Mistral_7b(),
            initialization=Factual(),
            prompt=ChatPrompt()
        )

class Assistant(Instance):
    """
    An Assistant is an instance that can follow instructions.
    """
    def __init__(self):
        super().__init__(
            release=Mistral_7b(),
            initialization=Factual(),
            prompt=InstructPrompt()
        )

class Council(Instance):
    """
    A Council is an instance that can answer questions.
    """
    def __init__(self):
        super().__init__(
            release=Samantha_33b(),
            initialization=Factual(),
            prompt=CouncilPrompt()
        )
