import os

import uvicorn
from llama_cpp.server.app import create_app, Settings
from llama_cpp_guidance.llm import LlamaCpp as LlamaCppGuidance
import guidance

from .utils import get_cores, has_metal
from .llm import LLM
from .character import Character


class Calm:
    def __init__(self):
        pass

    def answer(self, instance, question):
        # ensure LLM is loaded
        instance.resolve_llm()

        if instance.character.guidance:
            guidance.llm = LlamaCppGuidance(
                model_path=instance.resolve_path(),
                chat_mode=True,
                n_threads=get_cores() - 1,
                n_gpu_layers=1 if has_metal() else 0,
            )

            experts = guidance(instance.character.system_prompt)
            result = experts(query=question)
            return result
        else:
            full_prompt = instance.template["no_input"].format(
                system_prompt=instance.character.system_prompt,
                prompt=question,
                # input=""
            )

            result_raw = instance.llm(
                prompt=full_prompt,
                stop=[instance.template["stop"]],
                echo=False,
                max_tokens=-1,
                temperature=0.05
            )
            return str(result_raw['choices'][0]['text'].strip())

    def api(self, instance):
        settings = Settings(
            n_ctx=instance.input_size,
            n_threads=get_cores() - 1,
            n_gpu_layers=1 if has_metal() else 0,
            model=instance.resolve_path()
        )
        app = create_app(settings=settings)
        uvicorn.run(
            app,
            host=os.getenv("HOST", settings.host),
            port=int(os.getenv("PORT", settings.port)),
        )

    def list_models(self):
        "return a list of all available models"

        # scan models path for all yaml files, stripping .yaml from the end
        model_dir = f"{os.path.dirname(__file__)}/descriptions/models"
        model_files = os.listdir(model_dir)
        model_files = [x for x in model_files if x.endswith(".yaml")]
        models = [x[:-5] for x in model_files]

        return models

    def get_instance(self, model, character, quiet=False):
        instance = None
        loaded_character = None

        if character:
            loaded_character = Character.from_config(name=character)
            if model is None:
                model = loaded_character.model
        
        # if the model is still none, default to Mistral
        if model is None:
            model = "mistral"

        instance = LLM.from_config(name=model)

        if loaded_character:
            instance.character = loaded_character
        elif instance.character is not None:
            instance.character = Character.from_config(name=instance.character)
        else:
            instance.character = Character.from_config(name="chatter-gpt")

        if not quiet:
            print(f"Loaded {instance}, {instance.character}")
        
        return instance
