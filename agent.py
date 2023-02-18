import openai, os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("APIKEY")


completion = openai.Completion()


class Agent:
    def __init__(
        self,
        prompt,
        engine,
        temperature,
        max_tokens,
        frequency_penalty,
        presence_penalty,
    ):
        self.prompt = prompt
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty

    def respond(self, message):
        response = completion.create(
            engine=self.engine,
            prompt=self.prompt + message + "\n- AI: ",
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
            stop=["- AI: "],
        )
        return response.choices[0].text


if __name__ == "__main__":
    prompt = "The following is a conversation with an AI assistant. The assistant is empathetic, helpful and very friendly."
    agent = Agent(prompt)
    message = """Human: 오늘 친구랑 심하게 다퉜어. 친구는 아주 오래된 친구고 항상 붙어다녔는데 이렇게 싸우고 나니 마음이 좋지 않아. 이런 상황에서 내가 먼저 친구한테 연락하는게 좋을까?\n AI: """

    completion = agent.respond(message)
    print(completion)
