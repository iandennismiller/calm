from .model.instances import Answerer, Assistant


class Calm:
    def __init__(self, num_threads=1, gpu_layers=1):
        self.num_threads = num_threads
        self.gpu_layers = gpu_layers

    def answer(self, question):
        self.instance = Answerer()
        self.llm = self.instance.resolve_llm(
            num_threads=self.num_threads,
            gpu_layers=self.gpu_layers
        )

        full_prompt = self.instance.release.template.prompt_input.format(
            system_message=self.instance.prompt.system_message,
            input=question
        )

        result_raw = self.llm(
            prompt=full_prompt,
            stop=[self.instance.release.template.response_split],
            echo=False,
            max_tokens=-1,
            temperature=self.instance.initialization.temperature
        )
        return str(result_raw['choices'][0]['text'].strip())


if __name__ == "__main__":
    calm = Calm()
    calm.answer("What is the meaning of life?")
