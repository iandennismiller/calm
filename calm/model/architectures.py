from . import Architecture

class Llama(Architecture):
    def __init__(self):
        super().__init__(
            kind="llama",
            context_size=2048
        )

class Llama2(Architecture):
    def __init__(self):
        super().__init__(
            kind="llama2",
            context_size=4096
        )

class Mistral(Architecture):
    def __init__(self):
        super().__init__(
            kind="mistral",
            context_size=8192
        )
