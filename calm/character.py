import os
import yaml


class Character:
    """
    An instance is a specific combination of a model release (which implies architecture and template), initialization, prompt, and optionally a knowledgebase.
    """
    def __init__(self, name, system_prompt, temperature, model, guidance=False):
        self.name = name
        self.system_prompt = system_prompt
        self.temperature = temperature
        self.model = model
        self.guidance = guidance

    @classmethod
    def from_config(cls, name=None, filename=None):
        if (name is None and filename is None) or (name is not None and filename is not None):
            raise Exception("Must specify either name or filename")
        if name:
            filename = f"{os.path.dirname(__file__)}/../calm_data/characters/{name}.yaml"
        with open(filename, "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return cls(
            name=config["name"],
            system_prompt=config["system_prompt"],
            temperature=config["temperature"],
            model=config["model"],
            guidance=config["guidance"] if "guidance" in config else False,
        )

    def __repr__(self):
        return f"Character({self.name})"
