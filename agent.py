# -*-coding:utf-8-*-

import openai, os
from dotenv import load_dotenv
from typing import Union, List
from customtype import Ticket, Comment

load_dotenv()

openai.api_key = os.getenv("APIKEY")


class Agent:
    def __init__(
        self, engine, temperature, max_tokens, frequency_penalty, presence_penalty, type
    ):
        self.engine = engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.frequency_penalty = frequency_penalty
        self.presence_penalty = presence_penalty
        self.type = type

    def respond(
        self,
        ticket: Ticket = None,
        comments: List[Comment] = None,
        ticket_keyword: str = None,
    ):
        if self.type == "ticket":
            assert ticket_keyword is not None, "Ticket을 발행하려면 키워드가 필요합니다."
            botsona = f"{ticket_keyword}에 관련된 고민 한 가지를 200자 이내로 친구에게 털어놓듯이 얘기하는 봇"
            messages = [
                {"role": "system", "content": botsona},
                {"role": "user", "content": "그 고민을 갖고있는 사람이 말하는것처럼 얘기해줘"},
            ]

        elif self.type == "comment":
            assert Ticket is not None, "댓글을 작성하려면 Ticket이 필요합니다."
            botsona = "따뜻한 말로 친구한테 얘기하듯 자연스럽게 공감해줘"
            messages = [
                {"role": "system", "content": botsona},
                {"role": "user", "content": ticket.text},
                *[
                    {"role": "assistant", "content": comment.text}
                    for comment in comments[-3:]
                ],
            ]

        response = openai.ChatCompletion.create(
            model=self.engine,
            messages=messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens,
            top_p=1,
            frequency_penalty=self.frequency_penalty,
            presence_penalty=self.presence_penalty,
        )
        return response.choices[0]


if __name__ == "__main__":
    temperature = 1.0
    max_tokens = 300
    frequency_penalty = 0.6
    presence_penalty = 0.6

    agent = Agent(
        engine="gpt-3.5-turbo",
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
    )
    content = """오늘 친구랑 심하게 다퉜어. 친구는 아주 오래된 친구고 항상 붙어다녔는데 이렇게 싸우고 나니 마음이 좋지 않아. 이런 상황에서 내가 먼저 친구한테 연락하는게 좋을까?\n AI: """

    response = agent.respond(
        botsona="따뜻한 말로 친구한테 얘기하듯 자연스럽게 공감해줘",
        content=content,
        comments=["굳이 먼저 연락 안해도 될 것 같은데요?", "친구가 잘못한건가요?"],
    )

    print(response["message"]["content"])
