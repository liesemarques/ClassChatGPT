import openai


class MyOpenAI:
    def __int__(self, model, prompt, max_toquens, temperature, n, key):
        self.model = model
        self.prompt = prompt
        self.max_tokens = max_toquens
        self.teperature = temperature
        self.n = n
        self.key = key
        openai.api_key = self.key

    def callgpt(self):
        response = openai.Completion.create(
            model = self.model,
            prompt = self.prompt,
            max_toquens = self.max_tokens,
            temperature = self.teperature,
            n = self.n,
        )
        resp = []

        for a in range(len(response.choices)):
            resp.append(response.choices[a].text)
        return resp




