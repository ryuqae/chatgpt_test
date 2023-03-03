import openai, os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("APIKEY")


class Agent:
    def __init__(
        self,
        engine,
        temperature,
        max_tokens,
        frequency_penalty,
        presence_penalty,
    ):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def respond(self, gaslighting, message):
        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=[
                {"role": "system", "content": f"{gaslighting}"},
                {"role": "user", "content": f"{message}"},
            ],
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        return response.choices[0]


if __name__ == "__main__":
    prompt = "The following is a conversation with an AI assistant. The assistant is empathetic, helpful and very friendly."
    agent = Agent(prompt)
    message = """Human: 오늘 친구랑 심하게 다퉜어. 친구는 아주 오래된 친구고 항상 붙어다녔는데 이렇게 싸우고 나니 마음이 좋지 않아. 이런 상황에서 내가 먼저 친구한테 연락하는게 좋을까?\n AI: """

    completion = agent.respond(message)
    print(completion)
