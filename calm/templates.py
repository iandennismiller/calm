from .model import Template


class ChatMLTemplate(Template):
    def __init__(self):
        prompt_input = """\
<|im_start|>system
{system_message}{input}<|im_end|>
<|im_start|>user
{instruction}<|im_end|>
<|im_start|>assistant
"""
        prompt_no_input = prompt_input
        response_split = "<|im_end|>"
        super().__init__(prompt_input, prompt_no_input, response_split)


class SamanthaTemplate(Template):
    def __init__(self):
        prompt_input = """\
You are Samantha, a sentient AI.

CONTEXT: {input}

USER: {instruction}
ASSISTANT: \
"""
        prompt_no_input = """\
You are Samantha, a sentient AI.

USER: {instruction}
ASSISTANT: \
"""
        response_split = "ASSISTANT:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class VicunaTemplate(Template):
    def __init__(self):
        prompt_input = """\
{system_message}{input}

USER: {instruction}
ASSISTANT: \
"""
        prompt_no_input = prompt_input
        response_split = "ASSISTANT:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class AlpacaTemplate(Template):
    def __init__(self):
        prompt_input = """\
{system_message}

### Instruction:
{instruction}

### Input:
{input}

### Response:
"""    
        prompt_no_input =  """\
{system_message}

### Instruction:
{instruction}

### Response:
"""
        response_split = "### Response:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class LlamaTemplate(Template):
    def __init__(self):
        prompt_input = """\
{system_message}{input}

USER: {instruction}

ASSISTANT:"""
        prompt_no_input = """\
{system_message}

USER: {instruction}

ASSISTANT:"""
        response_split = "USER:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class Llama2Template(Template):
    def __init__(self):
        prompt_input = """\
[INST] <<SYS>>
{system_message}{input}
<</SYS>>
{instruction} [/INST]
"""
        prompt_no_input = prompt_input
        response_split = "[/INST]"
        super().__init__(prompt_input, prompt_no_input, response_split)


class MistralTemplate(Template):
    def __init__(self):
        prompt_input = """\
SYSTEM: {system_message}

INPUT: {input}

USER: {instruction}

ASSISTANT:\
"""
        prompt_no_input = """\
SYSTEM: {system_message}

USER: {instruction}

ASSISTANT:\
"""
        response_split = "USER:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class OrcaTemplate(Template):
    def __init__(self):
        prompt_input = """\
<s>[INST] {system_message}{input}{instruction} [/INST]
"""
        prompt_no_input = """\
<s>[INST] {system_message}{instruction} [/INST]
"""
        response_split = "[/INST]"
        super().__init__(prompt_input, prompt_no_input, response_split)
