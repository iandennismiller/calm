import os

import uvicorn
from llama_cpp.server.app import create_app, Settings

from .instances import Answerer, Assistant, Council
from .utils import get_cores, has_metal


class Calm:
    def __init__(self):
        pass

    def answer(self, question):
        self.instance = Answerer()
        self.llm = self.instance.resolve_llm()

        full_prompt = self.instance.release.template.prompt_input.format(
            system_message=self.instance.prompt.system_message,
            instruction=question,
            input=""
        )

        result_raw = self.llm(
            prompt=full_prompt,
            stop=[self.instance.release.template.response_split],
            echo=False,
            max_tokens=-1,
            temperature=self.instance.initialization.temperature
        )
        return str(result_raw['choices'][0]['text'].strip())

    def api(self):
        self.instance = Council()
        settings = Settings(
            n_ctx=self.instance.release.architecture.context_size,
            n_threads=get_cores() - 1,
            n_gpu_layers=1 if has_metal() else 0,
            model=self.instance.release.resolve_path()
        )
        app = create_app(settings=settings)
        uvicorn.run(
            app,
            host=os.getenv("HOST", settings.host),
            port=int(os.getenv("PORT", settings.port)),
        )

    def list_models(self):
        def classesinmodule(module):
            md = module.__dict__
            return [
                md[c] for c in md if (
                    isinstance(md[c], type) and md[c].__module__ == module.__name__
                )
            ]

        import calm.releases
        return classesinmodule(calm.releases)

    def consult(self, question):
        from llama_cpp_guidance.llm import LlamaCpp
        import guidance

        self.instance = Council()

        guidance.llm = LlamaCpp(
            model_path=self.instance.release.resolve_path(),
            chat_mode=True,
            n_threads=get_cores() - 1,
            n_gpu_layers=1 if has_metal() else 0,
        )

        experts = guidance(self.instance.prompt.system_message)
        result = experts(query=question)
        print(result)
