from pydantic import BaseModel
from datetime import datetime


class Book(BaseModel):
    title: str
    author: str
    description: str
    is_deleted: bool = False
    created: int = int(datetime.timestamp(datetime.now()))
    updated: int = int(datetime.timestamp(datetime.now()))
