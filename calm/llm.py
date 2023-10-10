import os
from glob import glob

import yaml
import requests

from llama_cpp import Llama as LlamaCpp

from .utils import get_resource_max, has_metal, get_cores, get_smaller_quants


class LLM:
    """
    A Release is an architecture that has been trained with a specific set of inputs, or that is produced by combining weights from similar architectures.
    A release combines an architecture, the number of parameters, its trained/learned weights (as written to a file), and a compatible template.
    """
    def __init__(self, name, input_size, source, template, model_size=None, quant=None, character=None):
        self.name = name
        self.input_size = input_size
        self.source = source
        self.template = template
        self.character = character

        biggest = self.get_biggest()

        if model_size is None:
            self.model_size = biggest["size"]
        else:
            self.model_size = model_size

        if quant is None:
            self.quant = biggest["quant"]
        else:
            self.quant = quant

        resource_max = get_resource_max(self.model_size)
        if resource_max["input_size"] < self.input_size:
            self.input_size = resource_max["input_size"]
        else:
            self.input_size = input_size

        self.llm = None

    def get_model_dir(self):
        url = self.source[self.model_size][self.quant]
        hf_slug = f'{url.split("/")[3]}/{url.split("/")[4]}'
        model_path = os.path.join(os.environ['CALM_ROOT'], hf_slug)
        model_path = os.path.expanduser(model_path)
        return model_path

    def get_model_filename(self):
        url = self.source[self.model_size][self.quant]
        return url.split("/")[-1]

    def resolve_path(self):
        model_filename = self.get_model_filename()
        model_path = self.get_model_dir()

        model_matches = glob(f"{model_path}/*{self.quant}*") + \
            glob(f"{model_path}/*{self.quant.lower()}*") + \
                glob(f"{model_path}/*{self.quant.upper()}*")

        if len(model_matches) > 0:
            return model_matches[0]

    def download(self):        
        # if model file exists, return
        if self.resolve_path():
            return

        # ensure model dir exists
        model_dir = self.get_model_dir()
        os.makedirs(model_dir, exist_ok=True)
        
        # using requests, download model file into model_dir
        model_url = self.source[self.model_size][self.quant]
        model_filename = self.get_model_filename()
        model_filepath = os.path.join(model_dir, model_filename)

        with requests.get(model_url, stream=True) as r:
            r.raise_for_status()
            with open(model_filepath, "wb") as f:
                for chunk in r.iter_content(chunk_size=8192):
                    f.write(chunk)

    def get_biggest(self):
        for size in ["180b", "70b", "65b", "33b", "30b", "13b", "7b", "3b", "1b"]:
            if size in self.source:
                resource_max = get_resource_max(size)
                if resource_max["quant"] in self.source[size]:
                    return {"size": size, "quant": resource_max["quant"]}
                else:
                    available = self.source[size].keys()
                    for quant in get_smaller_quants(resource_max["quant"]):
                        if quant in available:
                            return {"size": size, "quant": quant}

    def resolve_llm(self):
        if self.llm is None:
            model_path = self.resolve_path()
            if not model_path:
                raise Exception("Could not find model. Did you download it?")

            self.llm = LlamaCpp(
                model_path=model_path,
                n_ctx=self.input_size,
                n_threads=get_cores() - 1,
                n_gpu_layers=1 if has_metal() else 0,
                verbose=False,
                n_batch=1024,
                seed=-1,
            )

        return self.llm

    @classmethod
    def from_config(cls, name):
        check_filename = f"{os.path.dirname(__file__)}/../calm_data/models/{name}.yaml"
        
        if os.path.exists(check_filename):
            filename = check_filename
        elif os.path.exists(name):
            filename = name
        else:
            raise Exception(f"Could not find model {name} in {check_filename} or {name}")

        with open(filename, "r") as f:
            config = yaml.load(f, Loader=yaml.FullLoader)
        return cls(
            name=config["name"],
            input_size=config["input_size"],
            source=config["source"],
            template=config["template"],
            character=config["character"] if "character" in config else None,
        )

    def __repr__(self):
        return f"Model({self.name}, {self.model_size}, {self.quant}, {self.input_size})"
