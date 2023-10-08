from . import Prompt

class Chat(Prompt):
    """
    The chat prompt is used to generate output in a conversational style.
    """
    def __init__(self):
        super().__init__(
            system_message="""\
A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\
""")

class Instruct(Prompt):
    """
    The instruct prompt is used to generate output in an instructional style.
    """
    def __init__(self):
        super().__init__(
            system_message="""\
A set of instructions for an artificial intelligence assistant. The assistant follows the instructions to complete a task.\
""")
