from pydantic import BaseModel
from datetime import datetime


class Ticket(BaseModel):
    ticket_id: str
    user_id: str
    text: str
    timestamp: datetime
    ai_generated: bool


class Comment(BaseModel):
    comment_id: str
    ticket_id: str
    user_id: str
    text: str
    timestamp: datetime
    ai_generated: bool
