# -*-coding:utf-8-*-

from fastapi import FastAPI, Query
from typing import Union, List
from customtype import Ticket, Comment

# from fastapi.encoders import jsonable_encoder
from datetime import datetime
from agent import Agent

temperature = 1.0
max_tokens = 300
frequency_penalty = 0.6
presence_penalty = 0.6

app = FastAPI()


@app.get("/")
def read_root():
    t1 = Ticket(
        "1", "abc", "오늘 하루는 별로 기분이 좋지 않다. 이유를 모르겠는데 방법이 있을리가", datetime.now(), False
    )
    return t1


@app.get("/ai_ticket/")
async def get_ticket(keyword: str):

    agent = Agent(
        engine="gpt-3.5-turbo",
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        type="ticket",
    )

    response = agent.respond(
        ticket_keyword=keyword,
    )

    new_ticket = Ticket(
        ticket_id="2323",
        user_id="leafcle",
        text=response["message"]["content"],
        timestamp=datetime.now(),
        ai_generated=True,
    )
    return new_ticket


@app.post("/ai_comment/")
async def get_comment(
    ticket: Ticket,
    comments: List[Comment],
) -> Comment:
    assert len(ticket.text) > 3, "입력값의 길이는 0보다 커야 합니다."
    # content = """오늘 친구랑 심하게 다퉜어. 친구는 아주 오래된 친구고 항상 붙어다녔는데 이렇게 싸우고 나니 마음이 좋지 않아. 이런 상황에서 내가 먼저 친구한테 연락하는게 좋을까?"""
    # comments = ["굳이 먼저 연락 안해도 될 것 같은데요?", "친구가 잘못한건가요?"]
    # comments = {"comments": comments}

    agent = Agent(
        engine="gpt-3.5-turbo",
        temperature=temperature,
        max_tokens=max_tokens,
        frequency_penalty=frequency_penalty,
        presence_penalty=presence_penalty,
        type="comment",
    )

    response = agent.respond(
        ticket=ticket,
        comments=comments,
    )

    new_comment = Comment(
        comment_id="23513",
        ticket_id="2323",
        user_id="leafcle",
        text=response["message"]["content"],
        timestamp=datetime.now(),
        ai_generated=True,
    )
    return new_comment
