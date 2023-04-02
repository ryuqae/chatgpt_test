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


# 유저별 사용 정보
class user_collection(BaseModel):
    user_id: str
    last_login_timestamp: datetime
    last_login_location: dict
    last_create_ticket_timestamp: datetime
    last_create_comment_timestamp: datetime
    user_ticket_count: int
    user_comment_count: int
    user_like_count: int
    user_get_ticket_report_count: int
    user_get_comment_report_count: int
    user_give_ticket_report_count: int
    user_give_comment_report_count: int


# 티켓에 대한 정보
class ticket_collection(BaseModel):
    ticket_id: str
    ticket_order: str
    user_id: str
    ticket_created_location: dict
    ticket_created_timestamp: datetime
    is_ticket_ai_generated: bool
    is_ticket_admin_generated: bool
    ticket_content: str
    ticket_comment_count: int
    ticket_like_count: int
    ticket_report_count: int
    is_ticket_banned: bool
    tickect_revised_timestamp: datetime


# 댓글에 대한 정보
class comment_collection(BaseModel):
    comment_id: str
    ticket_id: str
    user_id: str
    comment_order: int
    is_comment_ai_generated: bool
    is_comment_admin_generated: bool
    comment_created_timestamp: datetime
    comment_content: str
    comment_report_count: int
    is_comment_banned: bool

    # 유저별 특정 티켓을 열람/작성했는지와 관련된 메타 정보


class user_ticket_collection(BaseModel):
    user_id: str
    ticket_id: str
    is_user_created: bool
    is_user_comment: bool
    is_user_like: bool
    is_user_report: bool
