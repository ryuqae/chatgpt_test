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
    return "잎클: 안녕? 나는 인공지능이야."


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
