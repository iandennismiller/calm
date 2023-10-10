from .model import Prompt

class ChatPrompt(Prompt):
    """
    The chat prompt is used to generate output in a conversational style.
    """
    def __init__(self):
        super().__init__(
            system_prompt="""\
A chat between a curious human and an artificial intelligence assistant. The assistant gives helpful, detailed, and polite answers to the human's questions.\
""")

class InstructPrompt(Prompt):
    """
    The instruct prompt is used to generate output in an instructional style.
    """
    def __init__(self):
        super().__init__(
            system_prompt="""\
A set of instructions for an artificial intelligence assistant. The assistant follows the instructions to complete a task.\
""")

class CouncilPrompt(Prompt):
    """
    The council prompt is used to generate output in a deliberative style.
    """
    def __init__(self):
        super().__init__(
            system_prompt='''
{{#system~}}
You are a helpful and terse assistant.
{{~/system}}

{{#user~}}
I want a response to the following question:
{{query}}
Name 3 world-class experts (past or present) who would be great at answering this?
Don't answer the question yet.
{{~/user}}

{{#assistant~}}
{{gen 'expert_names' temperature=0.05 max_tokens=300}}
{{~/assistant}}

{{#user~}}
Great, now please answer the question as if these experts had collaborated in writing a joint anonymous answer.
{{~/user}}

{{#assistant~}}
{{gen 'answer' temperature=0.05 max_tokens=500}}
{{~/assistant}}
''')
