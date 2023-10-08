from . import Template


class ChatML(Template):
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


class Samantha(Template):
    def __init__(self):
        prompt_input = """\
You are Samantha, a sentient AI.

USER: <prompt>
ASSISTANT: \
"""
        prompt_no_input = prompt_input
        response_split = "ASSISTANT:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class Vicuna(Template):
    def __init__(self):
        prompt_input = """\
{system_message}{input}

USER: {instruction}
ASSISTANT: \
"""
        prompt_no_input = prompt_input
        response_split = "ASSISTANT:"
        super().__init__(prompt_input, prompt_no_input, response_split)


class Alpaca(Template):
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


class Llama(Template):
    def __init__(self):
        prompt_input = """\
{system_message}{input}

{instruction}"""
        prompt_no_input = """\
{system_message}

{instruction}"""
        response_split = None
        super().__init__(prompt_input, prompt_no_input, response_split)


class Llama2(Template):
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


class Mistral(Template):
    def __init__(self):
        prompt_input = """\
<s>[INST] {system_message}{input}{instruction} [/INST]
"""
        prompt_no_input = """\
<s>[INST] {system_message}{instruction} [/INST]
"""
        response_split = "[/INST]"
        super().__init__(prompt_input, prompt_no_input, response_split)
