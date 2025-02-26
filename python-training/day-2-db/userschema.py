
from pydantic import BaseModel
from typing import Optional
class Users(BaseModel):
    uname: str
    email: str
    city: str
class UsersCreate(Users):
    pass