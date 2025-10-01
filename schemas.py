from fastapi import Form
from pydantic import BaseModel

class UserSchemaIn(BaseModel):
    username: str
    password: str

    @classmethod
    def as_form(cls, username: str = Form(...), password: str = Form(...)):
        return cls(username=username, password=password)

class UserSchema(BaseModel):
    id: int
    username: str
    avatar: str | None = None

    class Config:
        from_attributes = True
