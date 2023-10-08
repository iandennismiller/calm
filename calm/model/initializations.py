from . import Initialization

class Factual(Initialization):
    def __init__(self):
        temperature = 0.05
        super().__init__(temperature=temperature)

class Creative(Initialization):
    def __init__(self):
        temperature = 0.51
        super().__init__(temperature=temperature)

