import openai, os
from dotenv import load_dotenv

load_dotenv()

openai.api_key = os.getenv("APIKEY")

# print(openai.Model.list())

completion = openai.Completion()


class Agent:
    def __init__(self, prompt):
        self.prompt = prompt

    def respond(self, message):
        response = completion.create(
            engine="text-davinci-003",
            prompt=self.prompt + message,
            temperature=0.9,
            max_tokens=1000,
            top_p=1,
            frequency_penalty=0,
            presence_penalty=0.6,
            stop=["\n", "AI: "],
        )
        return response.choices[0].text


if __name__ == "__main__":
    prompt = "The following is a conversation with an AI assistant. The assistant is empathetic, helpful and very friendly.\n\n"
    agent = Agent(prompt)
    message = """Human: 오늘 친구랑 심하게 다퉜어. 친구는 아주 오래된 친구고 항상 붙어다녔는데 이렇게 싸우고 나니 마음이 좋지 않아. 이런 상황에서 내가 먼저 친구한테 연락하는게 좋을까?\n AI: """

    completion = agent.respond(message)
    print(completion)
