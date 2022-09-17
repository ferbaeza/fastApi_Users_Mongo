from pydantic import BaseModel


class Task(BaseModel):
    title: str
    author: str
    body: str